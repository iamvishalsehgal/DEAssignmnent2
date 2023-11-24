# DEAssignmnent2
This is a Data Engineering Assignment 2 at JADS

The goal of this assignment is to design and implement data architectures and data processing pipelines using Apache Spark and GCP services.

Some part of the architecture is done in Virtal Machine in Google Cloud. Because of budget limitations, every time you restart the virtual machine you need to enter a new IP address. 

Docker and docker compose must be installed. 
External IP as well as home direcotory must be specified in the .env file
To start the cluster:
first `sudo docker compose build` and later `sudo docker compose up -d`. 
To stop the cluster:
`sudo docker compose down`

To connect to Jupyter Lab (Spark App and Driver) run: `sudo docker logs spark-driver-app`



Data has been taken from: 
https://www.kaggle.com/datasets/nathanlauga/nba-games/data
