# A Java program with MySQL/MariaDB connector


## Step 1: Download the MySQL Connector Jar

1. Go to [MySQL Connector/J Download Page](https://dev.mysql.com/downloads/connector/j/).
2. Select `Platform Independent`
3. Download the compressed file you want. Recommend Zip Archive
4. Uncompress the file, you will file a file named `mysql-connector-java-x.x.xx.jar`. `x.x.xx` depends on the version you download at the time.

I have a file `mysql-connector-j-9.0.0.jar` in the same directory and will use it to demontrate for the next steps.
You can use this one in your project.

## Step 2: An example program

I have a sample program named `Client.java` which shows how to import the libary and how to use it for your queries. 
Please refer to it when working on your project program.

### For your local MySQL/MariaDB server.

I believe your server is running locally in your own PC/laptop and your program too.
And let's say your database name is `your_database`. So, the value of the property `URL` is `jdbc:mysql://localhost:3306/your_database`
Just update it in the code with the format.

### For MNSU's MariaDB server

1. You need to connect to NMSU Network through [NMSU VPN](https://agit.nmsu.edu/services/vpn.html) if your PC/laptop is not connecting to the network.
2. Then, you should update these properties by replacing `your_database`, `your_username` and `your_password`.

```java
private static final String URL = "jdbc:mysql://dbclass.cs.nmsu.edu:3306/your_database";
private static final String USER = "your_username";
private static final String PASSWORD = "your_password";
```

## Step 3: Compile the Java Program

Open your terminal and navigate to the directory storing the source file. 
Here, the source file `Client.java` and `mysql-connector-j-9.0.0.jar` are the same directory.

On Mac/Linux

```
javac -cp .:mysql-connector-j-9.0.0.jar Client.java
```

On Windows

```
javac -cp .;mysql-connector-j-9.0.0.jar Client.java
```

This will generate a `Client.class` file in the same directory.

## Step 4: Run the Java Program

On Mac/Linux

```
java -cp .:mysql-connector-j-9.0.0.jar Client.java
```

On Windows

```
java -cp .;mysql-connector-j-9.0.0.jar Client.java
```

## Troubleshooting

1. When executing the command in Step 4 in Windows, you may got this error 

```
Error: Could not find or load main class Client
Caused by: java.lang.ClassNotFoundException: client
```

You can try the command without `.java` extension

```
java -cp .;mysql-connector-j-9.0.0.jar Client
```