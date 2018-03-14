name = str(input("Please enter your Name: "))
email = str(input("What is your email address?: "))
phone_number = str(input("What is your phone number?: "))
password=str(input("Please enter your Password: "))
repassword = str(input("Please Re-Enter your Password: "))
if repassword == password :
        print ("Thank you for registering!")
if repassword != password:
        print("Your Password does not match your Re-Password, Please try again!")
        
def makeanAccount():
    something = str(input("Click Enter to login!\n"))
    if something == str(input("Enter")):
        login(0)
    
    




def login(attempts):
    attempts = 0
    email_attempt = str(input("Please enter your email address: "))
    if email_attempt == email:
        password_attempt = str(input("Please enter your password: "))
    if password_attempt == password:
        print ("Welcome to Facebook")
    else:
         print ("Your password is not correct, Please try again!")
         attempts = attempts + 1
         if attempts == 3:
            print ("You ran out of attempts, Sorry!")   
