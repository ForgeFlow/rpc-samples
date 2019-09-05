import odoorpc


def main():
    server_url = input("Server URL: ")
    server_port = input("Server Port: ")
    db_name = input("DB name: ")
    username = input("User name: ")
    pwd = input("Password: ")
    # Instance OdooRPC class
    odoo = odoorpc.ODOO(server_url, port=server_port)
    odoo.config['timeout'] = 100000
    # Login
    odoo.login(db_name, username, pwd)
    # Get a recordset
    cert_model = odoo.env['certification']
    cert_ids = cert_model.search([])
    cert_recordset = cert_model.browse(cert_ids)
    print(cert_recordset)


if __name__ == "__main__":
    main()
