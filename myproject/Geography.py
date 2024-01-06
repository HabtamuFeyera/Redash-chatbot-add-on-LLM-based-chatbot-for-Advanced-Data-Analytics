import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Database connection parameters
db_params = {
    'dbname': 'Geography',
    'user': 'postgres',
    'password': 'habte05',
    'host': 'localhost',
    'port': '5432'
}

# CSV file path
csv_file_path = '/home/habte/Geography/Table data.csv'

# Read CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Establish a connection to the PostgreSQL database
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

# Insert data into PostgreSQL database
df.to_sql('Viewer gender', engine, index=False, if_exists='replace')

# Close the database connection
engine.dispose()
