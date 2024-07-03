pipeline{
    agent any
    environment {
        REPO_DIR = '/home/chyngyz/Desktop/cicdproject/' // Укажите путь к вашему локальному репозиторию
    }
    stages{
        stage('Docker down'){
            steps   {
                dir(REPO_DIR){     
                    script {
                        sh 'sudo docker-compose down -v'
                    }
            }
            }}

        stage('Docker up'){
            steps   {
                dir(REPO_DIR){
                    script {
                        sh 'sudo docker-compose up --build'
                    }
                }
            }}
    }
}