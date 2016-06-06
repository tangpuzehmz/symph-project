from google.appengine.ext import db

class IncomeModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	income_date = db.DateProperty()
	income_type = db.StringProperty()
	account_name = db.StringProperty()
	reference_no = db.StringProperty()
	payment_method = db.StringProperty()
	payer = db.StringProperty()
	amount = db.StringProperty()
	notes = db.TextProperty()


class CompanyModel (db.Model):
	name = db.StringProperty()
