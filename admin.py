import getpass
import pickle
import sys, os
import menus

m= menus

# Function writes updated data back to file from obj
def writeToFile(obj, filename):
	with open(filename, 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# Function reads data from file and returns it
def readFromFile(filename):
	if os.path.getsize("users.pkl") > 0:
		with open(filename, 'rb') as f:
			return pickle.load(f)
	else:
		return {}

users = readFromFile("users.pkl")

 # Login function checks username and password
def login():
	try:
		if os.path.getsize("users.pkl") == 0:
			createUser()
		username, password = getUserDetails()
		if username in users and users[username] == password and username == "admin":
			print("Login Successful.")
			m.adminMenu()
		elif username in users and users[username] == password:
			print("Login Successful..")
			m.menu()
		else:
			print("\nIncorrect username or password.\nPlease try again.\n")
			login()
		return
	except KeyboardInterrupt:   # Ctrl+C to exit
		exit()

# Function creates new user
def createUser():
	try:
		print("\nPlease enter a new username and \npassword to create a user.")
		username, password = getUserDetails()
		if username in users:
			print("Sorry username already exists.")
		else:
			users[username] = password
			writeToFile(users, "users.pkl")
			print("User Created.")
			m.adminMenu()
	except KeyboardInterrupt:   # Ctrl+C to exit
		exit()

# Function deletes specified user
def deleteUser():
	try:
		username = raw_input("Enter username of account you wish to delete: ")
		if(username in users):
			del users[username]
			writeToFile(users, "users.pkl")
			print("User account removed.")
		else:
			print("User does'nt exist.")
		return
	except KeyboardInterrupt:   # Ctrl+C to exit
		exit()

# Function returns username and password
def getUserDetails():
	try:
	    username = raw_input("Username: ")
	    password = getpass.getpass()
	    return username, password
	except KeyboardInterrupt:   # Ctrl+C to exit
		exit()

def exit():
		print("\n-->  Application Exiting...\nGoodbye.")
		sys.exit()



