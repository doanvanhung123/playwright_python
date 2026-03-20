pipeline {
    agent none

    parameters {
        string(name: 'BROWSER', defaultValue: 'chromium', description: 'Browser')
        string(name: 'WORKERS', defaultValue: '2', description: 'Workers per machine')
        string(name: 'ENV', defaultValue: 'dev', description: 'Environment')
        string(name: 'MARKER', defaultValue: '', description: 'Pytest marker (smoke, regression...)')
    }

    stages {
        stage('Checkout') {
            agent { label 'node-1' }
            steps {
                git branch: 'main', url: 'https://github.com/doanvanhung123/playwright_python'
            }
        }

        stage('Run Tests Parallel') {
            parallel {

                stage('Machine 1') {
                    agent { label 'node-1' }
                    steps {
                        sh """
                        chmod +x runtest.sh
                        ./runtest.sh \
                          --browser ${params.BROWSER} \
                          --workers ${params.WORKERS} \
                          --env ${params.ENV} \
                          -m "${params.MARKER}"
                        """
                    }
                }

                stage('Machine 2') {
                    agent { label 'node-2' }
                    steps {
                        sh """
                        chmod +x runtest.sh
                        ./runtest.sh \
                          --browser ${params.BROWSER} \
                          --workers ${params.WORKERS} \
                          --env ${params.ENV} \
                          -m "${params.MARKER}"
                        """
                    }
                }
            }
        }

        stage('Allure Report') {
            agent { label 'node-1' }
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}