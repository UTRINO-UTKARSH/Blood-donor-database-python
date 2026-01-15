#THE BELOW CODE IS FOR THE ENTRY OF SOME SPECIFIC DETAILS FROM A DOCTOR

import random
id = random.randrange(1,99999990)
doc_id = id

#Important Function
#def signin():
   # print("\tEnter Your Details Properly....")
   # Name_of_Doctor = str(input("Enter Your Name: "))
   # Doctor_Specification = str(input("Enter Your Speciality or qualification in medical field: "))
   # Experience = str(input("How long have you been in this profession: "))
   # Contact_Details = str(input("Enter Your Contact Number So that Patient can contact you: "))
   # Gender = str(input("Enter Your Gender: "))
   # CLASSIFY = str(input("What age group patient you can treat for eg(infant,child,teenager,adult,senior citizen): "))
   # Age = int(input("Enter Your Age: "))
   # Doc_Id = doc_id
   # cur.execute(
    #"INSERT INTO personal_details VALUES(%s, %s, %s, %s, %s, %s,%s,%s)",
    #(Name_of_Doctor,Doctor_Specification,Experience,Contact_Details,CLASSIFY,
    #    Age,Doc_Id))
   # db.commit()
    #print("\tAccount Created Successfully......... \n")
   # print("\t Keep This Id Safe for Further Use ",doc_id)


def signin():
    print("\tPlease enter Your Details Properly :) \n")
    Name_Of_Doctor = str(input("Enter Your Name: ")).lower()
    Doctor_Specification = str(input("Enter Your Speciality or qualification in medical field: "))
    Experience = str(input("How long have you been in this profession: "))
    Contact_Details = str(input("Enter Your Contact Number So that Patient can contact you: "))
    Gender = str(input("Enter Your Gender: "))
    CLASSIFY = str(input("What age group patient you can treat for eg(infant,child,teenager,adult,senior citizen): "))
    Age = int(input("Enter Your Age: "))
    Doc_Id = doc_id
    print("\n\n")
    if Age <= 18:
        print("Your Are Underage......")
        exit()
    else:
        cur.execute(
            "INSERT INTO doctor_details VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
            (Name_Of_Doctor,Doctor_Specification,Experience,Contact_Details,Gender,
              CLASSIFY,Age,Doc_Id)
        )
        db.commit()
    print("\tAccount Created Successfully......... \n")







import mysql.connector as a
# MYSQL-PYTHON CONNECTION AND CODE
db = a.connect(host="localhost", password="YOUR_PASSWORD", user="YOUR_USERNAME", database="SAMPLE_DB")
cur = db.cursor()
d = input("\tWhat's Your Name: ")
print("Hello, ",d)
a = input("\t Greeting's from 'UTRINO BLOOD DONATION CAMP... I am UTRINO THE CHIEF OF THIS CAMP\n And would like to extend an offer of joining us is this program as a Doctor...: ").lower()
if a == 'yes':
    print("ALright Then First: Let's Start Your Account Creation")
    signin()
if a == 'no':
    print("It's Sad that one more talented being is not joining it.... :( ")
    exit()



cur.close()
db.close()    
