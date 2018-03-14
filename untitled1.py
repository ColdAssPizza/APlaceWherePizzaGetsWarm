def testScore ():
    studentName = str(input('Enter Students Name: '))
    testScore = int(input('Enter test score from 0 - 100: '))
    if testScore > 100 or testScore < 0:
        print ("You have clearly made a mistake in your marking, 100% is the maxmium and 0% is the minimum") 
    elif testScore >= 90: 
            print('Your grade is A,', studentName,', Top of the Class! Keep it up hotshot!')
    if testScore >= 80:
            print('Your grade is B,', studentName,', Good stuff!, Keep it up!')
    elif testScore >= 70:
            print('Your grade is C,', studentName,', You got a C, Not Bad!')
    elif testScore >= 60:
            print('Your grade is D,', studentName,', You did your best, Try Harder Next Time!')
    elif testScore <= 50:
            print('Your grade is F,', studentName,', Try Harder Next Time!')
            
testScore()
 

