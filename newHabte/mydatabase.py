import pandas as pd
from sqlalchemy import create_engine, text

# Load CSV data into a pandas DataFrame
csv_file_path = '/home/habte/Downloads/Data-20240102T114055Z-001/Data/youtube-data/Viewership by Date/Table data.csv'
df = pd.read_csv(csv_file_path)

# Connect to PostgreSQL database using SQLAlchemy
db_params = {
    'dbname': 'mydatabase',
    'user': 'postgres',
    'password': 'habte',
    'host': 'localhost',
    'port': '5432'
}
engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

# Define a function to create a table in the database based on DataFrame columns
def create_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS viewership (
        date DATE,
        views INTEGER,
        watch_time_hours FLOAT,
        average_view_duration FLOAT
    );
    '''
    with engine.connect() as connection:
        connection.execute(text(create_table_query))

# Create the table in the database
create_table()

# Insert data from the DataFrame into the database table
df.to_sql('viewership', engine, if_exists='replace', index=False)

# Example: Query data from the database
query = 'SELECT * FROM viewership LIMIT 5;'
result = pd.read_sql(query, engine)
print(result)
