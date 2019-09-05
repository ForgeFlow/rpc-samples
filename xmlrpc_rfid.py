from xmlrpc import client

card_code = input("Enter Card Code:")
# Credential Variables required
server_url = 'http://localhost:8069' # Odoo instance IP
db_name = '12.0-odoo-training-tai-2'
username = 'admin'
password = 'admin'

# No authenticate required
common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
# Check user connection to database. Return user's ID
user_id = common.authenticate(db_name, username, password, {})
models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)

if user_id:
    # Register Attendance
    call_attendance = models.execute_kw(db_name, user_id, password,
                                        'hr.employee', 'register_attendance',
                                        [card_code])
    print(call_attendance)
