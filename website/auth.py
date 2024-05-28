from flask import Flask, render_template,Blueprint,request,jsonify,session,flash,url_for,redirect,get_flashed_messages,abort
import website.models  

import sqlite3

from flask import request, render_template, jsonify, redirect, flash





auth=Blueprint('auth',__name__,template_folder='../Templates')












@auth.route("/",methods=['GET','POST'])
def home() : 
     
     departments = website.models.get_departments()
     return render_template('departments.html', departments=departments)

@auth.route('/<department_name>',methods=['GET','POST'])
def department_details(department_name):
    # In a real application, you would fetch department data based on the department_name
    # For demonstration purposes, let's create some example data
    department_data = {"name": department_name}

    return render_template('department_details.html', department_data=department_data)
@auth.route('/<department_name>/show_employees',methods=['GET','POST'])
def show_employees(department_name):
    # Fetch the list of employees working in the selected department from the models
    employees =  website.models.get_employees_by_department(department_name)
    return render_template('employees.html', employees=employees, department_name=department_name)
@auth.route('/<department_name>/agendaDept',methods=['GET','POST'])
def show_Agenda(department_name):
    # Fetch the list of employees working in the selected department from the models
    Agenda =  website.models.get_Agenda_by_department(department_name)
    return render_template('DeptAgenda.html', Agenda=Agenda, department_name=department_name)

@auth.route("/employees",methods=['GET','POST'])
def employees() : 
     
     employees =  website.models.get_employees()
     department_name = "All"
     return render_template('allemployees.html',employees=employees,department_name=department_name)


@auth.route("/employee/<employee_name>") 
def emplyee_agenda(employee_name):
        employee_agenda = website.models.get_employee_agenda(employee_name)
        return render_template("employeagenda.html", employee_agenda=employee_agenda)
@auth.route('/add_activity', methods=['GET', 'POST'])
def add_activity():
    if request.method == 'POST':
        activity_data = (
            request.form['typeA'],
            request.form['description'],
            request.form['dateAct'],
            request.form['hDebut'],
            request.form['hFin'],
            request.form['dateCreation'],
            request.form['createur'],
            request.form['visible'],
            request.form['numAgenda']
        )
        website.models.add_activity(activity_data)
        
    return render_template('AddActivityEmploye.html')

# Route to add an activity department
@auth.route('/add_activity_dept', methods=['GET', 'POST'])
def add_activity_dept():
    if request.method == 'POST':
        activity_dept_data = (
            request.form['typeD'],
            request.form['descript'],
            request.form['dateAct'],
            request.form['hDebut'],
            request.form['hFin'],
            request.form['dateCreation'],
            request.form['createur'],
            request.form['numAgenda']
        )
        website.models.add_activity_dept(activity_dept_data)
        
    return render_template('AddActivityDept.html')     



    







