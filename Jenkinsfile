pipeline {
  agent any
  stages {
    stage('Unit tests') {
      steps {
        sh 'python -m unittest discover -s tests'
      }
    }

  }
}