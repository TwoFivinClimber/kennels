import sqlite3
import json
from models import Location

LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike",
      "status": "active"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive",
      "status": "active"
    }
]


# def get_all_locations():
#     """gets all the locations"""
#     return LOCATIONS

# def get_single_location(id):
#     """gets single locations"""
#     requested_location = None
#     for location in LOCATIONS:
#         if location["id"] == id:
#             requested_location = location
#     return requested_location

def create_location(location):
    """creates location"""
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    """deletes location"""
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)
        
def update_location(id, new_location):
    """updates location"""
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break

#Requests with SQL3#

def get_all_locations():
    """gets all locations"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a                          
        """)
        
        locations = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
          
            locations.append(location.__dict__)
            
    return json.dumps(locations)
  

def get_single_location(id):
    """gets single location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM employee a
        WHERE a.id = ?                          
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        location = Location(data['id'], data['name'], data['address'])
        
    return json.dumps(location.__dict__)
