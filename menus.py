import os, io, sys
import encryption
import gDrive
import admin

e = encryption
drive = gDrive
admin = admin

def adminMenu():
	while 1:
		try:
			# Get user input.
			user_input = raw_input("\n-- Admin Menu --\n[1] Add New Account\n[2] Delete User Account\n[3] Go to main menu\n[Ctrl+C] To log out and exit.\n\nEnter Number: ")
            
			if(user_input == '1'):
				admin.createUser()

			elif(user_input == '2'):
				admin.deleteUser()

			elif(user_input == '3'):
				menu()

			else:
				print("Invalid entry.\n")

		except KeyboardInterrupt:   # Ctrl+C to exit
			print("\n-->  Application Exiting...\nGoodbye.")
			sys.exit()

def menu():
    while 1:
        try:
            # Get user input.
            user_input = raw_input("\n-- Main Menu --\n[1] Encrypt and Upload File to Drive\n[2] Download File from Drive and Decrypt\n[3] List Files in Drive\n[Ctrl+C] To log out and exit.\n\nEnter Number: ")
            
            if(user_input == '1'):
				filename = raw_input("File name: ")
				filepath = "Test_Files/" + filename
				if os.path.exists(filepath):
					e.encrypt(e.getKey(), filename)
					drive.uploadFile("(encrypted)"+filename,"(encrypted)"+filename)
					print("Done.")
				else:
					print("File doesnt exist in Test_Files.")
					
            elif(user_input == '2'):
                filename = raw_input("File name: ")
                file_id = drive.getFileId(1, "name contains '"+filename+"'")
                if file_id!=0:
	                drive.downloadFile(file_id,filename)
	                e.decrypt(e.getKey(), filename)
	                os.remove("Downloads/"+filename)
	                print("Done.")

            elif(user_input == '3'):
                files = raw_input("Please enter the number of files you wish to be listed: ") 
                drive.listFiles(files)    # List Files function called

            else:
                print("Invalid entry.\n")

        except KeyboardInterrupt:   # Ctrl+C to exit
            print("\n-->  Application Exiting...\nGoodbye.")
            sys.exit()



