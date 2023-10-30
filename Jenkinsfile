pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                script{
                    dockerapp = docker.build("aldrikalvaro/teste:${env.BUILD_ID}", '-f ./Dockerfile ./')
                }
            }
        }
    }
}
