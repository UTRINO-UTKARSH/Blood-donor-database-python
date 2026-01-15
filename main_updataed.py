import mysql.connector as a
from prettytable import PrettyTable

# USER ID GENRATOR
import random
b = random.randrange(1, 10000000)
genrate = b

# MYSQL-PYTHON CONNECTION AND CODE
db = a.connect(host="localhost", password="YOUR_PASSWORD",
               user="YOUR_USERNAME", database="blood_donor_database")
cur = db.cursor()

# IMPORTANT FUNCTIONS

# SIGNIN


def signin():
    print("\tPlease enter Your Details Properly :) \n")
    Name = str(input("Enter Your Name: ")).lower()
    Age = int(input("Enter Your Age: "))
    Phone_Number = str(input("Enter Your Phone Number: "))
    Address = str(input("Enter Your Present Address: "))
    State = str(input("Enter The State Where You Live: "))
    District = str(input("Enter District: "))
    Email_Id = str(input("Enter you email-id: "))
    Password = str(input("Enter your password: "))
    User_Id = genrate
    print("\n \n")
    if Age <= 18:
        print("Your Are Underage......")
        exit()
    else:
        cur.execute(
            "INSERT INTO personal_details VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s)",
            (Name, Age, Phone_Number, Address, State,
             District, Email_Id, Password, User_Id)
        )
        db.commit()
    print("\tAccount Created Successfully......... \n")
    print(
        f'\t\tYour USER_ID is \t{User_Id}\t keep This Safe Your Further Use....\n')
    print("\tNow Give Your Medical History\t")
    Medical_History()

# LOGIN


def login():
    print("\t Login Process Starts From Now...... \n")
    Name = str(input("Enter Your Name: ")).lower()
    Email_Id = str(input("Enter Your Email-Id: "))
    Password = str(input("Enter Your Password: "))
    try:
        # Check if the provided email and password match a record in the database
        cur.execute(
            "SELECT * FROM personal_details WHERE Email_Id = %s AND Password = %s", (Email_Id, Password))
        result = cur.fetchone()

        if result:
            print("\tLogin successful.......\n Welcome back,", result[0])
        else:
            print("Login failed. Invalid credentials")
            exit()
    finally:
        pass
# ENTER MEDICAL HISTORY


def Medical_History():
    print('\n')
    print(" \t Please Enter Your Medical details \n")
    Name = input("Enter You Full Name: ")
    Allergies = input("Enter Your Allergies (If Any) else write 'N/A' : ")
    Height = input("Enter Your Height in cm: ")
    Weight = input("Enter Your Weight: ")
    Blood_Type = input("Enter Your Blood Group: ")
    Any_Severe_Medical_History = input(
        "Enter any severe medical condition or operation you have gone through (If Any) Else write "
        "N/A: ")
    Any_Disease = input(
        "Any Genetic or Permanent Disease (If Any) else Write N/A: ")
    Any_Disease_Related_To_Blood = input(
        "(If Any) Disease related to blood else write N/A: ")
    Any_Vaccination = input("Any Recent Vaccination else write N/A: ")
    Any_Medication_Going_On = input(
        "Any Medication on going if yes, then name the disease (eg:- BP,Thyroid,Sugar,Dibaties etc..) else write N/A: ")
    Age = int(input("Enter Your Age: "))
    User_Id = genrate
    print("\n \n")
    if Age <= 18:
        print("Your Are Underage......")

    else:
        cur.execute(
            "INSERT INTO Medical_Details VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
            (Name, Allergies, Height, Weight, Blood_Type, Any_Severe_Medical_History,
             Any_Disease, Any_Disease_Related_To_Blood, Any_Vaccination, Any_Medication_Going_On, Age, User_Id)
        )

        db.commit()
        print("Medical History Updated......")
        print("Now Login to continue......")
        exit()
# SHOW MEDICAL DATA


def User_Check():
    username = input("Enter You Name: ")
    user_id = int(input("Enter The User_Id Provided To You During Signin: "))
    query = "SELECT * FROM Medical_Details WHERE User_Id = %s AND Name = %s"
    cur.execute(query, (user_id, username))

    user_data = cur.fetchone()

    if user_data:
        user_id = user_data[-1]
        medical_data_query = "SELECT * FROM Medical_Details WHERE User_Id = %s"
        cur.execute(medical_data_query, (user_id,))
        medical_details = cur.fetchall()

        # Now Printing The Medical details
        if medical_details:
            if medical_details:
                table = PrettyTable()
                table.field_names = ["Name", "Allergies", "Height", "Weight", "Blood Type", "Medical_History",
                                     "Any Disease", "Blood Disease", "Any Vaccination", "Medication", "Age"]

                for record in medical_details:
                    table.add_row(record[:11])

                print(table)
        else:
            print("No Medical History Found For The User named:", username)
    else:
        print("The Provided name or user_id is not available in our database.")

# Donnation bank location


def BanK_Details():
    print("\tHere Are Your Neccessary Information :)\n")
    print("\n\n")
    print("\tWARNING\n \t If the number of blood type is low then don't choose that bank\n")
    query = "SELECT * FROM Donnation_Bank_Info"
    cur.execute(query)
    Bank_info = cur.fetchall()

    if Bank_info:
        table = PrettyTable()
        table.field_names = ["Bank_Id", "Name", "Postal Code",
                             "Address", "State", "District", "Landmark", "Contact"]

        for rec in Bank_info:
            table.add_row(rec[:8])

        print(table)
        print("\n\n")
        print("\t They All Have All The Blood_Group Blood present\n")
        print("That's All....")
    else:
        print("No active bank available.....")
# DOCTOR INFORMATION:


def DOCTOR_INFO():
    print("\t Here's The List OF All The Doctor Available And Don't Share Any Critical Infromation with them: \n Like Your Bank account details and all as the fee of doctor will be paid at the end of the month\n For that we will send you the notification to pay the bills..... \n\n")
    user_name = input("Enter The Name Of Paitent: ")
    Age = input("Enter the age of the Patient: ")
    Problem = input("Enter Patient's Disease: ")
    Classify = input(
        "Is Patient A infant,child,teenager,adult or Senior_Citizen, others: ").lower()
    if Classify == 'infant':
        print("\t\nWelcome to the Infant Section, The Details for Doctor Suitable For This Are Below...\n")
        query = "SELECT * FROM Doctor_Details WHERE CLASSIFY = Infant"
        cur.execute(query)
    Result = cur.fetchall()

    if Result:
        table = PrettyTable()
        table.field_names = ["Name", "Specification",
                             "Experience", "Contact", "Gender","Classify","Age"]

        for res in Result:
            table.add_row(res[0:7])
        print(table)

        

# Main Section
while True:
    print("\n")
    print(" \t ******************************WELCOME TO THE BLOOD DONATION CAMP************************** \t")
    print("\n")
    b = str(input("Enter Your Name: "))
    print("Hello", b, "And Welcome To This Camp..... \n")

    role = input("Are You A Doctor or Donnation_Bank_Owner or a User: ").lower()
    if role == 'doctor':
        with open("DOCTOR_FILLUP.py") as f:
            exec(f.read())                        # file connection DOCTOR_FILLUP
    if role == "donnation_bank_owner":
        with open("DONNATION_BANK_REGISTRATION.py") as ak:
            exec(ak.read()) # file connection DONNATION_BANK_REGISTRATION


    if role == 'user':
        
            res = str(input("Are You New Here?: ")).lower()
            if res == "yes":
                print(
                    "So", b, "Let's Build Your Account First and Add All The Details CareFully :) \n")
                signin()
            elif res == "no":
                print("\t\tPlease Login To Continue.....")
                login()
            else:
                print("Enter Correct Response.... \n Try Again....!!")
                break

            print('''\t\nPlease Select The Option You Want To Do..........
                1. Make Appointment with doctor for medical assistance 
                2. Want To Donate?... 
                3. Update Medical History
                4. View Your Medical Histroy
                \n''')

            ans = input("Enter Your response by choosing The numbers: ")
            if ans == '1':
                print("\t Here's The List Of Doctors Available Right now..... \n")
                DOCTOR_INFO()

            if ans == '2':
                print("\tHere's The Location Of All The Active Donnation Banks which support or Accept Blood Donnation...... \n")
                BanK_Details()

            if ans == '3':
                print(
                    "\t Now You are Going To Give Your Medical Details So do it carefully :) \n")
                Medical_History()

            if ans == '4':
                User_Check()


    # Close cursor and database connection at the end
    cur.close()
    db.close()
