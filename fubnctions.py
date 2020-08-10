from tkinter import *
from tkinter.messagebox import *

class func:
    # total bill value
    def total_bill_value_f(self,price,quantity,total):
        print("Total function is called")
        total_bill = int(price) * int(quantity)
        if len(total)==0:
            total = 0
            total1 = int(total) + int(total_bill)
        else:
            total1 = int(total) + int(total_bill)
        return total1

    #adding new items to customer bill
    def add_items(self,item_name, item_model,item_sr,quantity,warranty,price,items):
        print("Adding items")
        items_detail = []
        items_detail.append(item_name)
        items_detail.append(item_model)
        items_detail.append(item_sr)
        items_detail.append(quantity)
        items_detail.append(warranty)
        items_detail.append(price)
        items.append(items_detail)
        print(items)

######### Dummy Bill format for start page
    def welcome_bill(self,textArea,date, billno, customer_name, customer_no, customer_address):
        print("Welcome bill function is called")
        textArea.delete('1.0', END)
        textArea.insert(END, "\n\t\t\t  *********************")
        textArea.insert(END, "\n\t\t\t  * AKASH ENTERPRISES *")
        textArea.insert(END, "\n\t\t\t  *********************")
        textArea.insert(END, f"\n\n\tBill No.{billno}\t\t\t\t       Date:{date}")
        textArea.insert(END, f"\n\tName: {customer_name}")
        textArea.insert(END, f"\n\tPhone: {customer_no}")
        textArea.insert(END, f"\n\tAddress: {customer_address}")
        textArea.insert(END, "\n\n\t******************************************************")
        textArea.insert(END, "\n\tProduct\t\tRate\t\tQuantity\t\tPrice")
        textArea.insert(END, "\n\t******************************************************")

    ####Customer Bill
    def bill(self, customer_name, customer_address, customer_no, items, textArea, total) :
        print("Bill fucnction is called")
        if (not customer_name):
            showerror("Error", "Enter Customer Name")
        elif not customer_address:
            showerror("Error", "Enter Customer Address")
        elif not customer_no:
            showerror("Error", "Enter Customer Phone Number")
        elif len(items) == 0:
            showerror("Error", "No Item")

        else:
            for i in range(len(items)):
                total_item_value = int(items[i][5]) * int(items[i][3])
                textArea.insert(END,
                                     f"\n\t{items[i][0]}\t\t{items[i][5]}\t\t{items[i][3]}\t\t{total_item_value}")
                if (len(items[i][1]) != 0):
                    textArea.insert(END, f"\n\tM.no:{items[i][1]}")
                if len(items[i][2]) != 0:
                    textArea.insert(END, f"\n\tSr.no:{items[i][2]}")
                if len(items[i][4]) != 0:
                    textArea.insert(END, f"\n\tWarrant:{items[i][4]}")


            textArea.insert(END, f"\n\n\n\t\t\t\t\t\tTotal:\t{total}")

