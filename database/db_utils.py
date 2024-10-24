"""
This module provides functionality to build a SQLAlchemy engine for connecting
to a PostgreSQL database using configuration values from environment variables.

It defines the following function:
- build_engine: Creates and returns a SQLAlchemy engine for the database.

Usage:
    This module is used to establish a connection to a PostgreSQL database by creating an engine
    with SQLAlchemy. The `build_engine` function retrieves connection details from environment variables
    and handles potential errors during the connection process.
    
"""
from dotenv import load_dotenv
import sys 
import os
from decouple import config, UndefinedValueError
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from database.model import CountryData

load_dotenv()
work_dir = os.getenv('WORK_DIR')

sys.path.append(work_dir)

def build_engine():
    """
    Creates a SQLAlchemy engine for connecting to the PostgreSQL database using
    configuration values from environment variables.

    Returns:
        sqlalchemy.engine.base.Engine: The SQLAlchemy engine connected to the database.

    Raises:
        UndefinedValueError: If any required environment variable is missing.
        SQLAlchemyError: If there is an error connecting to the database.
    """
    try:
        dialect = config('PGDIALECT')
        user = config('PGUSER')
        passwd = config('PGPASSWD')
        host = config('PGHOST')
        port = config('PGPORT')
        db = config('PGDB')
    except UndefinedValueError as e:
        print(f"Missing environment variable: {e}")
        raise

    database_url = (f"{dialect}://{user}:{passwd}@{host}:{port}/{db}")

    # Test the connection
    try:
        engine = create_engine(database_url)
        print(f"Successfully connected to the database {db}!")
        return engine
    except SQLAlchemyError as e:
        print(f"Failed to connect to the database: {e}")


def load_data(df):
    engine = build_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        inspector = inspect(engine)

        # Verificar si la tabla 'country_data' ya existe
        if not inspector.has_table('country_data'):
            try:
                CountryData.__table__.create(engine)
                print("Table 'country_data' creation was successful.")
            except SQLAlchemyError as e:
                print(f"Error creating table: {e}")
                raise

        # Cargar datos en la tabla
        with engine.connect() as connection:
            df.drop_duplicates(subset='id', inplace=True)
            df.to_sql('country_data', connection, if_exists='append', index=False)
            print("Data loaded successfully into 'country_data'.")
        return df

    except SQLAlchemyError as error:
        print(f"An error occurred: {error}")
        return None

    finally:
        if session:
            session.close()