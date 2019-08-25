# Bullhorn Assessment

Pre Installed Software Required:
1. Java
2. Jenkins
3. Python (Default with Centos)

Software Installed by Groovy Script:
1. Docker
2. Python-pip
3. Pip Module - xmlutils

Working Procedure: 
Step 1: Create a Pipeline job in Jenkins
Step 2: In the Pipeline tab Choose "Pipeline Script from SCM" in Definition
Step 3: Choose "Git" as SCM
Step 4: Provide "https://github.com/sunlove123/bullhorn.git" as Repo url and Save.
Step 5: Execute the Newly Configured Job to get the desired output

Artifact Management:
You can download the final artifact from "you can download the artifact in: http://{Jenkins_IP}:8081/repository/maven-releases/bullhorn/devops/1/devops-1.csv"

Note:
Assume that the port "8081" of host machine is available. If incase the post is not availale in the host machine, Kindly Fork my repo and change the host port of Docker run command and  also change the respective port in Nexus Rest API.


How to Use:
Keep all your "n x candidate.xml" inside "input" folder
You can get your output in "output/out.csv" also can find it inside Nexus Repo "http://{Jenkins_IP}:8081/repository/maven-releases/bullhorn/devops/1/devops-1.csv"
