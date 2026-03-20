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
            agent { label 'master' }
            steps {
                git 'https://github.com/doanvanhung123/playwright_python'
            }
        }

        stage('Run Tests Parallel') {
            parallel {

                stage('Machine 1') {
                    agent { label 'agent1' }
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
                    agent { label 'agent2' }
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

                stage('Machine 3') {
                    agent { label 'agent3' }
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
            agent { label 'master' }
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}