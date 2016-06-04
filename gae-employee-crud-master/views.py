#Collection of handlers which is to process route request from main.py

import webapp2
import cgi
import jinja2
import os

from datetime import datetime
from logics import Employee
from logic import Expense

from google.appengine.ext import db
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

jinja_environment.globals['year'] = datetime.now().year

class MainHandler(webapp2.RequestHandler):
    def get(self):
        emp = Employee() 
        template_values = {'employees' : emp.list_employee()}
        template = jinja_environment.get_template('template/index.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'): #if user clicks "Delete" button
                employee_ids = self.request.get('employee_id',allow_multiple=True) #allow_multiple=True so that it reads multiple key into list.
                emp = Employee()
                emp.delete_employee(employee_ids)
                self.redirect('/')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class CreateHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_payperiod_from = self.request.get('payperiod_from').strip()
        input_payperiod_to = self.request.get('payperiod_to').strip()
        input_pay_date = self.request.get('pay_date').strip()
        input_full_name = self.request.get('full_name').strip()
        input_basic_pay = self.request.get('basic_pay').strip()
        input_allowance_1 = self.request.get('allowance_1').strip()
        input_allowance_2 = self.request.get('allowance_2').strip()
        input_allowance_3 = self.request.get('allowance_3').strip()
        input_allowance_4 = self.request.get('allowance_4').strip()
        input_allowance_calc = self.request.get('allowance_calc').strip()
        input_deduc_1 = self.request.get('deduc_1').strip()
        input_deduc_2 = self.request.get('deduc_2').strip()
        input_deduc_3 = self.request.get('deduc_3').strip()
        input_deduc_4 = self.request.get('deduc_4').strip()
        input_deduc_calc = self.request.get('deduc_calc').strip()
        input_additional_1 = self.request.get('additional_1').strip()
        input_additional_2 = self.request.get('additional_2').strip()
        input_additional_3 = self.request.get('additional_3').strip()
        input_additional_4 = self.request.get('additional_4').strip()
        input_additional_calc = self.request.get('additional_calc').strip()
        input_net_pay = self.request.get('net_pay').strip()
        input_notes = self.request.get('notes').strip()
        
        emp = Employee()
        emp.save_employee(input_payperiod_from,input_payperiod_to,input_pay_date,input_full_name,input_basic_pay,input_allowance_1,input_allowance_2,input_allowance_3,input_allowance_4,input_allowance_calc,input_deduc_1,input_deduc_2,input_deduc_3,input_deduc_4,input_deduc_calc,input_additional_1,input_additional_2,input_additional_3,input_additional_4,input_additional_calc,input_net_pay,input_notes,0)
        self.redirect('/create')


class EditHandler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            #get ID of entity Key
            emp_k = db.Key.from_path('CompanyModel','Bellucci','EmployeeModel',long(self.request.get('id')))
            #get entity from key instance
            emp = db.get(emp_k)
            
            template_values = {'employee' : emp}
            template = jinja_environment.get_template('template/edit.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_id = self.request.get('id')
        input_payperiod_from = self.request.get('payperiod_from').strip()
        input_payperiod_to = self.request.get('payperiod_to').strip()
        input_pay_date = self.request.get('pay_date').strip()
        input_full_name = self.request.get('full_name').strip()
        input_basic_pay = self.request.get('basic_pay').strip()
        input_allowance_1 = self.request.get('allowance_1').strip()
        input_allowance_2 = self.request.get('allowance_2').strip()
        input_allowance_3 = self.request.get('allowance_3').strip()
        input_allowance_4 = self.request.get('allowance_4').strip()
        input_allowance_calc = self.request.get('allowance_calc').strip()
        input_deduc_1 = self.request.get('deduc_1').strip()
        input_deduc_2 = self.request.get('deduc_2').strip()
        input_deduc_3 = self.request.get('deduc_3').strip()
        input_deduc_4 = self.request.get('deduc_4').strip()
        input_deduc_calc = self.request.get('deduc_calc').strip()
        input_additional_1 = self.request.get('additional_1').strip()
        input_additional_2 = self.request.get('additional_2').strip()
        input_additional_3 = self.request.get('additional_3').strip()
        input_additional_4 = self.request.get('additional_4').strip()
        input_additional_calc = self.request.get('additional_calc').strip()
        input_net_pay = self.request.get('net_pay').strip()
        input_notes = self.request.get('notes').strip()

        emp = Employee()
        emp.save_employee (input_payperiod_from,input_payperiod_to,input_pay_date,input_full_name,input_basic_pay,input_allowance_1,input_allowance_2,input_allowance_3,input_allowance_4,input_allowance_calc,input_deduc_1,input_deduc_2,input_deduc_3,input_deduc_4,input_deduc_calc,input_additional_1,input_additional_2,input_additional_3,input_additional_4,input_additional_calc,input_net_pay,input_notes,long(input_id))
        self.redirect('/')

































class Main2Handler(webapp2.RequestHandler):
    def get(self):
        emp = Expense() 
        template_values = {'employees' : emp.list_expense()}
        template = jinja_environment.get_template('template/index2.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        user = users.get_current_user()
        if user:
            if self.request.POST.get('delete'): #if user clicks "Delete" button
                employee_ids = self.request.get('employee_id',allow_multiple=True) #allow_multiple=True so that it reads multiple key into list.
                emp = Expense()
                emp.delete_expense(employee_ids)
                self.redirect('/index2')
        else:
            self.redirect(users.create_login_url(self.request.uri))

class Create2Handler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            template = jinja_environment.get_template('template/create2.html')
            self.response.out.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_date_spent = self.request.get('date_spent').strip()
        input_description = self.request.get('description').strip()
        input_supplier = self.request.get('supplier').strip()
        input_amount = self.request.get('amount').strip()
        input_tax_type = self.request.get('tax_type').strip()
        input_payment_method = self.request.get('payment_method').strip()
        input_account = self.request.get('account').strip()
        input_client_project = self.request.get('client_project').strip()
        input_receipt_image = self.request.get('receipt_image').strip()
        input_notes = self.request.get('notes').strip()
        
        
        emp = Expense()
        emp.save_expense(input_date_spent,input_description,input_supplier,input_amount,input_tax_type,input_payment_method,input_account,input_client_project,input_receipt_image,input_notes,0)
        self.redirect('/create2')


class Edit2Handler(webapp2.RequestHandler):
    def get (self):
        user = users.get_current_user()
        if user:
            #get ID of entity Key
            emp_k = db.Key.from_path('CompanyModel','Bellucci','ExpenseModel',long(self.request.get('id')))
            #get entity from key instance
            emp = db.get(emp_k)
            
            template_values = {'employee' : emp}
            template = jinja_environment.get_template('template/edit2.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))
    def post(self):
        #get all input values
        input_id = self.request.get('id')
        input_date_spent = self.request.get('date_spent').strip()
        input_description = self.request.get('description').strip()
        input_supplier = self.request.get('supplier').strip()
        input_amount = self.request.get('amount').strip()
        input_tax_type = self.request.get('tax_type').strip()
        input_payment_method = self.request.get('payment_method').strip()
        input_account = self.request.get('account').strip()
        input_client_project = self.request.get('client_project').strip()
        input_receipt_image = self.request.get('receipt_image').strip()
        input_notes = self.request.get('notes').strip()

        emp = Expense()
        emp.save_employee (input_date_spent,input_description,input_supplier,input_amount,input_tax_type,input_payment_method,input_account,input_client_project,input_receipt_image,input_notes,long(input_id))
        self.redirect('/index2')