import oracledb
from utils.config import *

# Initialize Oracle Client (ONLY once)
oracledb.init_oracle_client(lib_dir=INSTANT_CLIENT_PATH)

def get_connection():
    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )
    return connection