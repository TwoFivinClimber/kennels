CUSTOMERS = [
        {
          "id": 1,
          "name": "John Jameson"
        },
        {
          "id": 2,
          "name": "Jack Daniels"
        },
        {
          "id": 3,
          "name": "Luxy Luxardo"
        },
        {
          "id": 4,
          "name": "Mellie MellowCorn"
        }
]

def get_all_customers():
    """gets all customers"""
    return CUSTOMERS

def get_single_customer(id):
    """gets single customer"""
    requested_customer = None
    
    for customer in CUSTOMERS:
      if customer["id"] == id:
        requested_customer = customer
    
    return requested_customer
  
def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
