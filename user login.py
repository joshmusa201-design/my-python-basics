

user_name: str = input ("enter your name ")
print ("enter your password, password must be 6 digits and contain digits, alphabet and special characters")
password = input("")



alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special_charaters = "~`@#$%^&}*()_+{|?><"
#tying to add certain critirials to the lodgin system
#version 2

has_alphabet = False
has_numbers = False
has_special = False

for passw in password:
   if passw.isalpha():
      has_alphabet = True
   elif passw.isdigit():
      has_numbers = True
   elif passw in special_charaters:
      has_special = True
while  True:
   if (len(password)) == 6 and has_alphabet and has_numbers and has_special:
       break
   elif password == "":
       print("input something !!")
       password = input("")
   else:
       print("password must be 6 digit long and contain digit a special letter and  a alphabet")
       break
password = input("")
if (len(password)) == 6 and has_alphabet and has_numbers and has_special:
   print()
else:
   print ("enter your email")
   input("")

print(f" you are welcome {user_name}")
print ("welcome !!!!")


