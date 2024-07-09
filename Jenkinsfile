pipeline{
    agent any
    stages{
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