pipeline{
    agent any
    stages{
        stage('Docker down'){
        steps   {
            sh 'docker-compose down -v'
        }}

        stage('Docker up'){
        steps   {
            sh 'docker-compose up --build'
        }}
    }
}