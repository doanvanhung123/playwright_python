pipeline {
    agent none

    parameters {
        string(name: 'BROWSER', defaultValue: 'chromium')
        string(name: 'WORKERS', defaultValue: '2')
        string(name: 'ENV', defaultValue: 'dev')
        string(name: 'MARKER', defaultValue: '')
    }

    stages {
        stage('Run Tests Parallel') {
            parallel {

                stage('Machine 1') {
                    agent { label 'node-1' }
                    steps {
                        checkout scm
                        bat "runtest.bat ${params.BROWSER} ${params.WORKERS} ${params.ENV} ${params.MARKER}"
                        stash includes: 'allure-results/**', name: 'allure-node1'
                    }
                }

                stage('Machine 2') {
                    agent { label 'node-2' }
                    steps {
                        checkout scm
                        bat "runtest.bat ${params.BROWSER} ${params.WORKERS} ${params.ENV} ${params.MARKER}"
                        stash includes: 'allure-results/**', name: 'allure-node2'
                    }
                }
            }
        }

        stage('Allure Report') {
            agent { label 'node-1' }
            steps {
                unstash 'allure-node1'
                unstash 'allure-node2'
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}