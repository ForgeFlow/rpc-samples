import psycopg2

db_name = '12.0-odoo-training-tai-2' # Select your database name
db_username = 'odoo' # Change for your DB username
db_pwd = 'odoo' # Change for your DB password


def connect_to_database():
    # Define our connection string
    conn_string = """dbname=%s user=%s
        password=%s""" % (db_name, db_username, db_pwd)

    # print the connection string we will use to connect
    print("Connecting to database\n    ->%s", conn_string)

    # get a connection, if a connect cannot be made an exception
    # will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor
    # to perform queries
    cr = conn.cursor()
    print("Connected!\n")
    return conn, cr


def main():
    conn, cr = connect_to_database()
    cr.execute("""
        SELECT id FROM res_partner WHERE is_certification_body = True
    """)
    results = cr.fetchall()
    for result in results:
        import random
        if random.choice([False, True]):
            cr.execute("""
                UPDATE res_partner SET is_certification_body = False WHERE id = %s
            """ % result[0])

    # conn.commit() # Uncomment to save changes into DB


if __name__ == "__main__":
    main()
