# oracledatabaseconnection
connect python code to oracle db hosted locally and insert/fetch from the database
The code in python takes a input to code as .dsv file and reads data from the file.
It then inserts the data into database using insert.py script
it also fetch the data pushed to database and stored it to output.tsv file in local as well.
it uses module oracledb of python.
the oracledatabase was setup locally to connect with both the script
To run the script at particular time 
We cron on machine: This helps in timed scheduling of the scripts
