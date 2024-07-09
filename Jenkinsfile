pipeline{
    agent any
    stages{
        stage('Test Docker Compose') {
            steps {
                sh 'docker-compose --version'
            }
        }
        stage('Docker down'){
            steps   {
                sh '''
                docker-compose down 
                '''
            }}

        stage('Docker up'){
            steps   {
                sh '''
                docker-compose up --build
                '''

            }}
    }
}