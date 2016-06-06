from google.appengine.ext import db

class ExpenseModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	date_spent = db.DateProperty()
	description = db.TextProperty()
	supplier = db.StringProperty()
	amount = db.StringProperty()
	tax_type = db.StringProperty()
	payment_method = db.StringProperty()
	account = db.StringProperty()
	client_project = db.StringProperty()
	receipt_image = db.StringProperty()
	notes = db.TextProperty()


class CompanyModel (db.Model):
	name = db.StringProperty()