username = input("Username: ") 
password = input("Password: ")  
if username == "admin":     
  if password == "secret":         
    print("Access granted")     
  else:         
    print("Wrong password") 
else:     
    print("Unknown user")