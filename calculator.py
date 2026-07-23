user_name = input ("ENTER YOUR NAME ").upper()
welcome_user = (f"welcome to my calculator {user_name}")
print (welcome_user)

first_no = int (input("enter a number "))
operator_signs = input ("choose an operator (+, -, *, /) ")
second_no = int (input("enter a second number "))


if operator_signs == "+":
    print (first_no + second_no)
elif operator_signs == "-":
    print (first_no - second_no)
elif operator_signs == "*":
    print (first_no * second_no)
elif operator_signs == "/" :
   print (first_no / second_no)

while True:
    print("do you want to keep playin ? (y/n)")
    keep_playing = input ("")
    if keep_playing == "y".lower():
      first_no = int (input("enter a number "))
      operator_signs = input ("choose an operator (+, -, *, /) ")
      second_no = int (input("enter a second number "))
    elif operator_signs == "+":
      print (first_no + second_no)
    elif operator_signs == "-":
      print (first_no - second_no)
    elif operator_signs == "*":
      print (first_no * second_no)
    elif operator_signs == "/" :
      print (first_no / second_no)
    else:
     keep_playing == "n".lower()
    print ("GOOD BYE KING!!")
    break

# kraff gald rapping music is gold buddy
# will you be my prompt for valatine buddy?
#be real wth me king