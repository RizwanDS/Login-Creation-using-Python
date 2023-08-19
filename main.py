from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Students Registration Form")

def getvals():
    print("Accepted")

# Heading
Label(root, text = "Registration Form", font ="Arial 15 bold").grid(row=0, column=3)

#Field Names
name  = Label(root, text = "Name")
phone  = Label(root, text = "Phone")
gender = Label(root, text = "Gender")
emergency= Label(root, text = "Emergency")
paymentmode= Label(root, text = "Payment Mode")

#Packing Fields:
name.grid(row =2, column=2)
phone.grid(row =3, column=2)
gender.grid(row =4, column=2)
emergency.grid(row=5, column=2)
paymentmode.grid(row=6, column=2)

#Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue =StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

#Creating entry field:
nameentry =Entry(root, textvariable= namevalue)
phoneentry =Entry(root, textvariable = phonevalue)
genderentry =Entry(root, textvariable = gendervalue)
emergencyentry =Entry(root, textvariable = emergencyvalue )
paymentmodeentry =Entry(root, textvariable = paymentmodevalue)

#Packing Entry fields:

nameentry .grid(row=2, column=3)
phoneentry .grid(row=3, column=3)
genderentry .grid(row=4, column=3)
emergencyentry .grid(row=5, column=3)
paymentmodeentry .grid(row=6, column=3)

#Creating check box
checkbtn = Checkbutton(text ="Remember me?", variable = checkvalue)
checkbtn.grid(row = 7, column= 3)

#Submit Button
Button(text="Submit", command=getvals).grid(row =8, column =3)

root.mainloop()

