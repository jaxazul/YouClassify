# YouClassify

YouClassify is a Django-based web application that enables users to upload datasets, select and train machine learning classification models from scikit-learn, save their trained models, and classify new data instantly. The app features user authentication and personalized model management.

## Features

- User registration, login, and authentication  
- Upload datasets in CSV format  
- Choose from multiple scikit-learn classification models (e.g., Random Forest, SVM, Logistic Regression)  
- Train and save models per user  
- Classify new datasets using saved models  
- View and manage previously saved models  

## Tech Stack

- Backend: Django  
- Machine Learning: scikit-learn  
- Frontend: Django templates (HTML, CSS, JavaScript)  
- Deployment: AWS (Elastic Beanstalk recommended)  
- Containerization: Docker support for easy setup and deployment  

## Getting Started

### Prerequisites

- Python 3.8+  
- pip  
- virtualenv (optional but recommended)  
- Docker (optional, if you prefer containerized setup)  

### Installation

#### Using virtual environment

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/youclassify.git
    cd youclassify
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional, for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your browser at `http://127.0.0.1:8000/`

#### Using Docker

1. Build the Docker image:

    ```bash
    docker build -t youclassify .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8000:8000 youclassify
    ```

3. Open your browser at `http://127.0.0.1:8000/`

## Usage

- Register a new account or log in.  
- Upload a CSV dataset and select a model to train.  
- Save your trained model for later use.  
- Upload new data and classify it using your saved models.  

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License](LICENSE)

## Contact

Your Name – olugbilehassan@gmail.com 
