import psycopg2
from psycopg2 import sql
from rest_framework.response import Response

def check_error(e):
    if e.pgcode is None:
        e = Response({"error": "Error interno de servidor BD"}, status=500)
    else:
        e = Response({"error" : "La tabla ingresada no existe"}, status=400)

    return e

def get_record_count(dbname, user, password, host, port, table_name):

    if not isinstance(table_name, str):
        error_msg = "Es necesario ingresar la variable table_name"
        return Response({"error" : error_msg}, status=400)

    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        query = sql.SQL("SELECT COUNT(*) FROM {}").format(sql.Identifier(table_name))
        cur.execute(query)
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return Response({"total de registros": count}, status=200)

    except psycopg2.Error as e:
        print(e.pgcode)
        e = check_error(e)
        return e