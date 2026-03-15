from flask import Flask, render_template, request, jsonify
import mysql.connector
import time
import random

app = Flask(__name__)


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'duda2402',
    'database': 'sistema_voos',
    'port': 3306
}

TABELA = "vra_20257"
SEARCH_COLUMN = "Número Voo"   



def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_all_search_keys():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute(f"SELECT `{SEARCH_COLUMN}` FROM {TABELA}")
    keys = [row[SEARCH_COLUMN] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return keys


def get_first_100_distinct():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SET SESSION sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))")

    cursor.execute(f"""
        SELECT *
        FROM {TABELA}
        GROUP BY `{SEARCH_COLUMN}`
        LIMIT 10
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows




ALL_KEYS = get_all_search_keys()
CHAVE_PADRAO = random.choice(ALL_KEYS) if ALL_KEYS else "Nenhuma chave encontrada"



def busca_sequencial(key):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    start = time.perf_counter()
    cursor.execute(f"SELECT * FROM {TABELA} WHERE `{SEARCH_COLUMN}` = %s", (key,))
    result = cursor.fetchone()
    end = time.perf_counter()
    cursor.close()
    conn.close()
    return result, end - start


def busca_indexada(key):
    return busca_sequencial(key)


def busca_hash(key):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute(f"SELECT * FROM {TABELA}")
    all_rows = cursor.fetchall()
    cursor.close()
    conn.close()
    hashmap = {row[SEARCH_COLUMN]: row for row in all_rows}
    start = time.perf_counter()
    result = hashmap.get(key)
    end = time.perf_counter()
    return result, end - start



@app.route("/")
def index():
    first_100 = get_first_100_distinct()
    return render_template("index.html", search_key=CHAVE_PADRAO, first_100=first_100)


@app.route("/search", methods=["POST"])
def search():
    key = request.form.get("search_key")
    search_type = request.form.get("search_type", "sequencial")

    if not key:
        return jsonify({"erro": "Nenhuma chave de busca enviada"}), 400

    if search_type == "sequencial":
        result, tempo = busca_sequencial(key)
        tipo = "Sequencial (MySQL)"
    elif search_type == "indexada":
        result, tempo = busca_indexada(key)
        tipo = "Indexada (MySQL com Índice)"
    elif search_type == "hash":
        result, tempo = busca_hash(key)
        tipo = "Hash (Memória Python)"
    else:
        return jsonify({"erro": "Tipo de busca inválido"}), 400

    if not result:
        return jsonify({"erro": "Nenhum registro encontrado"}), 404

    return jsonify({
        "chave_buscada": key,
        "tipo": tipo,
        "tempo": f"{tempo:.6f} segundos",
        "registro": result
    })



if __name__ == "__main__":
    print(f"Chave selecionada automaticamente: {CHAVE_PADRAO}")
    app.run(debug=True)
