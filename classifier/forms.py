from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class DatasetUploadForm(forms.Form):
    dataset = forms.FileField()


from django import forms

MODEL_CHOICES = [
    ('logistic_regression', 'Logistic Regression'),
    ('naive_bayes', 'Naive Bayes'),
    ('random_forest', 'Random Forest'),
    ('neural_network', 'Neural Network'),
]

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label="Upload CSV")
    train_size = forms.FloatField(
        label="Training Size (0-1)",
        min_value=0.1,
        max_value=0.9,
        initial=0.8
    )
    model_choice = forms.ChoiceField(
        choices=MODEL_CHOICES,
        label="Select Model"
    )
