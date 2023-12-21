# from dagster import op
import pandas as pd
import os
from sqlalchemy import create_engine


def get_db_config(self):
        conn_info = (
            f"mysql+pymysql://{self.params['admin']}:{self.params['admin123']}"
            + f"@{self.params['localhost']}:{self.params['3306']}"
            + f"/{self.params['tiki_ecommerce']}"
        )

        print(f"Config: {conn_info}")
        db_conn = create_engine(conn_info)
        return db_conn


folder_path = "./data"

print(get_db_config(self))