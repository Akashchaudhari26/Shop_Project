from tkinter import *
from datetime import date

import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                     user='root',passwd='root',database='shop')

class Database:

    def insert(self, bill_no, customer_name, customer_no, customer_address, date):

        mycursor = connection.cursor()
        in_query = "insert into customer(bill_no,name,mobile_no,address,date)values(%s,%s,%s,%s,%s)"
        value = (bill_no,customer_name,customer_no,customer_address,date)
        mycursor.execute(in_query, value)
        connection.commit()

    def select_bill(self):
        mycursor = connection.cursor()
        select_query = "SELECT bill_no FROM customer WHERE bill_no=(SELECT max(bill_no) FROM customer)"
        mycursor.execute(select_query)
        result = mycursor.fetchone()
        try:
            return result[0]
        except :
            return 0

