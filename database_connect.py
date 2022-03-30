from http import client
from pymongo import MongoClient

def databaseConnection():
    client = MongoClient()
    db = client.revatureTrial
    return db



