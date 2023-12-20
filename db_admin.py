# Only Admin can do this

import pandas as pd
from db_conn import connection

def load_table(TName :str):
    with connection.cursor() as cur:
        cur.execute(f'''  SELECT * FROM {TName} '''  )
        
        col_names = [desc[0] for desc in cur.description]
        
        result = cur.fetchall()
        df = pd.DataFrame(result ,columns = col_names)
        
    return df



table_list = []

with connection.cursor() as cur:
    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public'
    """)
    table_names = cur.fetchall()
    for char in table_names:
        table_list.append(char[0])






df_dict = {}
for table_name in table_list:
    df_dict[f"{table_name}_df"] = load_table(table_name)   
