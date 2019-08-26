# Bullhorn Assessment

Pre Installed Software Required:<br />
1. Java<br />
2. Jenkins<br />
3. Python (Default with Centos)<br />
<br />
Software Installed by Groovy Script:<br />
1. Docker<br />
2. Python-pip<br />
3. Pip Module - xmlutils<br />
<br />
Working Procedure: <br />
Step 1: Create a Pipeline job in Jenkins<br />
Step 2: In the Pipeline tab Choose "Pipeline Script from SCM" in Definition<br />
Step 3: Choose "Git" as SCM<br />
Step 4: Provide "https://github.com/sunlove123/bullhorn.git" as Repo url and Save.<br />
Step 5: Execute the Newly Configured Job to get the desired output<br />
<br />
Artifact Management:<br />
You can download the final artifact from "you can download the artifact in: http://{Jenkins_IP}:8081/repository/maven-releases/bullhorn/devops/1/devops-1.csv"<br />
<br />
Note:<br />
Assumption 1: Assume that the port "8081" of host machine is available. If incase the post is not availale in the host machine, Kindly Fork my repo and change the host port of Docker run command and  also change the respective port in Nexus Rest API.<br />
Assumption 2: All XML are from portal which follows the defined XSD, which helps me to skip the XML and XML tag validation part.<br />
<br />
<br />
How to Use:<br />
Keep all your "n x candidate.xml" inside "input" folder. <br />
You can get your output in "output/out.csv" also can find it inside Nexus Repo "http://{Jenkins_IP}:8081/repository/maven-releases/bullhorn/devops/1/devops-1.csv"<br />
