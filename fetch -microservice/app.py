import oracledb

# Oracle DB connection details
db_username = 'SYS'
db_password = 'Admin1234'
db_host = 'localhost'
db_port = '1521'
db_service = 'orcl'

# Fetch and process data from the database
def fetch_data():
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
        # Fetch the data from the database
        query = "SELECT * FROM employeedetail"
        cursor.execute(query)        
# Fetch and store the result in a TSV file
        output_file = 'output.tsv'
        with open(output_file, 'w') as file:
            # Write the header row with column names
            columns = [desc[0] for desc in cursor.description]
            file.write('\t'.join(columns) + '\n')

            # Write each row of data
            result = cursor.fetchall()
            for row in result:
                file.write('\t'.join(map(str, row)) + '\n')

        print(f"Data saved to {output_file}")

# Usage example
fetch_data()
