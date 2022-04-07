import logging

import azure.functions as func

import pyodbc

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    server = "aaazure1.database.windows.net"
    database = "ProdRepository"
    driver = "{ODBC Driver 17 for SQL Server}"
    query = "SELECT * FROM dbo.AALEList WHERE ID=129"

    connection_string = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database
    conn = pyodbc.connect(connection_string + ';Authentication=ActiveDirectoryMsi')

    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    id = row[0]
    name = row[1]

    return func.HttpResponse(
            f'Data:\n----------------------------------------------\nID: {id}, AALEName: {name}',
            status_code=200
    )