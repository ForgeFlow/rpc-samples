import odoorpc


def main():
    server_url = input("Server URL: ")
    server_port = input("Server Port: ")
    db_name = input("DB name: ")
    username = input("User name: ")
    pwd = input("Password: ")
    card_code = input("Card code: ")
    # Instance OdooRPC class
    odoo = odoorpc.ODOO(server_url, port=server_port)
    odoo.config['timeout'] = 100000
    # Login
    odoo.login(db_name, username, pwd)
    # Call attendance
    call_attendance = odoo.env['hr.employee'].register_attendance(card_code)
    print(call_attendance)


if __name__ == "__main__":
    main()
