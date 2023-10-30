pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                script{
                    dockerapp = docker.build("aldrikalvaro/teste", '-f ./Dockerfile ./')
                }
            }
        }
    }
}
