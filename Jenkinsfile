pipeline{
    agent any
    stages{
        stage('Docker down'){
        steps   {
            script {
                sh 'docker-compose down -v'
            }
        }}

        stage('Docker up'){
        steps   {
            script {
                sh 'docker-compose up --build'
            }
        }}
    }
}