import json
import pathlib
import bcrypt

logged_in = False  
current_user = None
DATABASE = pathlib.Path.cwd() / "Data" / "db.json"

def display_option():
   print("\n---- Welcome to User Management System ----")
   print("1. Login")
   print("2. Register")
   print("3. Exit")
   try:
      n = int(input("Enter Your Choice: "))
      return n
   except ValueError:
      return 0 

def display_home(user: str):
   print(f"\n--- Dashboard ---")
   print(f"Welcome back, {user}!")
   print("1. Logout")
   try:
      return int(input("Enter your choice: "))
   except ValueError:
      return 0


def main():
   global logged_in, current_user

   DATABASE.parent.mkdir(exist_ok=True)

   while True:
      if not logged_in:
         choice = display_option()

         if choice == 1:
               try:
                  with open(DATABASE, "r", encoding="utf-8") as f:
                     data = json.load(f)
               except (FileNotFoundError, json.JSONDecodeError):
                  print("\n[Error] No users registered. Please register first.")
                  continue

               username = input("Enter Username: ")
               
               user_account = next((user for user in data if user.get('username') == username), None)

               if user_account:
                  pwd = input("Enter Password: ")
                  stored_hash = user_account.get('password').encode('utf-8')

                  if bcrypt.checkpw(pwd.encode("utf-8"), stored_hash):
                     print("\nLogin successful!")
                     logged_in = True
                     current_user = username
                  else:
                     print("\n[Error] Incorrect password.")
               else:
                  print("\n[Error] Username doesn't exist.")

         elif choice == 2:
               try:
                  with open(DATABASE, "r", encoding="utf-8") as f:
                     data = json.load(f)
                  if not isinstance(data, list): data = []
               except (FileNotFoundError, json.JSONDecodeError):
                  data = []

               while True:
                  username = input("Enter Username: ")
                  if any(u.get('username') == username for u in data):
                     print("\n[Error] Username already exists. Please try another.")
                  else:
                     break
               
               while True:
                  pwd = input("Enter Password: ")
                  confirm_pwd = input("Confirm Password: ")
                  if pwd == confirm_pwd:
                     break
                  else:
                     print("\n[Error] Passwords didn't match. Please try again.")

               hashed_pw = bcrypt.hashpw(pwd.encode("utf-8"), bcrypt.gensalt(6))
               user = {
                  'username': username,
                  'password': hashed_pw.decode('utf-8')
               }
               
               data.append(user)
               with open(DATABASE, "w", encoding="utf-8") as f:
                  json.dump(data, f, indent=4)
               
               print(f"\nUser '{username}' registered successfully! Please log in.")

         elif choice == 3:
               print("Exiting...")
               break
         else:
               print("\n[Error] Invalid choice. Please try again.")
      
      else:
         choice = display_home(str(current_user))
         if choice == 1:
               print(f"Logging out {current_user}...")
               logged_in = False
               current_user = None
         else:
               print("\n[Error] Invalid choice.")


if __name__ == "__main__":
   main()