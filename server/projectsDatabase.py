# Import necessary libraries and modules
from pymongo import MongoClient

import hardwareDatabase

'''
Structure of Project entry:
Project = {
    'projectName': projectName,
    'projectId': projectId,
    'description': description,
    'hwSets': {HW1: 0, HW2: 10, ...},
    'users': [user1, user2, ...]
}
'''

# Function to query a project by its ID
def queryProject(client, projectId):
    # Query and return a project from the database
    pass

# Function to create a new project
def createProject(db_project, projectName, projectId, description, user):
    
    project = {
        'name': projectName,
        'projectId': projectId, 
        'description': description,
        'hwSets': {'HW1':0, 'HW2':0},
        'users': [user]
    }

    p = {'projectId': projectId}
    find = db_project.find_one(p)

    try:
        if find['projectId'] == projectId:
            return {'status': 0}                        #project already exists
    except:
        db_project.insert_one(project)
        return {'status': 1}

# Function to add a user to a project
def addUser(client, projectId, userId):
    # Add a user to the specified project
    pass

# Function to update hardware usage in a project
def updateUsage(client, projectId, hwSetName):
    # Update the usage of a hardware set in the specified project
    pass

# Function to check out hardware for a project
def checkOutHW(client, projectId, hwSetName, qty, userId):
    # Check out hardware for the specified project and update availability
    pass

# Function to check in hardware for a project
def checkInHW(client, projectId, hwSetName, qty, userId):
    # Check in hardware for the specified project and update availability
    pass

