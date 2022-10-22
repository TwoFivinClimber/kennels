import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
      "id": 1,
      "name": "Mitch McCullough",
      "title": "Surgeon"
    },
    {
      "id": 2,
      "name": "Lesley Keyes",
      "title": "Chief of Staff"
    },
    {
      "id": 3,
      "name": "Christian Black",
      "title": "Head of Fun Department"
    },
    {
      "id": 4,
      "name": "Justin Ferwerda",
      "title": "Janitor"
    },
]

# def get_all_employees():
#     """gets all employees"""
#     return EMPLOYEES
  
# def get_single_employee(id):
#     """gets single employee"""
    
#     requested_employee = None
    
#     for employee in EMPLOYEES:
#         if employee["id"] == id:
#            requested_employee = employee
    
#     return requested_employee

def create_employee(employee):
    """creates location"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee
  
def delete_employee(id):
    """deletes employee"""
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
        
def update_employee(id, new_employee):
    """updates employee"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break


# Requests with SQLITE #

def get_all_employees():
    """gets all employees"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a                          
        """)
        
        employees = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'],
                                row['location_id'])
          
            employees.append(employee.__dict__)
            
    return json.dumps(employees)
  

def get_single_employee(id):
    """gets single employee"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?                          
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        employee = Employee(data['id'], data['name'], data['address'],
                                data['location_id'])
        
    return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):
    """Gets employees by location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.location_id = ?                          
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
