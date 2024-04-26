import mysql.connector
from mysql.connector import Error
from config import db_config 

def create_connection_mysql_db(db_host, user_name, user_password, db_name = None):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host = db_host,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Подключение к MySQL успешно выполнено")
    except Error as db_connection_error:
        print("Возникла ошибка: ", db_connection_error)
    return connection_db


conn = create_connection_mysql_db(db_config["mysql"]["host"], 
                                  db_config["mysql"]["user"], 
                                  db_config["mysql"]["pass"])
#cursor = conn.cursor()
#create_db_sql_query = 'CREATE DATABASE {}'.format('Test')
#cursor.execute(create_db_sql_query)
#cursor.close()
#conn.close()

conn = create_connection_mysql_db(db_config["mysql"]["host"], 
                                  db_config["mysql"]["user"], 
                                  db_config["mysql"]["pass"],
                                  "Test")
try:

    # создание таблицы
    cursor = conn.cursor()
    #create_table_query = '''
    #CREATE TABLE IF NOT EXISTS drons1 (
    #id INT AUTO_INCREMENT, 
    #name TEXT NOT NULL, 
    #year_of_issue INT,  
    #information TEXT,
    #PRIMARY KEY (id)
    #) ENGINE = InnoDB'''
    #cursor.execute(create_table_query)
    #conn.commit()

    # вставка данных в таблицу
    insert_drons1_table_query = '''
    INSERT INTO
    drons1 (name, year_of_issue, information)     
    VALUES
    ('беспилотник 1', 2019, '...'),
    ('беспилотник 2', 2022, '...'),
    ('беспилотник 3', 2022, '...'),
    ('беспилотник 4', 2023, '...');'''
    cursor.execute(insert_drons1_table_query)
    conn.commit()
    
    # редактирование записей
    update_drons1_query = '''
    UPDATE drons1 SET name = 'беспилотник 1' WHERE name = 'беспилотник 5';
    '''
    cursor.execute(update_drons1_query)
    conn.commit()

    # удаление записей 
    delete_drons1_query = '''
    DELETE FROM drons1 WHERE year_of_issue = 2023;
    '''
    cursor.execute(delete_drons1_query)
    conn.commit()

    # извлечение данных из бд
    select_drons1_query = '''
    SELECT name, year_of_issue, information FROM drons1 WHERE year_of_issue = '2022';
    '''
    cursor.execute(select_drons1_query)
    query_result = cursor.fetchall()
    for dron in query_result:
        print(dron)

except Error as error:
    print(error)
finally:
    cursor.close()
    conn.close()                                 
