from sqlalchemy import text

def verify_mssql_connection(engine, logger):
    """
    Verify SQL Server connection by running a simple query.
    """
    try:
        logger.info("Verifying SQL Server connection...")
        with engine.connect() as conn:
            result = conn.execute(text("SELECT @@VERSION"))
            version = result.fetchone()[0]
            logger.info(f"Successfully connected to SQL Server: {version[:50]}...")
            return True
    except Exception as e:
        logger.error(f"Failed to connect to SQL Server: {e}")
        return False