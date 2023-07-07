import oracledb

# Oracle DB connection details
db_username = 'SYS'
db_password = 'Admin1234'
db_host = 'localhost'
db_port = '1521'
db_service = 'orcl'

# Fetch and process data from the database
def insert_data():
        print('Connecting to Oracle database...')
        # Establish a connection to the Oracle database
        connection = oracledb.connect(
        user=db_username,
        password=db_password,
        dsn=f'{db_host}:{db_port}/{db_service}',
        mode=oracledb.SYSDBA
        )
        print("Successfully connected to Oracle Database")
        # Create a cursor
        cursor = connection.cursor()
        #query = "create table employeedetail(id number ,name varchar2(250))"
        #cursor.execute(query)
        # Open the Rawdata.dsv file
        with open('Rawdata.dsv', 'r') as file:
            print('Inserting data into the database...')
            # Read and process each line
            for line in file:
                data = line.strip().split(';')
                # Insert data into the database 
                query = f"insert into employeedetail values ('{data[1]}', '{data[0]}')"
                cursor.execute(query)
        connection.commit()
        print('Data inserted successfully')
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print('Connection to Oracle database closed')
# Usage example
insert_data()
