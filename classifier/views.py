import pandas as pd
import numpy as np

from django.shortcuts import render
from .forms import CSVUploadForm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from io import TextIOWrapper

def upload_and_train(request):
    # Initialize variables for template
    trained_model_name = None
    accuracy_value = None
    class_report_list = None
    conf_matrix_list = None
    error_message = None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                csv_file = request.FILES['csv_file']
                df = pd.read_csv(TextIOWrapper(csv_file.file, encoding='utf-8'))

                if 'label' not in df.columns:
                    error_message = "CSV must contain a 'label' column."
                else:
                    X = df.drop('label', axis=1)
                    y = df['label']

                    train_size = form.cleaned_data['train_size']
                    X_train, X_test, y_train, y_test = train_test_split(
                        X, y, train_size=train_size, random_state=42
                    )

                    model_choice = form.cleaned_data['model_choice']
                    trained_model_name = model_choice

                    if model_choice == 'logistic_regression':
                        model = LogisticRegression(max_iter=1000)
                    elif model_choice == 'naive_bayes':
                        model = GaussianNB()
                    elif model_choice == 'random_forest':
                        model = RandomForestClassifier()
                    elif model_choice == 'neural_network':
                        model = MLPClassifier(max_iter=1000)
                    else:
                        model = LogisticRegression(max_iter=1000)

                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)

                    # Metrics
                    accuracy_value = round(accuracy_score(y_test, y_pred) * 100, 2)

                    # Classification report
                    raw_report = classification_report(y_test, y_pred, output_dict=True)
                    class_report_list = []
                    for label, metrics in raw_report.items():
                        if label not in ['accuracy', 'macro avg', 'weighted avg']:
                            class_report_list.append({
                                'label': label,
                                'precision': round(metrics['precision'], 2),
                                'recall': round(metrics['recall'], 2),
                                'f1_score': round(metrics['f1-score'], 2),
                                'support': metrics['support']
                            })

                    # Confusion matrix
                    conf_matrix_list = confusion_matrix(y_test, y_pred).tolist()

                    cm_array = np.array(conf_matrix_list)
                    num_classes = cm_array.shape[0]
                    conf_matrix_detailed = []

                    for i in range(num_classes):
                        TP = cm_array[i, i]
                        FP = cm_array[:, i].sum() - TP
                        FN = cm_array[i, :].sum() - TP
                        TN = cm_array.sum() - (TP + FP + FN)
                        conf_matrix_detailed.append({
                            'class_index': i,
                            'TP': int(TP),
                            'TN': int(TN),
                            'FP': int(FP),
                            'FN': int(FN)
                        })

                    # Pass this to template instead of raw matrix
                    conf_matrix_list = conf_matrix_detailed

                    

            except Exception as e:
                error_message = str(e)
    else:
        form = CSVUploadForm()

    return render(request, 'classifier/upload.html', {
        'form': form,
        'trained_model_name': trained_model_name,
        'accuracy_value': accuracy_value,
        'class_report_list': class_report_list,
        'conf_matrix_list': conf_matrix_list,
        'error_message': error_message
    })
