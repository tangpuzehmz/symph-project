#Where business logics reside.

from models import EmployeeModel,CompanyModel
import datetime
from google.appengine.ext import db
from google.appengine.api import users

class Employee(object):
	def save_employee (self,payperiod_from,payperiod_to,pay_date,full_name,basic_pay,allowance_1,allowance_2,allowance_3,allowance_4,allowance_calc,deduc_1,deduc_2,deduc_3,deduc_4,deduc_calc,additional_1,additional_2,additional_3,additional_4,additional_calc,net_pay,notes,id):
		#id will be greater than zero when EDIT action is triggered.
		if id>0:
			emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(id))
			emp = db.get(emp_k)
		else:
			comp = CompanyModel(key_name='Bellucci',name='Bellucci Enterprise')
			comp.put()
			emp = EmployeeModel(parent = comp)

		emp.payperiod_from = datetime.date(year=int(payperiod_from[6:10]), month=int(payperiod_from[3:5]), day=int(payperiod_from[0:2]))
		emp.payperiod_to = datetime.date(year=int(payperiod_to[6:10]), month=int(payperiod_to[3:5]), day=int(payperiod_to[0:2]))
		emp.pay_date = datetime.date(year=int(pay_date[6:10]), month=int(pay_date[3:5]), day=int(pay_date[0:2]))
		emp.full_name = full_name
		emp.basic_pay = basic_pay
		emp.allowance_1 = allowance_1
		emp.allowance_2 = allowance_2
		emp.allowance_3 = allowance_3
		emp.allowance_4 = allowance_4
		emp.allowance_calc = allowance_calc
		emp.deduc_1 = deduc_1
		emp.deduc_2 = deduc_2
		emp.deduc_3 = deduc_3
		emp.deduc_4 = deduc_4
		emp.deduc_calc = deduc_calc
		emp.additional_1 = additional_1
		emp.additional_2 = additional_2
		emp.additional_3 = additional_3
		emp.additional_4 = additional_4
		emp.additional_calc = additional_calc
		emp.net_pay = net_pay
		emp.notes = notes
		emp.user_name = users.get_current_user().email()
		emp.put()

	def delete_employee (self, employee_ids):
		if len(employee_ids)>0:
			for employee_id in employee_ids:
				emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(employee_id))
				emp = db.get(emp_k)
				db.delete(emp_k)

	def list_employee (self):
		comp = db.Key.from_path('CompanyModel','Bellucci')
		employee_query = EmployeeModel.all()
		employee_query.ancestor(comp)
		return employee_query



