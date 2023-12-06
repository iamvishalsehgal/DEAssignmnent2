# DEAssignmnent2
This is a Data Engineering assignment 2 at JADS

The goal of this assignment is to design and implement data architectures and data processing pipelines using Apache Spark and GCP services.

Spark Driver App is run on Virtual Machine in Google Cloud. Because of budget limitations, every time you restart the virtual machine you need to enter a new IP address. 
Virtual machine used in this assignment: 
- Machine type: e2-standard-4
- Architecture: x86/64
- Zone: us-central1-a
- Storage boot disk: ubuntu-2204-jammy-v20230908

Prerequisities:
- Docker and docker compose must be installed. (`sh docker.sh` and `sh docker_compose.sh`)
- External IP as well as home directory must be specified in the .env file

To build and start the cluster: first `sudo docker compose build` and later `sudo docker compose up -d`. 

To stop the cluster:
`sudo docker compose down`

To connect to Jupyter Lab (Spark App and Driver) run: `sudo docker logs spark-driver-app`

- **1st pipeline**: batch data processing pipeline: retrieves information how many times each team finished in the top 3 in the NBA (regardless of the conference) based on points scored home.


- **2nd pipeline**: stream data processing pipeline: retrieves information from JSON data produced by Kafka producer and consumed by Kafka consumer who are the players who scored the most points 
    - we are using KAFKA to produce and consume data (1st run admin, then start notebook, then run producer and in the end run consumer)
    - check spark jobs by accessing it on YOUR_VM:4040/jobs/ 


Kafkacat was used to understand and debugg kafka processes: `sudo apt install kafkacat`

Data has been taken from: 
- NBA games data. (2022, December 23). Kaggle. 
https://www.kaggle.com/datasets/nathanlauga/nba-games/data
