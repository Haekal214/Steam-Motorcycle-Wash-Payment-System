# 🧼 Steam Motorcycle Wash Payment System

A simple yet functional **cashier application** built with **Python Tkinter**, designed to manage transactions at a steam-based motorcycle wash. This app features a secure login system, customer data entry, payment processing, and CSV-based record management.

---

## ✨ Features

- 🔐 **Login Authentication**  
  Secure access via hardcoded credentials (`user1:123`, `user2:456`) with input validation and error messages.

- 🧾 **Main Menu Interface**  
  - Input customer data: Plate number, Name, and Motorcycle Type  
  - Motorcycle types & prices:  
    - Small → Rp15.000  
    - Big → Rp18.000  
    - Trail → Rp22.000  
  - User-friendly dropdowns (Combobox)  
  - Save all data to `databaseM.csv`

- 💰 **Payment Menu**  
  - Displays customer queue via Listbox (with scrollbar)  
  - **Bayar** button: Calculates total cost and removes selected entry from CSV  
  - **Hapus** button: Deletes selected record from the file  
  - CSV read/write ensures persistent storage

---

## 🧠 System Overview

### 🔹 Login Window
- Size: 266 × 367 pixels  
- Validates hardcoded user credentials  
- On success → navigates to Main Menu  
- On failure → shows error popup

### 🔹 Main Menu (720 × 480 px)
- Inputs: Customer name, plate number, motorcycle type  
- Buttons:  
  - **Home** → Returns to home screen  
  - **Bayar** → Opens payment interface  
  - **Exit** → Exits app with confirmation  
- Records stored in `databaseM.csv`

### 🔹 Payment Menu
- Scrollable Listbox displays queue  
- Buttons:  
  - **Bayar** → Calculates & removes transaction  
  - **Hapus** → Deletes selected entry  

---

## ▶️ Getting Started

### ✅ Requirements

- Python 3.x  
- Tkinter (comes with most Python installations)  
- CSV module (built-in)  
- PNG files for GUI layout (included in `/assets`)

### 💻 How to Run

1. Clone this repository  
2. Run the app
3. Use login credentials:
  - user1 / 123
  - user2 / 456
4. Start managing your steam wash queue and payments!

---
