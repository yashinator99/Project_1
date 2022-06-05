import psycopg2

#To define a function and  return it to the database connection

def get_connection():
    connection = psycopg2.connect(
            database="project1",
            user="postgres",
            password="password1234!",
            host="project-1.ch0i3nfkajfb.us-east-1.rds.amazonaws.com",
            port="5432"
    )

    return connection