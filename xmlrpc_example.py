from xmlrpc import client

# Credential Variables required
server_url = 'http://localhost:8069' # Odoo instance IP
db_name = '12.0-odoo-training-tai-2'
username = 'admin'
password = 'admin'

# No authenticate required
common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
# Check Odoo Version
version = common.version()
print(version)
# Check user connection to database. Return user's ID
user_id = common.authenticate(db_name, username, password, {})
print(user_id)

models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)
if user_id:
    search_domain = [('is_certification_body', '=', True)]
    entity_partners = models.execute_kw(db_name, user_id, password,
                                        'res.partner', 'search_read',
                                        [search_domain, ['name', 'entity']],{})
    print(entity_partners)

    create_data = [{'number': 'XMLRPC Certificate'}, {'number': 'XMLRPC 2 Certificate'}]
    created_data = models.execute_kw(db_name, user_id, password, 'certification', 'create', [create_data])
    print(created_data)
    from datetime import date
    DATE_FORMAT = "%Y-%m-%d"
    update_date = {'date': date.today().strftime(DATE_FORMAT)}
    models.execute_kw(db_name, user_id, password, 'certification', 'write', [created_data, update_date])
    models.execute_kw(db_name, user_id, password, 'certification', 'unlink', [created_data])