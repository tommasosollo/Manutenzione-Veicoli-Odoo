import xmlrpc.client


url = 'http://127.0.0.1:8069'
db = "odoo17_dev"
user_name = "tommaso.sollo06@gmail.com"
password = "password"


common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

uid = common.authenticate(db, user_name, password, {})

if uid:
    print("authentication success")
else:
    print("authentication failed")


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partners = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', "=", True]]])

print(partners)