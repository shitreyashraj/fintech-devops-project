pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t fintech-app:latest .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-pat-system',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        powershell -NoProfile -Command "$env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin"

                        if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

                        docker tag fintech-app:latest %DOCKER_USER%/fintech-app:latest

                        docker push %DOCKER_USER%/fintech-app:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" apply -f terraform\\k8s\\configmap.yaml -f terraform\\k8s\\secret.yaml -f terraform\\k8s\\deployment.yaml -f terraform\\k8s\\service.yaml -f terraform\\k8s\\hpa.yaml

                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" -n fintech set image deployment/fintech-app fintech-app=shitreyashraj/fintech-app:latest

                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" -n fintech rollout status deployment/fintech-app

                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" -n fintech get pods

                    "C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" -n fintech get hpa
                '''
            }
        }
    }
}