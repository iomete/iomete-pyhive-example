import os

from connection import ConnectionArgs, create_connection

connection_args = ConnectionArgs(
    account_id="111111111111",  # replace with your account id.
    cluster="reporting",  # your lakehouse cluster name. find the name from iomete console
    user="user1",  # replace with the actual user name
    password=os.environ.get('IOMETE_PASSWORD'),
    database="default",
)


# example1. how to query data and iterate over result set
def query_data():
    with create_connection(connection_args) as conn, conn.cursor() as cursor:
        cursor.execute("SELECT * FROM test_table LIMIT 10")
        result = cursor.fetchall()
        for row in result:
            print(row)


# example 2. get single result value
def query_single_value():
    with create_connection(connection_args) as conn, conn.cursor() as cursor:
        cursor.execute("SELECT count(1) FROM test_table")
        result = cursor.fetchone()
        if result:
            print(result[0])
        else:
            print(None)


# example 3. run any statement
def execute_statement():
    with create_connection(connection_args) as conn, conn.cursor() as cursor:
        cursor.execute("""
            CREATE OR REPLACE TABLE employees 
                AS SELECT  * FROM employees_proxy
            """)


if __name__ == '__main__':
    query_data()
    # query_single_value()
    # execute_statement()
