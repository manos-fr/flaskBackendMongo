import psycopg2
from psycopg2 import Error


def db():
    try:
        connection = psycopg2.connect(user="postgres", password="12345",
                                      host="127.0.0.1", port="5432", database="Movies")

        cursor = connection.cursor()

        cursor.execute("SELECT version();")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()


if __name__ == '__main__':
    db()
