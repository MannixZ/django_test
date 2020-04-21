pipeline {
  agent any
  stages {

    stage('Stage 1') {
      steps {
        script {
          echo 'Stage 1'
        }
      }
    }

    stage('Stage 2') {
      steps {
        script {
          echo 'Stage 2'
        }
      }
    }
    
    stage('Stage 3') {
      when {
        steps {
          script {
            echo 'Stage 2'
        }
      }
      }
    }

  }
}
