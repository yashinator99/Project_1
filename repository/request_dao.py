import psycopg2
from repository.connection import get_connection
from models.request_dto import Request


def insert_user_request(user_id, request_desc:str, request_amount:int):
    connection = get_connection()
    cursor = connection.cursor()

    qry = "INSERT INTO request_table VALUES (default, %s, %s, %s, %s) RETURNING request_id;"

    try:
        cursor.execute(qry,(user_id,request_desc,request_amount, "pending"))
        id = cursor.fetchone()[0]
        #while True:
        #    record = cursor.fetchone()
        #    if record is None:
        #        break
        connection.commit()
        return id
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def get_request(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT request_id, user_id, request_desc, request_amount, status FROM request_table WHERE user_id = {user_id};"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchall()
            if record is None:
                break
            #request_info = Request(record[0], record[1], record[2])
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

# New
def get_all_request():
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT request_id, user_id, request_desc, request_amount, status FROM request_table;"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchall()
            if record is None:
                break
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def get_status_request(status):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT request_id, user_id, request_desc, request_amount, status FROM request_table WHERE status = '{status}';"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchall()
            if record is None:
                break
            return record
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

def update_request(request_id, status):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"UPDATE request_table SET status='{status}' WHERE request_id = '{request_id}';"

    try:
        cursor.execute(qry)
        connection.commit()
        return
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()

def get_user_id_from_request_id(request_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"SELECT user_id FROM request_table WHERE request_id = {request_id};"

    try:
        cursor.execute(qry)

        while True:
            record = cursor.fetchone()
            if record is None:
                break
            #request_info = Request(record[0], record[1], record[2])
            return record[0]
    except(psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def delete_user_request(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    qry = f"DELETE FROM request_table WHERE user_id = '{user_id}';"

    try:
        cursor.execute(qry)
        connection.commit()
        return
    except(psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()
    finally:
        if connection is not None:
            connection.close()