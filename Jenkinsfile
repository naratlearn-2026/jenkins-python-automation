pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    environment {
        API_URL = 'https://httpbin.org/basic-auth/dummyuser/dummypass'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('API Pre-check') {
            environment {
                API_CREDS = credentials('api-creds')
            }
            steps {
                sh '''
                    . venv/bin/activate
                    export API_USERNAME="${API_CREDS_USR}"
                    export API_PASSWORD="${API_CREDS_PSW}"
                    python src/main.py
                '''
            }
        }
    }

    post {
        success {
            echo 'API validation succeeded'
        }
        failure {
            echo 'API validation failed'
        }
    }
}

