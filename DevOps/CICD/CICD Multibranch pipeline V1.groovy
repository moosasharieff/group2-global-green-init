pipeline {
    agent none

    environment {
        DOCKER_IMAGE = 'arunthopil/pro-green-v2'
    }

    stages {
        stage('Setup') {
            agent any
            steps {
                script {
                    ENVIRONMENT = BRANCH_NAME == 'main' ? 'Demo' :
                                  BRANCH_NAME == 'production' ? 'Production'
                                  BRANCH_NAME == 'staging' ? 'Staging' :
                                  BRANCH_NAME.startsWith('test') ? 'Testing' : 'De'
                    echo "Environment set to ${ENVIRONMENT}"
                }
            }
        }

        stage('Checkout Code') {
            agent any
            steps {
                checkout scm
            }
        }

        stage('Prepare and Build') {
            agent { docker { image 'node:21' } }
            steps {
                dir('client') {
                    sh 'npm install'
                    sh 'npm run build'
                    stash includes: '**', name: 'build-artifacts'
                }
            }
        }

        stage('Analyze and Scan') {
            agent any
            steps {
                script {
                    unstash 'build-artifacts'
                    dir('client') {
                        withSonarQubeEnv('Sonarcube') {
                            sh "sonar-scanner -Dsonar.projectKey=my-project -Dsonar.sources=. -Dsonar.host.url=https://sonarqube.globalgreeninit.world -Dsonar.login=${env.SONARQUBE_TOKEN}"
                        }
                        // Snyk scan (corrected placement and syntax)
                        //withCredentials([string(credentialsId: 'snyk-token', variable: 'SNYK_TOKEN')]) {
                            snykSecurity failOnError: false, failOnIssues: false, organisation: 'Group2-Global-Green', projectName: 'For-Green2', snykInstallation: 'Snyk', snykTokenId: 'snyk-token', targetFile: '/client/package.json'
                        }
                    }
                }
            }
        }

        stage('Build and Push Docker Image') {
            agent any
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'Dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        def dockerImage = "${DOCKER_IMAGE}:${BRANCH_NAME}-${env.BUILD_NUMBER}"
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                        sh "docker build -t ${dockerImage} ."
                        sh "docker push ${dockerImage}"
                    }
                }
            }
        }

        stage('Deploy') {
            agent any
            steps {
                script {
                    def sshCredentialsId = ENVIRONMENT == 'Production' ? 'prod-ssh-credentials-id' :
                                           ENVIRONMENT == 'Staging' ? 'stage-ssh-credentials-id' :
                                           ENVIRONMENT == 'Testing' ? 'test-ssh-credentials-id' :
                                           'ssh-wsl' // Default to Demo credentials

                    def dockerHost = ENVIRONMENT == 'Production' ? 'prod-user@prod-docker-host' :
                                      ENVIRONMENT == 'Staging' ? 'stage-user@stage-docker-host' :
                                      ENVIRONMENT == 'Testing' ? 'test-user@test-docker-host' :
                                      'host.docker.internal' // Default to Demo host

                    if (sshCredentialsId && dockerHost) {
                        sshagent([sshCredentialsId]) {
                            def dockerImage = "${DOCKER_IMAGE}:${BRANCH_NAME}-${env.BUILD_NUMBER}"
                            sh """
                               ssh -o StrictHostKeyChecking=no ${dockerHost} 'docker pull ${dockerImage} && docker stop ${BRANCH_NAME}-app || true && docker rm ${BRANCH_NAME}-app || true && docker run -d --name ${BRANCH_NAME}-app -p 80:3000 ${dockerImage}'
                            """
                        }
                    } else {
                        echo "Deployment environment not configured properly."
                    }
                }
            }
        }
}

    post {
        always {
            echo "Pipeline execution completed for ${ENVIRONMENT}"
        }
    }

