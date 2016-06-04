#Data Model module 
#It's similar to table schema in SQL
#
from google.appengine.ext import db

class EmployeeModel (db.Model):
	timestamp = db.DateTimeProperty(auto_now=True)
	payperiod_from = db.DateProperty()
	payperiod_to = db.DateProperty()
	pay_date = db.DateProperty()
	full_name = db.StringProperty()
	
	basic_pay = db.StringProperty()
	allowance_1 = db.StringProperty()
	allowance_2 = db.StringProperty()
	allowance_3 = db.StringProperty()
	allowance_4 = db.StringProperty()
	allowance_calc = db.StringProperty()
	deduc_1 = db.StringProperty()
	deduc_2 = db.StringProperty()
	deduc_3 = db.StringProperty()
	deduc_4 = db.StringProperty()
	deduc_calc = db.StringProperty()
	additional_1 = db.StringProperty()
	additional_2 = db.StringProperty()
	additional_3 = db.StringProperty()
	additional_4 = db.StringProperty()
	additional_calc = db.StringProperty()
	net_pay = db.StringProperty()
	notes = db.TextProperty()


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