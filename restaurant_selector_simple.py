#### Restaurant Selector ####

# In this program the user will answer three questions regarding a parties dietary resrictions. The program
    # will then output a response of which restaurants are best for the party.

print(f'For the following questions, enter yes or no: ')
vegetarian = input('Is anyone of this party a vegetarian? ').lower()
vegan = input('Is anyone of this party a vegan? ').lower()
gluten_free = input('Is anyone of this party a gluten free? ').lower()

print()

if vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print('Your restaurant choices are as follows: ')
    print('Wood Fired Pizza Wine Bar\nVillaggio’s Ristorante Italiano\nFarmacy Vegan Kitchen')
    
elif vegan == 'yes' and vegetarian == 'no' and gluten_free == 'no':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen')
    
elif gluten_free == 'yes' and vegan == 'no' and vegetarian == 'no':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen\nWood Fired Pizza Wine Bar')
    
elif vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'no':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen')

elif vegan == 'yes' and gluten_free == 'yes' and vegetarian == 'no':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen')

elif gluten_free == 'yes' and vegetarian == 'yes' and vegan == 'no':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen\nWood Fired Pizza Wine Bar')
    
elif vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print('Your restaurant choices are as follows: ')
    print('Farmacy Vegan Kitchen')
    
else:
    print('Your restaurant choices are as follows: ')
    print('Wood Fired Pizza Wine Bar\nVillaggio’s Ristorante Italiano\nFarmacy Vegan Kitchen\nCouncil Oak Steaks and Seafood')
