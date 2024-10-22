temperature=float(input('Enter temperature:'))
unit=input('Is the temperature is in farenheit or celcius (C or F)' )
if unit=='c' or unit=='C':
    farenheit=(9/5*temperature+32)
    print(farenheit,'F')
elif unit=='f' or unit=='F':
    celcius=(5/9*(temperature-32))
    print(celcius,'C')
else :
     print('wrong input')


