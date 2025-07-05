first_name = "Phoebe"
last_name = "Adikinyi"

#combine into full name and print using f string
print(f"First Name: {first_name}, Last Name: {last_name}")
message = input("Enter your message: ")

# Print the length
print(f"The length of your message is {len(message)} characters.")

# Print in uppercase
print(f"Message in uppercase: {message.upper()}")

# Print the first 5 characters
print(f"First 5 characters: {message[:5]}")
