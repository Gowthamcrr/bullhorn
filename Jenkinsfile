node {
   stage ('req_install') {
    checkout scm
    sh 'sudo yum install -y python-pip'
	sh 'sudo pip install xmlutils'
	sh 'sudo yum install -y docker'
	sh 'sudo systemctl restart docker'
  }
   stage ('xml2csv') {
    sh 'python assessment.py'
  }
   stage ('push_artifacts') {
    sh 'docker run -d -p 8081:8081 --name nexus sonatype/nexus3:3.15.2'
	sh 'sleep 5m'
	sh 'curl -v -u admin:admin123 -X POST 'http://localhost:8081/service/rest/v1/components?repository=maven-releases' -F maven2.groupId=bullhorn -F maven2.artifactId=devops -F maven2.version=1 -F maven2.asset1=@output/out.csv -F maven2.asset1.extension=csv'
  }
}
