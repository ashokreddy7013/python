import pymysql.connections as my
from MySQLExamples.Demo1 import *

conn = my.connect(user="root",password="3306",host="127.0.0.1",port="3306",database="sathya")

TableCreation()