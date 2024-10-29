string_1=input('Enter a string')
vowels='aeiouAEIOU'
vowels_count=0
consonents_count=0
for char in string_1:
    if char in vowels:
        vowels_count+=1
    else :
       consonents_count+=1
print(f'number of characters in the given string' , {vowels_count})
print(f'the number of consonents in the given string' , {consonents_count})
