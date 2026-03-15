import pandas as pd
import mysql.connector
import random

CSV_FILE = 'VRA_20257.csv'
TOTAL_RECORDS = 6000
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'duda2402',
    'database': 'vra_20257'
}

VRA_20257 = 'voos_6000'

def preparar_dados (csv_path, num_registros):

    try:
        df = pd.read_csv(csv_path, sep=";", encoding='latin1')
        df_aleatorio = df.sample(n=num_registros, random_state=42)
        return df_aleatorio
    except Exception as e:
        print (f"Erro ao ler o arquivo ou selecionar dados do CSV: {e}")
        return None
    
    def criar_tabela_e_inserir(df):

        try:
            conn = myqsql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            create_table_query = f"""
            crate table if not exists {VRA_202257} (
                id int auto_increment primary key,
                'codigo_empresa' varchar(10),
                'numero_voo' varchar(10),
                'DI' varchar(10),
                'linha' varchar(10),    
                'origem' varchar(50),
                'destino' varchar(50),
                'partida_prevista' varchar(10),
                'partida_real' varchar(10),
                'chegada_prevista' varchar(10),
                'chegada_real' varchar(10),
                'situacao' varchar(20
            );
            """
            cursor.execute(create_table_query)

            cools = ", ".join(df.columns)
            placeholders = ", ".join(["%"] * 12)
            insert_query = f"insert into {VRA_20257} ({cools}) values ({placeholders})"

            data_to_tuple = [tuple(row) for row in df.values()]

            cursor.executemany(insert_query, data_to_insert)
            conn.commit()
            print(f"Sucesso:{len(data_to_insert)}) registros inseridos com sucesso na tabela {VRA_20257}.")
        except Exception as e:
            print(f"Erro no MySQL {err}")
        finally:
            if conn and conn.is_connected():
                cursor.close()  
                conn.close()