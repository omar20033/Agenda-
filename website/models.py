import sqlite3





def get_departments():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nom FROM DEPARTEMENT')
    departments = cursor.fetchall()
    conn.close()
    return departments    

def get_employees_by_department(department_name):
    conn = sqlite3.connect('user_database.db')  # Update with your database name
    cursor = conn.cursor()
    cursor.execute('SELECT nom,numEmploye FROM EMPLOYE WHERE numDept = (SELECT num FROM DEPARTEMENT WHERE nom = ?)', (department_name,))
    employees = [row[0] for row in cursor.fetchall()]
    conn.close()
    return employees
def get_Agenda_by_department(department_name):
    conn = sqlite3.connect('user_database.db')  # Update with your database name
    cursor = conn.cursor()
    
    # Fetch the agenda number for the specified department name
    cursor.execute('SELECT numAgendaDept FROM DEPARTEMENT WHERE nom = ?', (department_name,))
    department_agenda = cursor.fetchone()
    
    if department_agenda:  # Check if department exists
        # Fetch activities for the department's agenda number from ACTIVITIESDEPT table
        cursor.execute('SELECT * FROM ACTIVITESDEPT WHERE numAgenda = ?', (department_agenda[0],))
        activities = cursor.fetchall()
        conn.close()
        return activities
    else:
        conn.close()
        return None
def get_employees():   
    conn = sqlite3.connect('user_database.db')  # Update with your database name
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMPLOYE ')
    employees = [row for row in cursor.fetchall()]
    conn.close()
    return employees


def get_employee_agenda(employee_name) : 
    
    conn = sqlite3.connect('user_database.db')  # Update with your database name
    cursor = conn.cursor()
    
    # Fetch the agenda number for the specified department name
    cursor.execute('SELECT * FROM ACTIVITES WHERE numAgenda = ?', (employee_name,))
    employe_agenda = cursor.fetchall()
    
    
    conn.close()
    return employe_agenda
    
    

def add_activity(activity_data):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ACTIVITES (typeA, description, dateAct, hDebut, hFin, dateCreation, createur, visible, numAgenda)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', activity_data)
    conn.commit()
    conn.close()
def add_activity_dept(activity_dept_data):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ACTIVITESDEPT (typeD, descript, dateAct, hDebut, hFin, dateCreation, createur, numAgenda)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', activity_dept_data)
    conn.commit()
    conn.close()        


















