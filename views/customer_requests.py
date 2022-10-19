CUSTOMERS = [
        {
          "id": 1,
          "name": "John Jameson",
          "last_seen": "10/4/2019"
        },
        {
          "id": 2,
          "name": "Jack Daniels",
          "last_seen": "8/6/2021"
        },
        {
          "id": 3,
          "name": "Luxy Luxardo",
          "last_seen": "1/29/2022"
        },
        {
          "id": 4,
          "name": "Mellie MellowCorn",
          "last_seen": "4/19/2016"
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
    """creates customer"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer

def delete_customer(id):
    """deletes customer"""
    customer_index = -1  
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index 
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """updates customer"""
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
