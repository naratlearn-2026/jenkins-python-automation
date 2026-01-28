pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
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

    stage('Run automation') {
            environment {
                API_CREDS = credentials('api-creds')
            }
            looks {
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
            echo 'Pipeline succeeded'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}

