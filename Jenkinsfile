node {
   stage ('req_install') {
    checkout scm
    sh 'sudo yum install -y python-pip'
	sh 'sudo pip install xmlutils'
  }
   stage ('xml2csv') {
    checkout scm
    sh 'python assessment.py'
  }
}
