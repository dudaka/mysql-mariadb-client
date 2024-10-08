import mysql.connector
from mysql.connector import Error

def main():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',       # Hostname or IP address of the database server
            user='your_username',   # Your MySQL/MariaDB username
            password='your_password', # Your MySQL/MariaDB password
            database='your_database'  # Name of the database to connect to
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected to MySQL/MariaDB Server version {db_info}")
            cursor = connection.cursor()

            # Example DDL query: Creating a table
            ddl_query = """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                position VARCHAR(100),
                salary DECIMAL(10, 2),
                hire_date DATE
            );
            """
            cursor.execute(ddl_query)
            print("Table 'employees' created successfully.")

            # Example DML query: Inserting data into the table
            dml_query = """
            INSERT INTO employees (name, position, salary, hire_date)
            VALUES (%s, %s, %s, %s);
            """
            data = [
                ('John Doe', 'Software Developer', 70000, '2024-01-15'),
                ('Jane Smith', 'Project Manager', 85000, '2023-10-10'),
                ('Sam Wilson', 'Designer', 50000, '2022-05-30')
            ]
            cursor.executemany(dml_query, data)
            connection.commit()  # Commit the transaction
            print("Data inserted successfully.")

            # Example DML query: Fetching data
            select_query = "SELECT * FROM employees;"
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

    except Error as e:
        print(f"Error while connecting to MySQL/MariaDB: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL/MariaDB connection is closed")


if __name__ == '__main__':
    main()