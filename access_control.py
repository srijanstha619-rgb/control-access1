import json
import os

DATA_FILE = "users.json"
ROLE_PERMISSIONS = {
    "admin": ["create", "edit_all", "delete", "view"],
    "editor": ["create", "edit_own", "view"],
    "viewer": ["view"]
}

def load_data():
    if not os.path.exists(DATA_FILE):
        default_users = {"alice": "admin", "bob": "editor", "charlie": "viewer"}
        save_data(default_users)
        return default_users
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def register_user(user_database):
    print("\n--- User Registration ---")
    new_username = input("Enter new username: ").strip().lower()
    
    if new_username in user_database:
        print("Error: Username already exists!")
        return
    
    print(f"Available roles: {', '.join(ROLE_PERMISSIONS.keys())}")
    new_role = input("Enter role: ").strip().lower()
    
    if new_role not in ROLE_PERMISSIONS:
        print(f"Error: Invalid role. Please choose from {list(ROLE_PERMISSIONS.keys())}.")
        return

    user_database[new_username] = new_role
    save_data(user_database)
    print(f"Successfully registered {new_username} as {new_role}!")

def has_permission(username, action, user_database):
    role = user_database.get(username.lower())
    if not role:
        return False, "User not found."
    
    permissions = ROLE_PERMISSIONS.get(role, [])
    if action in permissions:
        return True, f"Access GRANTED: {username} ({role}) can '{action}'."
    return False, f"Access DENIED: {username} ({role}) cannot '{action}'."

def main():
    print("=== University Access Control System ===")
    users = load_data()
    
    while True:
        choice = input("\nChoose an option: [1] Login [2] Register [3] Exit: ").strip()
        
        if choice == '1':
            user_input = input("Username: ").strip()
            action_input = input("Action (view/create/edit_all/delete): ").strip()
            allowed, message = has_permission(user_input, action_input, users)
            print(f"{'SUCCESS' if allowed else 'FAILURE'}: {message}")
            
        elif choice == '2':
            register_user(users)
            
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
