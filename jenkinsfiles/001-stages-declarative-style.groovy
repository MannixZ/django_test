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
        steps {
          script {
            echo 'Stage 3'
        }
      }
    }
    
    stage('Stage 4') {
        when {
          branch 'master'}
          steps {
            echo 'i am master'
      }
    }

  }
}
