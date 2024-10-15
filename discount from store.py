purchase_amount=int(input('Enter purchase amount'))
if purchase_amount>500:
    final_amount=purchase_amount*0.8
    print(final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    final_amount=purchase_amount*0.9
    print(final_amount)
else:
    print('No discount applied')



