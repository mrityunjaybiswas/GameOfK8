###1.1 Here I will show how to build a small python tool, writing basic of docker files, Deployments and all.
==================================================================================================================================================
pre-requisite:

  Python 
  
To run this python file :

python employeeData.py

It will ask you : 

  Enter User ID (or type exit to exit):
  
Until you type exit it will keep asking you the user id.

For Running Api-employeeData.py

python Api-employeeData.py

Open browser and put this in Address bar http://localhost:5000/userid?id=ID 

ex. http://localhost:5000/userid?id=2


###2.1 To dockerized the API 
==================================================================================================================================================

Too create docker image out of Docker file : docker build -t APPNAME .

To Check the docker image : docker images

To run the docker container on 5000 : docker run -d -p 5000:5000 APPNAME

Once you see container is up and running, go to the browser and hit : 

localhost:5000/health  --> To check the app status

localhost:5000/userid?id=1 --> to see the details for user id 1

###3.1 To Deploy the API as POD
==================================================================================================================================================

Its time to land on everyone’s favourite Kubernetes, and as its a demo for now I am using minikube on my windows system:

To start minikube : minikube start

To Deploy the Application I have made it very simple so we need only two things :

1. Deployment
2. Service
Create a namespace with name employeedata : kubectl create ns employeedata

To create deployment and nodeport service : kubectl apply -f Deployement-employeedata.yaml

To make the service available outside : minikube service employeeapp-service -n employeedata --url

From the above command you will get the ip to access the application from the browser, and then you will need to type :

http://127.0.0.1:60075/health --> To test the application running or not.

http://127.0.0.1:60075/userid?id=8 --> To see the details for userid 8

