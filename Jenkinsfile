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
            powershell '''
                $env:DOCKER_PASS | docker login -u $env:DOCKER_USER --password-stdin
                if ($LASTEXITCODE -ne 0) {
                    exit $LASTEXITCODE
                }

                docker tag fintech-app:latest "$env:DOCKER_USER/fintech-app:latest"
                docker push "$env:DOCKER_USER/fintech-app:latest"
            '''
        }
    }
}