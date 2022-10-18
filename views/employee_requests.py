EMPLOYEES = [
    {
      "id": 1,
      "name": "Mitch McCullough"
    },
    {
      "id": 2,
      "name": "Lesley Keyes"
    },
    {
      "id": 3,
      "name": "Christian Black"
    },
    {
      "id": 4,
      "name": "Justin Ferwerda"
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
