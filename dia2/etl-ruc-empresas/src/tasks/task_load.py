import mysql.connector
from config import Config
from prefect import task

config = Config()

conn = mysql.connector.connect(
            user=config.mysql_user,
            password=config.mysql_password,
            host=config.mysql_host,
            database=config.mysql_database
        )


@task(name='carga de info en bd')
def task_load_empresas(empresas):
    try:
        cursor = conn.cursor()

        query_drop = "drop table if exists tbl_empresa"
        cursor.execute(query_drop)
        conn.commit()

        query_table = """
        create table if not exists tbl_empresa(
        id INT AUTO_INCREMENT PRIMARY KEY,
        ruc VARCHAR(20),
        razon_social VARCHAR(255),
        direccion VARCHAR(255),
        venta_anual VARCHAR(20))
        """
        cursor.execute(query_table)
        conn.commit()

        query_insert = """
        insert into tbl_empresa(ruc,razon_social,direccion,venta_anual)
        values(%s,%s,%s,%s)
        """

        for empresa in empresas:
            cursor.execute(query_insert,empresa)

        conn.commit()
        cursor.close()
        conn.close()
        print('datos guardados en bd...')

    except mysql.connector.Error as err:
        print(err)