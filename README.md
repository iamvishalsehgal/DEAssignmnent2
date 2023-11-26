# DEAssignmnent2
This is a Data Engineering Assignment 2 at JADS

The goal of this assignment is to design and implement data architectures and data processing pipelines using Apache Spark and GCP services.

Some part of the architecture is done in Virtal Machine in Google Cloud. Because of budget limitations, every time you restart the virtual machine you need to enter a new IP address. 
Virtual machine used in this assignment: 
- Machine type: e2-standard-4
- Architecture: x86/64

Docker and docker compose must be installed. 
External IP as well as home directory must be specified in the .env file
To start the cluster:
first `sudo docker compose build` and later `sudo docker compose up -d`. 
To stop the cluster:
`sudo docker compose down`

To connect to Jupyter Lab (Spark App and Driver) run: `sudo docker logs spark-driver-app`


1st pipeline: batch data processing pipeline
2nd pipeline: stream data processing pipeline 
    - we are using KAFKA to produce and consume data (1st run admin, then start notebook, then run producer and in the end run consumer)
    - check spark jobs by accessing it on YOUR_VM:4040/jobs/ 
    

Data has been taken from: 
https://www.kaggle.com/datasets/nathanlauga/nba-games/data (still APA references to be added)
