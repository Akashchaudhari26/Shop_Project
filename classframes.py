from tkinter import *
from tkinter.messagebox import *
from Project.fubnctions import func
from Project.database import Database


function = func()
bg_color = "#d6d6d6"
title_font = ("times new roman", 30, "bold")
lable_font = ("times new roman", 15, "bold")


class MainScreen(Database):
    def __init__(self, root, date):
        self.root = root
        self.date = date
        self.root.geometry("1920x800+0+0")
        self.root.title("Bill Book")

        title = Label(self.root, text="AKASH ENTERPRISES", bd=5, relief=GROOVE, bg=bg_color, font=title_font, pady=5)
        title.pack(fill=X)
        #####################variables
        self.price = StringVar()
        self.quantity = StringVar()
        self.total = StringVar()
        self.warranty = StringVar()

        self.item_name = StringVar()
        self.item_model = StringVar()
        self.item_sr = StringVar()

        self.customer_name = StringVar()
        self.customer_address = StringVar()
        self.customer_no = StringVar()

        self.billno = IntVar()
        self.billnumber = int
        self.billnumber = Database.select_bill(self)+1
        self.billno.set(self.billnumber)

        self.items = []
        ###########customer details

        customer_frame = LabelFrame(self.root, text="Customer Details", font=lable_font, bg="#5c4949", fg="white", bd=5,
                                    pady=10, padx=10)
        customer_frame.place(x=0, y=70, relwidth=1)

        billNoLable = Label(customer_frame, text=" Bill No", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        billNoLable.grid(row=0, column=6, padx=20, pady=5)
        billNoText = Entry(customer_frame, textvariable=self.billno, width=10, font=lable_font, bd=6, relief=RIDGE)
        billNoText.grid(row=0, column=7, pady=10)

        customerNameLable = Label(customer_frame, text="Customer Name", font=lable_font, fg="white", bg="#5c4949",
                                  padx=5, pady=5)
        customerNameLable.grid(row=0, column=0, padx=20, pady=5)
        customerNameText = Entry(customer_frame, textvariable=self.customer_name, width=20, font=lable_font, bd=6,
                                 relief=RIDGE)
        customerNameText.grid(row=0, column=1, padx=5, pady=10)

        customerNoLable = Label(customer_frame, text="Mobile No. ", font=lable_font, fg="white", bg="#5c4949", padx=5,
                                pady=5)
        customerNoLable.grid(row=0, column=2, padx=20, pady=5)
        customerNoText = Entry(customer_frame, textvariable=self.customer_no, width=12, font=lable_font, bd=6,
                               relief=RIDGE)
        customerNoText.grid(row=0, column=3, padx=5, pady=10)

        customerAddressLable = Label(customer_frame, text="Address", font=lable_font, fg="white", bg="#5c4949", padx=5,
                                     pady=5)
        customerAddressLable.grid(row=0, column=4, padx=20, pady=5, sticky=W)
        customerAddressText = Entry(customer_frame, textvariable=self.customer_address, width=20, font=lable_font, bd=6,
                                    relief=RIDGE)
        customerAddressText.grid(row=0, column=5, padx=5, pady=10)

        date = Label(customer_frame, text="Date ", font=lable_font, fg="white", bg="#5c4949", padx=5,
                     pady=5)
        date.grid(row=0, column=8, padx=20, pady=5, sticky=W)
        dateText = Entry(customer_frame, width=10, font=lable_font, bd=6, relief=RIDGE)
        dateText.grid(row=0, column=9, padx=5, pady=10)
        dateText.insert(END, self.date)

        self.item_details()

        btnFrame = Frame(self.root, bg="#5c4949", bd=5, pady=10,
                         padx=10)
        btnFrame.place(x=50, y=600, width=700)

        generateBtn = Button(btnFrame, command=self.total_bill, text="Generate Bill", bd=5, width=10, padx=5,
                             font=lable_font)
        generateBtn.grid(row=0, column=1, padx=40, pady=5)

        clrBtn = Button(btnFrame, command=self.clearall, text="Clear", bd=5, width=10, font=lable_font)
        clrBtn.grid(row=0, column=0, padx=40, pady=5)

        printBtn = Button(btnFrame, command=self.print_bill, text="Print", bd=5, width=10, padx=5,
                          font=lable_font)
        printBtn.grid(row=0, column=2, padx=40, pady=5)



        # billl area
        billArea = Frame(self.root, bd=5, bg="#5c4949")
        billArea.place(x=900, y=190, height=600, width=600)
        bill_title = Label(billArea, text="BILL", font=lable_font, bg="#5c4949", fg="white")
        bill_title.pack(fill=X)
        scrollY = Scrollbar(billArea, orient=VERTICAL)
        self.textArea = Text(billArea, yscrollcommand=scrollY.set)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.textArea.yview)
        self.textArea.pack(fill=BOTH, expand=1)
        self.welcome_bill()

    def total_bill_value(self):
        total1 = function.total_bill_value_f(self.price.get(),self.quantity.get(),self.total.get())
        self.total.set(str(total1))

    def total_bill(self):

        try:
            self.add_items()
        except:
            print("Exception")
        finally:
            self.bill()

    def add_items(self):
        total1 = function.total_bill_value_f(self.price.get(),self.quantity.get(),self.total.get())
        function.add_items(self.item_name.get(), self.item_model.get(),
                           self.item_sr.get(), self.quantity.get(),
                           self.warranty.get(), self.price.get(),self.items)
        self.clear()
        self.total.set(str(total1))

    def clear(self):
        self.item_name.set("")
        self.item_model.set("")
        self.item_sr.set("")
        self.quantity.set("")
        self.warranty.set("")
        self.price.set("")

    def clearall(self):
        self.customer_name.set("")
        self.customer_no.set("")
        self.customer_address.set("")
        self.total.set("")
        self.clear()
        self.welcome_bill()
        self.items.clear()

    def welcome_bill(self):
        function.welcome_bill(self.textArea, self.date, self.billno.get(), self.customer_name.get(), self.customer_no.get(),self.customer_address.get())

    def bill(self):
        function.welcome_bill(self.textArea, self.date, self.billno.get(), self.customer_name.get(), self.customer_no.get(),self.customer_address.get())
        function.bill(self.customer_name.get(), self.customer_address.get(),
                      self.customer_no.get(), self.items, self.textArea, self.total.get())
        Database.insert(self,self.billno.get(),self.customer_name.get(),self.customer_no.get(),self.customer_address.get(),self.date)

    def print_bill(self):
        self.clearall()
        self.billnumber = self.billno.get() + 1
        self.welcome_bill()
        self.billno.set(self.billnumber)


    def item_details(self):
        ####### Items Details

        itemFrame = LabelFrame(self.root, text="Item Details", font=lable_font, bg="#5c4949", fg="white", bd=5, pady=10,
                               padx=10)
        itemFrame.place(x=50, y=300, width=700)

        itemNameLable = Label(itemFrame, text="Item Name", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        itemNameLable.grid(row=0, column=0, padx=20, pady=5)
        itemNameText = Entry(itemFrame, textvariable=self.item_name, width=20, font=lable_font, bd=6, relief=RIDGE)
        itemNameText.grid(row=0, column=1, padx=5, pady=10)

        quantityLable = Label(itemFrame, text="Quantity", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        quantityLable.grid(row=0, column=2, padx=20, pady=5, stick=W)
        quantityText = Entry(itemFrame, textvariable=self.quantity, width=10, font=lable_font, bd=6, relief=RIDGE)
        quantityText.grid(row=0, column=3, padx=5, pady=10)

        modelNoLable = Label(itemFrame, text="Model No", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        modelNoLable.grid(row=1, column=0, padx=20, pady=5, stick=W)
        modelNoText = Entry(itemFrame, textvariable=self.item_model, width=20, font=lable_font, bd=6, relief=RIDGE)
        modelNoText.grid(row=1, column=1, padx=5, pady=10)

        priceLable = Label(itemFrame, text="Price", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        priceLable.grid(row=1, column=2, padx=20, pady=5, stick=W)
        priceText = Entry(itemFrame, textvariable=self.price, width=10, font=lable_font, bd=6, relief=RIDGE)
        priceText.grid(row=1, column=3, padx=5, pady=10)

        srNoLable = Label(itemFrame, text="Serial No", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        srNoLable.grid(row=2, column=0, padx=20, pady=5, stick=W)
        srNoText = Entry(itemFrame, textvariable=self.item_sr, width=20, font=lable_font, bd=6, relief=RIDGE)
        srNoText.grid(row=2, column=1, padx=5, pady=10)

        warrantyLable = Label(itemFrame, text="Warranty", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        warrantyLable.grid(row=3, column=0, padx=20, pady=5, stick=W)
        warrantyText = Entry(itemFrame, textvariable=self.warranty, width=20, font=lable_font, bd=6, relief=RIDGE)
        warrantyText.grid(row=3, column=1, padx=5, pady=10)

        totalLable = Label(itemFrame, text="Total", font=lable_font, fg="white", bg="#5c4949", padx=5, pady=5)
        totalLable.grid(row=2, column=2, padx=20, pady=5, stick=W)
        totalText = Entry(itemFrame, textvariable=self.total, width=10, font=lable_font, bd=6, relief=RIDGE,
                          state='disabled')
        totalText.grid(row=2, column=3, padx=5, pady=10)

        add = Button(itemFrame, command=self.add_items, text="Add Items", bd=5, font=lable_font, width=8)
        add.grid(row=3, column=3, padx=10, pady=5)
        clear = Button(itemFrame, command=self.clear, text="Clear", bd=5, font=lable_font, width=8)
        clear.grid(row=3, column=2, padx=10, pady=5)
