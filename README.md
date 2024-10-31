# 🌍 Happiness Prediction Project by Country

## 📜 General Description

This project utilizes happiness data from various countries over several years (2015-2019) to train a regression model that predicts happiness scores. The structure includes a complete workflow, from data exploration and transformation (EDA/ETL) to storing predictions in a database, as well as training and evaluating the model. Additionally, a real-time data streaming system is implemented using Apache Kafka.

## 🎯 Project Objective

The objective is to train a regression model using historical data to predict happiness scores for different countries. The data is analyzed and cleaned through EDA, and the trained model is tested using 70% of the data for training and the remaining 30% for testing. Accuracy is evaluated through performance metrics, and the results are stored in a database for further analysis.

![image](https://github.com/caroldvarela/images/blob/main/workshop3.png)

## 🛠️ Technologies Used

- **Programming Language**: Python 🐍
- **Notebooks**: Jupyter Notebook 📓
- **Machine Learning**: Scikit-learn 📊
- **Data Streaming**: Apache Kafka 📡
- **Database**: Your choice (e.g., PostgreSQL, MySQL, SQLite) 💾
- **Docker**: for deployment and service configuration 🐳

## 📂 Project Structure

The structure of the project is as follows:

```plaintext
.
├── data
│   ├── 2015.csv
│   ├── 2016.csv
│   ├── 2017.csv
│   ├── 2018.csv
│   └── 2019.csv
│   └── data_clean.csv
├── database
│   ├── db_utils.py
│   └── model.py
├── models
│   └── best_model_Random_forest.pkl
├── notebooks
│   ├── 001_EDA_and_model_training.ipynb
│   └── 002_model_metrics.ipynb
├── src
├── .gitignore
├── README.md
├── docker-compose.yml
├── main.py
└── requirements.txt
```

## 🛠️ Component Description

- **`data/`**: Contains CSV files with information about happiness scores from various countries between 2015 and 2019. It also includes a `data_clean.csv` file resulting from data cleaning and transformation. 📊
  
- **`database/`**: Contains `db_utils.py` for database handling and `model.py` to store predictions with their respective inputs in the database. 💾

- **`models/`**: Folder where the best trained and serialized model (`best_model_Random_forest.pkl`) is stored, which is used for making predictions. 🤖

- **`notebooks/`**: Includes Jupyter notebooks for performing EDA, training the model, and calculating performance metrics on the test data. 📓

- **`src/`**: Additional source code for data manipulation and streaming with Kafka. 🔄

- **`main.py`**: Main script to run the complete pipeline: data loading, processing, predictions, and storage. 🚀

## ⚙️ Setup and Execution

First, you need to have a few things installed. Here’s a brief tutorial on how to do it.

## Installing Docker on Ubuntu <img src="https://upload.wikimedia.org/wikipedia/commons/7/79/Docker_%28container_engine%29_logo.png" alt="Docker Logo" width="70" style="vertical-align: middle;"/>


1. **Update your system**  
   Update the package list and install available updates:
   ```bash
   sudo apt update && sudo apt upgrade -y

2. **Install certificates and data transfer tool**  
   Install the necessary certificates and curl for data transfer:
   ```bash
   sudo apt-get install ca-certificates curl

3. **Create a secure directory for APT repository keys**  
   Create a directory to store the repository keys:
   ```sql
   sudo install -m 0755 -d /etc/apt/keyrings
   
4. **Download and save the Docker GPG key to the system**  
   Download the Docker GPG key and save it in the created directory:
   
   ```bash
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   
5. **Grant read permissions to all users for the Docker GPG key**  
   Allow all users to read the GPG key:
   ```bash
   sudo chmod a+r /etc/apt/keyrings/docker.asc

6. **Add the Docker repository and update the package list**  
   Add the Docker repository to the APT sources and update the package list:
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   sudo apt-get update
   
7. **Install Docker Engine, CLI, Containerd, Buildx, and Compose plugins**  
   Install Docker and its necessary components:
   ```bash
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

## Installing PostgreSQL <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Postgresql_elephant.svg/200px-Postgresql_elephant.svg.png" alt="PostgreSQL Logo" width="30" style="vertical-align: middle;"/>

1. **Set Up PostgreSQL**  
   Install and configure PostgreSQL:
   ```bash
   sudo apt update
   sudo apt-get -y install postgresql postgresql-contrib
   sudo service postgresql start
   sudo apt-get install libpq-dev python3-dev

2. **Log in to PostgreSQL**  
   Run the following commands to log in:
   ```bash
   sudo -i -u postgres
   psql

3. **Create a New Database and User**  
   Run the following SQL commands to create a new user and database:
   ```sql
   CREATE USER <your_user> WITH PASSWORD '<your_password>';
   ALTER USER <your_user> WITH SUPERUSER;
   CREATE DATABASE workshop3 OWNER <your_user>;
   
4. **Configure PostgreSQL for External Access (Optional for PowerBI)**  
   The PostgreSQL configuration files are generally located in `/etc/postgresql/{version}/main/`
   Edit the `postgresql.conf` file to allow external connections
   
   ```bash
   listen_addresses = '*'
   ssl = off
   
5. **Edit the pg_hba.conf File**  
   Allow connections from your local IP by adding the following line:
   ```plaintext
   host    all             all             <your-ip>/32         md5

6. **Set Up pgAdmin 4 (Optional)**  
   To install pgAdmin 4, run the following commands:
   ```bash
   sudo apt install curl
   sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
   sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
   sudo apt install pgadmin4

## Configuration of the .env file 📂✨

- **Create a .env File**  
   Create a `.env` file with the following configuration:
   ```plaintext
   PGDIALECT=postgresql
   PGUSER=<your_user>
   PGPASSWD=<your_password>
   PGHOST=localhost
   PGPORT=5432
   PGDB=workshop3
   WORK_DIR=<your_working_directory>

## Time to setup the project 🚀

1. **Clone the Repository**
   ```bash
   git clone https://github.com/caroldvarela/workshop-03.git
   cd workshop-03
   
2. **Create a Virtual Environment**  
   Create a Python virtual environment to manage dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. **Install Dependencies**  
   To install the project's dependencies:
   ```bash
   pip install -r requirements.txt

4. **Configure Kafka and Database**  
   Set up the Kafka service using Docker:
   ```bash
   docker compose up -d

5. **Access Kafka Container**  
   Open a terminal inside the Kafka container:
   ```bash
   docker exec -it kafka bash

6. **Create Kafka Topic**  
   Set up a new Kafka topic for the workshop:
   ```bash
   kafka-topics --bootstrap-server kafka:9092 --create --topic kafka_workshop3
   
7. **Run the Complete Pipeline**  
   Exit the Kafka console, and in the project folder execute the main pipeline:
   ```bash
   python main.py


