### Shapes Inscribed In A Circle ###

# With the users input of a radius value, the program will calculate the area and circumference
    # and then find either or both the square or triangle areas, side lengths, and perimeters within the given circle.


    # Some python arithmetic from math library
        ## pow(c,2) = pow(a,2)+pow(b,2)
        ##c = 2r and s = a = b
        ## Laws of sines: 2r = AB/sin(60) = AB/(math.sqrt(3)/2)
                    # AB is a side of equilateral triangle

import math

# this first while loop is to ensure the user can find as many values as needed 
value = 1
while value:

    # the userNum while loop is to ensure that the user enters a number
    userNum = 1
    while userNum:
        try:
            rad = float(input('\nEnter a radius value: ' ))
            userNum = 0
            continue

        except ValueError:
            print(f'\nType a number.')

    # after the userNum while loop, the program will calculate the circumference and area of the radius value entered by the user
    circumference = 2*math.pi*rad
    print(f'\nThe circumference of a circle with a radius of {rad} is {circumference:.4f} units.')

    area = math.pi*(pow(rad,2))
    print(f'\nThe area of a circle with a radius of {rad} is {area:.4f} units.')


    print('\nDo you want to calculate the largest square or the largest triangle that can fit in you circle?')

    # the shapeNum while loop is to ensure the user chooses on of the three options given
    shapeNum = 1
    while shapeNum:
        shape = input('\nEnter "sq" for square, "tri" for triangle, or "quit": ')
        if shape == 'sq':
            break
        elif shape == 'tri':
            break
        elif shape == 'quit':
            print(f'\nProgram Complete!\n')
            exit(0)
        else: print(f'\nTry Again!')

    # this count variable will be used later on as it will make sure the user is shown the values of a square and/or triangle within the circle unrepeating
    count = 1
    
    # the value2 while loop is for the choice specifically choosen by the user, square and/or triangle
    value2 = 1
    while value2:
        
        if shape == 'sq':

            #arithemtic for a square enclosed in the circle
            side_length = 2*(rad/math.sqrt(2))
            print(f'\nThe side length of the square is {side_length:.4f} units within the given circle.')

            # perimeter = 4*s
            perimeter = 4*side_length
            print(f'\nThe perimeter is equal to {perimeter:.4f} units.')

            # area = pow(s,2)
            area = pow(side_length,2)
            print(f'\nThe area of the square is equal to {area:.4f} units.')

            # count must be less than two, so that the user is asked if he/she would like to see the other option, which in this case is triangle
            if count < 2:
                changeShape = ''
                # this while loop is to ensure the user can input the correct answer, just in case a mis-type was made
                while changeShape != 'yes':
                    changeShape = input(f'\nDo you want to find the largest triangle that can fit (yes or no)?: ')
                    if changeShape == 'yes':
                        shape = 'tri'
                        count = count + 1
                    elif changeShape == 'no':
                        break
                    else: print(f'\nTry Again!')
                continue

            # this while loop is for the user to either change the radius and/or quit the program entirely, having the same format as the other while loops
            york = 1
            while york:
                answer = input('\nDo you want to change the radius? (Enter yes or no): ')
                if answer == 'yes':
                    value2 = 0
                    york = 0
                    continue
                elif answer == 'no':
                    answer = input('\nDo you want to quit? (Enter yes or no): ')
                    if answer == 'yes':
                        value = 0
                        value2 = 0
                        york = 0
                        print(f'\nProgram Complete!\n')
                    else: print(f'\nTry Again!')
                else: print(f'\nTry Again!')

        # this part of the over all code is very similar the one above except if the user chose tri as their first option, they would have the choice to see the sq too
        elif shape == 'tri':

            tri_side_length = rad*math.sqrt(3)
            print(f'\nThe side length of the triangle is {tri_side_length:.4f} units within the given circle.')
            
            tri_perimeter = tri_side_length*3
            print(f'\nThe perimeter of the triangle is {tri_perimeter:.4f} units.')
            
            tri_area = (math.sqrt(3)/4)*(pow(tri_side_length,2))
            print(f'\nThe area of the triangle is equal to {tri_area:.4f} units.')

            if count < 2:
                changeShape = ''
                while changeShape != 'yes':
                    changeShape = input(f'\nDo you want to find the largest square that can fit (yes or no)?: ')
                    if changeShape == 'yes':
                        shape = 'sq'
                        count = count + 1
                    elif changeShape == 'no':
                        break
                    else: print(f'\nTry Again!')
                continue

            york = 1
            while york:
                answer = input('\nDo you want to change the radius? (Enter yes or no): ')
                if answer == 'yes':
                    value2 = 0
                    york = 0
                    continue
                elif answer == 'no':
                    answer = input('\nDo you want to quit? (Enter yes or no): ')
                    if answer == 'yes':
                        value = 0
                        value2 = 0
                        york = 0
                        print(f'\nProgram Complete!\n')
                    else: print(f'\nTry Again!')
                else: print(f'\nTry Again!')

