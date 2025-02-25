pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops-demo-jenkins.git']])
            }
        }

        stage ('Building') {
            steps {
                sh 'pip3 install -r requirements.txt'
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