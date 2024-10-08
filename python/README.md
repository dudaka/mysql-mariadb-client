# A Python program with MySQL/MariaDB connector


## Step 1: Install the MySQL Connector

If you haven't already installed the library, use the following command:

```
pip install mysql-connector-python
```

## Step 2: An example program

I have a sample program named `client.py` which shows how to import the libary and how to use it for your queries. 
Please refer to it when working on your project program.

### For your local MySQL/MariaDB server.

I believe your server is running locally in your own PC/laptop and your program too.
Please update the following code by by replacing `your_database`, `your_username` and `your_password`.

```python
# Establish the connection
        connection = mysql.connector.connect(
            host='localhost',       # Hostname or IP address of the database server
            user='your_username',   # Your MySQL/MariaDB username
            password='your_password', # Your MySQL/MariaDB password
            database='your_database'  # Name of the database to connect to
        )
```

### For MNSU's MariaDB server

1. You need to connect to NMSU Network through [NMSU VPN](https://agit.nmsu.edu/services/vpn.html) if your PC/laptop is not connecting to the network.
2. Then, you should update these properties by replacing `your_database`, `your_username` and `your_password`.

```python
# Establish the connection
        connection = mysql.connector.connect(
            host='dbclass.cs.nmsu.edu',       # Hostname or IP address of the database server
            user='your_username',   # Your MySQL/MariaDB username
            password='your_password', # Your MySQL/MariaDB password
            database='your_database'  # Name of the database to connect to
        )
```


## Step 3: Run the Java Program

```sh
python client.py
```

