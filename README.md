# University Access Control System

This is a simple **Python-based Access Control System** for managing users and their permissions in a university setting. Users can **login**, **register**, and perform actions based on their assigned roles. The system stores user data locally in a JSON file (`users.json`) and enforces role-based permissions.  

---

## Features

- **Role-based Access Control**  
  Three roles with distinct permissions:  
  - **Admin:** create, edit all, delete, view  
  - **Editor:** create, edit own, view  
  - **Viewer:** view only  

- **User Registration:**  
  Register new users with a chosen role.

- **Permission Checks:**  
  Validate if a user can perform a specific action.

- **Persistent Storage:**  
  User data is stored in `users.json` for persistence.

- **Interactive Command-Line Interface (CLI):**  
  Easy-to-use menu for login, registration, and exit.

---

## Installation

1. Make sure you have **Python 3.x** installed.  
2. Clone or download this repository.  
3. Run the program in a terminal:  

```bash
python access_control.py
