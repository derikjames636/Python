def check_number():
    mobile_number = input('Enter the mobile number')
    if len(mobile_number)==10 and mobile_number[0] in '789':
        print('It is a valid number')
    else:
        print('The number is not valid ')
check_number()

