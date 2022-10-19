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

def get_all_employees():
    """gets all employees"""
    return EMPLOYEES
  
def get_single_employee(id):
    """gets single employee"""
    
    requested_employee = None
    
    for employee in EMPLOYEES:
        if employee["id"] == id:
           requested_employee = employee
    
    return requested_employee

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
