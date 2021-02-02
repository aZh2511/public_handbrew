
from pymongo import MongoClient
from config import *

cluster = MongoClient(DB_LINK)
db_handbrew = cluster['handbrew']
cln_item = db_handbrew['item']
cln_user = db_handbrew['user']
cln_order = db_handbrew['order']
