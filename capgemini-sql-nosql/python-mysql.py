import mysql.connector
def connect_db():
    try:
        connection=mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='department'
        )
        print('Mysql connected Succesfully')
        return connection
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
def create_table(connection):
    cursor=connection.cursor()
    try:
        query="""CREATE TABLE EMPLOYEE (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary INT);"""
        cursor.execute(query)
        print('Table created Succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def inserting_data(connection):
    cursor=connection.cursor()
    try:
        query="""INSERT INTO EMPLOYEE(name,age,salary) VALUES(%s,%s,%s)"""
        data=[
            ("shanmuk",19,5000),
            ("sandeep",20,6000),
            ("satwik",30,7000)
        ]
        cursor.executemany(query,data)
        connection.commit()
        print('Data Inserted Succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def updating_data(connection):
    cursor=connection.cursor()
    try:
        query="""UPDATE EMPLOYEE SET SALARY=7000 WHERE name="%s";"""
        cursor.execute(query,("shanmuk",))
        connection.commit()
        print('Updated the data succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def deleting_data(connection):
    cursor=connection.cursor()
    try:
        query="""DELETE FROM EMPLOYEE WHERE ID=1;"""
        cursor.execute(query)
        connection.commit()
        print('Data deleted succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def sort_data(connection):
    cursor = connection.cursor()
    try:
        query = """SELECT * FROM EMPLOYEE ORDER BY SALARY DESC;"""
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f'Something went wrong:{err}')
    finally:
        cursor.close()
def query_with_filter(connection):
    cursor=connection.cursor()
    try:
        query="""SELECT * FROM EMPLOYEE WHERE SALARY>%s;"""
        cursor.execute(query,(5000,))
        result=cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print(f'Something went wrong:{err}')
    finally:
        cursor.close()
def drop_table(connection):
    cursor=connection.cursor()
    try:
        query="""DROP TABLE EMPLOYEE;"""
        cursor.execute(query)
        connection.commit()
        print('Table dropped succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def drop_database(connection):
    cursor = connection.cursor()
    try:
        query = """DROP DATABASE department;"""
        cursor.execute(query)
        connection.commit()
        print('Database dropped succesfully')
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        cursor.close()
def main():
    connection=connect_db()
    if not connection:
        return None
    create_table(connection)
    inserting_data(connection)
    # updating_data(connection)
    # deleting_data(connection)
    # sort_data(connection)
    # query_with_filter(connection)
    # drop_table(connection)
    # drop_database(connection)
    connection.close()
    print('Mysql connection closed')
main()