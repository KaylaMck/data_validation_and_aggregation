import boto3
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import my_logger as ml
import process_files as pf

MINIO_URL = "http://minio:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"

# PostgreSQL credentials
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "de"

# Microsoft SQL Server credentials
MSSQL_USER = "devadmin"
MSSQL_PASSWORD = "Bootcamp1433!"
MSSQL_HOST = "de-nss-bootcamp.database.windows.net"
MSSQL_PORT = "1433"
MSSQL_DB = "de_bootcamp"


def get_db_engine():
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    return engine


def get_mssql_engine():
    # URL-encode the password to handle special characters like !
    password_encoded = quote_plus(MSSQL_PASSWORD)
    
    engine = create_engine(
        f"mssql+pyodbc://{MSSQL_USER}:{password_encoded}@{MSSQL_HOST}:{MSSQL_PORT}/{MSSQL_DB}"
        f"?driver=SQL+Server"  # Changed from "ODBC Driver 17" to "SQL Server"
    )
    return engine


def get_s3_client():
    s3_client = boto3.client(
        "s3",
        endpoint_url=MINIO_URL,
        aws_access_key_id=MINIO_ACCESS_KEY,
        aws_secret_access_key=MINIO_SECRET_KEY,
    )
    return s3_client


def main(logger):
    logger.info("setting up database engines and s3 client")
    pg_engine = get_db_engine()
    mssql_engine = get_mssql_engine()
    s3 = get_s3_client()
    
    logger.info("all connections established successfully")

    if not pf.verify_mssql_connection(mssql_engine, logger):
        logger.error("Exiting due to MSSQL connection failure.")
        return
    
    logger.info("SQL Server connection verified successfully.")
    

if __name__ == "__main__":
    logger = ml.get_my_logger()
    main(logger)