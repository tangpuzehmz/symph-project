from modelincome import IncomeModel,CompanyModel
import datetime
from google.appengine.ext import db
from google.appengine.api import users


class Income(object):
	def save_income (self,income_date,income_type,account_name,reference_no,payment_method,payer,amount,notes,id):

		if id>0:
			emp_k = db.Key.from_path('CompanyModel','Bellucci','IncomeModel',long(id))
			emp = db.get(emp_k)
		else:
			comp = CompanyModel(key_name='Bellucci',name='Bellucci Enterprise')
			comp.put()
			emp = IncomeModel(parent = comp)

			emp.income_date = datetime.date(year=int(income_date[6:10]), month=int(income_date[3:5]), day=int(income_date[0:2]))
			emp.income_type = income_type
			emp.account_name = account_name
			emp.reference_no = reference_no
			emp.payment_method = payment_method
			emp.payer = payer
			emp.amount = amount
			emp.notes = notes
			emp.user_name = users.get_current_user().email()
			emp.put()

	def delete_income (self, employee_ids):
		if len(employee_ids)>0:
			for employee_id in employee_ids:
				emp_k = db.Key.from_path('CompanyModel','Bellucci','IncomeModel',long(employee_id))
				emp = db.get(emp_k)
				db.delete(emp_k)

	def list_income (self):
		comp = db.Key.from_path('CompanyModel','Bellucci')
		employee_query = IncomeModel.all()
		employee_query.ancestor(comp)
		return employee_query