# # ~~~~~~~~~~~~~~~~~unpacking~~~~~~~~~~~~~~~~~~

# creaiting values from a list of values -- any iterable

# names = ['charlie','lucy']
# name1 , name2 = names   name1 = 'charlie'   name2 = 'lucy'

# sorted_score = [2400,2350,2100,1960]
# top_score, *scores = sorted_score  top_score = 2400   scores
#     = [2350,2100,1960]

# point = [40,50,20]
# x,y,z = point  x = 40   y = 50   z = 20

# colors_pairs = [['red','gree'n],['purple','orange']]
# ((primary1, secondary1),(primary2, secondary2)) = colors_pairs
#     primary1 = 'red'   secondary1 = 'green'   primary2 = 'purple'

# grades = {
#     'A': 12,
#     'B': 19,
#     'C': 30
# }

# for pair in grades.items():
#     print(pair)

# for (k,v) in grades.items():
#     print(k,v)



# ~~~~~~~~~~~~~~~~~packing/spreading~~~~~~~~~~~~~~~~~~


# iterables into iterables or fn  call


# nums = [2,4,6,8]
# [*nums]  #[2,4,6,8]
# [-2,0,*nums]  #[-2,0,2,4,6,8]

# odds = [1,3,5,7,9]
# [*odds, *nums]  #[1,3,5,7,9,2,4,6,8]

# [*hello] #['h','e','l','l','o']
# {*hello} #{'h','e','l','o'}

# rainfall = {'Jan': 2.5, 'Feb': 4.9}
# # {*rainfall}  #{'Jan','Feb'}
# # {'Dec': 0.5, **rainfall}  #{'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}
# {'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}  #{'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}
# {'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}   #{'Dec': 0.5, 'Jan': 2.5, 'Feb': 4.9}

# nums = [1,2,3,4,5,6,7,8,9]
# print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*nums) # 1 2 3 4 5 6 7 8 9



# ~~~~~~~~~~~~~~~~~~~~~~~error handling~~~~~~~~~~~~~~~~~~~~~~~~

# look before you leap
# easier to ask for forgiveness


# def get_days_alive(person):
#     try: 
#         days = person['age'] * 365
#         print(f'{person["name"]} have been alive for {days} days')
#     except KeyError as exc:
#         print(f'Missing key: {exc}')
#     except TypeError: 
#         print('Expected person to be a dict')
    


# ~~~~~~~~~~~~~raising errors~~~~~~~~~~~~~~~~~~

# def bounded_avg(nums):
#     for n in nums if n < 1 or n > 100:
#         raise ValueError('Outside bounds of 1-100')
    
#     return sum(nums) / len(nums)

# def handle_detail():

#     ages = [10,40,50,99,103,2,0]
#     try:
#         avg = bounded_avg(ages)
#         print('Average was', avg)

#     except ValueError as exc:
#         print('Invalid age in list of ages')



# ~~~~~~~~~~~~~~~~~doc strings/tests~~~~~~~~~~~~~~~~~~

# python3 -m doctest -v py_tools.py


# def bounded_avg(nums):
#     """
#     returns avg of list of nums (nums must be between 1-100)
    
#     >>> bounded_avg([2,4,6])
#     4.0

#     >>> bounded_avg([10,20,30,40,50])
#     30.0

#     >>> bounded_avg([2,4,500])
#     Traceback (most recent call last):
#     ...
#     ValueError: Outside bounds of 1-100
#     """
#     for n in nums:
#         if n < 1 or n > 100:
#             raise ValueError('Outside bounds of 1-100')

#     return sum(nums) / len(nums)


# ~~~~~~~~~~~~~~~~~~~~~~im/exporting~~~~~~~~~~~~~~~~~~~~~~~~

# standard library included

# import random                #all functions  random.choice()
# from random import choice    #spercific function(s)  choice()
# from random import choice as pick   #alias

# same idea with local files - call file and function

# import helper
# def make_person(name, fav_color):
#     return {
#         'name': name,
#         'fav_color': fav_color,
#         'birth_year': helper.get_ran_year(),
#         'birth_month': helper.get_ran_month()
#     }


# from forex_python.bitcoin import BtcConverter
# b = BtcConverter()
# b.get_latest_price('USD')     # 27347.9235


# ~~~~~~~~~~~~~~~~~~~~~~~Virtual Enviro~~~~~~~~~~~~~~~~~~~~~~~~

# python3 -m venv venv            #once to make
# source venv/bin/activate        #every time to use
# will use ver of py that was used to make venv
# don't have access to global pip pkgs
# deactive to exit

# pip3 freeze > requirements.txt    #makes list of used pkgs
# cat requirements.txt              #shows list of used pkgs  

# add venv/ to .gitignore           #don't want to push to git


# git clone http://path-to-project  #clone project
# cd project                        #go to project
# python3 -m venv venv              #make venv
# source venv/bin/activate          #activate venv
# pip3 install -r requirements.txt  #install pkgs


# ~~~~~~~~~~~~~~~~~~~~~~~~~files~~~~~~~~~~~~~~~~~~~~~~~~~~

# open(filepath, mode)    'r' = read, 'w' = write, 'a' = append

# file = open('test.txt')

# for line in file:
#     print('line = ', line)
    
# file.seek(0)    #go back to beginning of file
# all_text = file.read()

# file.close()


# file = open('test.txt', 'w')

# file.write("This is a new line.")
# file.write("So is this")

# file.close()


file = open('demo.txt', 'w')
file.write('I am a demo file.....promise')
file.close()

input_file = open('morse.txt', 'r')
output_file = open('translated.txt', 'w')
for line in input_file:
    output_file.write(line)

input_file.close()
output_file.close()

def get_english(phrase):
    letters = phrase.split('')
    return "".join([morse_to_letter(letter) for letter in letters])


