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
                echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

                docker tag fintech-app:latest %DOCKER_USER%/fintech-app:latest
                docker push %DOCKER_USER%/fintech-app:latest
            '''
        }
    }
}