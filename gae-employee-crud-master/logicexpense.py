from modelexpense import ExpenseModel,CompanyModel
import datetime
from google.appengine.ext import db
from google.appengine.api import users


class Expense(object):
	def save_expense (self,date_spent,description,supplier,amount,tax_type,payment_method,account,client_project,receipt_image,notes,id):

		if id>0:
			emp_k = db.Key.from_path('CompanyModel','Bellucci','ExpenseModel',long(id))
			emp = db.get(emp_k)
		else:
			comp = CompanyModel(key_name='Bellucci',name='Bellucci Enterprise')
			comp.put()
			emp = ExpenseModel(parent = comp)

			emp.date_spent = datetime.date(year=int(date_spent[6:10]), month=int(date_spent[3:5]), day=int(date_spent[0:2]))
			emp.description = description
			emp.supplier = supplier
			emp.amount = amount
			emp.tax_type = tax_type
			emp.payment_method = payment_method
			emp.account = account
			emp.client_project = client_project
			emp.receipt_image = receipt_image
			emp.notes = notes
			emp.user_name = users.get_current_user().email()
			emp.put()

	def delete_expense (self, employee_ids):
		if len(employee_ids)>0:
			for employee_id in employee_ids:
				emp_k = db.Key.from_path('CompanyModel','Bellucci','ExpenseModel',long(employee_id))
				emp = db.get(emp_k)
				db.delete(emp_k)

	def list_expense (self):
		comp = db.Key.from_path('CompanyModel','Bellucci')
		employee_query = ExpenseModel.all()
		employee_query.ancestor(comp)
		return employee_query