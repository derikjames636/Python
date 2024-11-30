


def right_triangle_side():
    a = int(input('Enter the side 1 '))
    b = int(input('Enter side 2 '))
    c = int(input('Enter side 3 '))
    sides=[a,b,c]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        print('The given sides of part of right triangle')
    else:
      print('the given sides are not part of right triangle ')
right_triangle_side()

