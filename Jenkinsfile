pipline{
    agent any
    stages{
        stage('Docker down')
        {
            sh 'docker-compose down -v'
        }

        stage('Docker up')
        {
            sh 'docker-compose up --build'
        }
    }
}