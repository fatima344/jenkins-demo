pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/fatima344/jenkins-demo.git']])
            }
        }

        stage ('Building') {
            steps {
                bat 'pip3 install -r req.txt'
            }
        }

        stage ('Testing') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage ('Deployment') {
            steps {
                script {
                    deploy()
                }
            }
        }
    }
}

def void deploy() {
    println("BUILD NUMBER : ${env.BUILD_NUMBER}")
}