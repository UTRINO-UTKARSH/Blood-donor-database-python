# Blood Donor Database Management System (Python + MySQL)

This project was originally developed as my **Class 12 Computer Science practical project (2023–24)** using **Python and MySQL**.  
It implements a **menu-driven, terminal-based CRUD system** for managing blood donors, medical records, doctors, and donation banks.

This repository primary motive is to intentionally preserved the code **without refactoring** to maintain the originality and thought process from my early programming journey.

What makes this project special:
- Built completely **from scratch**
- No AI assistance or external frameworks
- Logic, flow, and features were planned manually
- Still works **unchanged after 3+ years** with modern Python & MySQL

---

## 🧠 Project Overview

The system simulates a **blood donation camp management platform**, supporting:

- User registration (sign-up)
- User login
- Medical history entry & retrieval
- Donation bank information lookup
- Doctor listing & appointment flow
- CLI-based interaction using menus

All operations are performed through the **command line interface**.

---

## 🛠 Tech Stack

- **Python**
- **MySQL**
- `mysql-connector-python`
- `prettytable` (for tabular CLI output)

---

## 📂 Project Structure

```text
UPDATED CODE/
├── main_updated.py
├── DOCTOR_FILLUP.py
├── DONNATION_BANK_REGISTRATION.py
└── sample_database
    |__blood_donner_database.sql
```

---

## 🏃‍♂️ How to Run

1. Ensure you have Python and MySQL installed on your system.

2. Setup MySQL
   import the <b>sample_database</b> to your own system
   1. First create your database, by running these commands in you <b>MySQL command line client</b>
   ```bash
      CREATE DATABASE YOUR_DB_NAME;
   ```
   then exit the command line<br>
   then run the below code in the terminal<br>
   <br>
   If you are using my sample_database then Make <b>Sure that you open the terminal in the exact folder where the sample is located</b> else it will not not be copied...
   ```bash
   mysql -u root -p Your_database_name < blood_donner_database.sql
   ```
3. Install the required packages using pip:
   ```bash
   pip install mysql-connector-python prettytable
   ```
5. Run the main application:
   ```bash
   python main_updated.py
   ```
6. Follow the on-screen instructions to navigate through the menu options.