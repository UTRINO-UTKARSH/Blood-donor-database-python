#THE BELOW CODE IS FOR THE ENTRY OF DETAILS OF DONNATION BANK BY THE OWNER



def Fill_up():
    print("\tEnter Your Details Properly\n")
    Name_Of_Bank = str(input("Enter Name Of Your Bank: "))
    Postal_Code = int(input("Enter Postal Code: "))
    Contact_Number = str(input("Enter Your Banks Contact Number: "))
    Address_Of_Bank = str(input("Enter The Location of your bank: "))
    LANDMARK = str(input("Enter A Landmark which is near your bank: "))
    State = str(input("Enter The State: "))
    District = str(input("Enter The District: "))
    Number_of_Blood_Types = int(input("Enter The Number Of Blood_Group You Have Available:  "))

    cur.execute(
            "INSERT INTO donnation_bank_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
            (Name_Of_Bank, Postal_Code, Contact_Number, Address_Of_Bank, LANDMARK,
             State, District, Number_of_Blood_Types)
        )
    db.commit()    
    print("Registration Successfull............")



import mysql.connector as a
# MYSQL-PYTHON CONNECTION AND CODE
db = a.connect(host="localhost", password="YOUR_PASSWORD", user="YOUR_USERNAME", database="SAMPLE_DB")
cur = db.cursor()

print("\tHello Owner Of The Blood_Donnation Bank\n")
a = input("Would Like to give your services to us?: ").lower()
if a =='yes':
    print("\tThank Your For Your help :) \n")
    print("\t Do FIll up the details below to register your bank to our organization \n")
    Fill_up()
if a == 'no':
    print("\t\tIf You ever feel a change in mind remeber we are egarly waitting for your services :)\n")
