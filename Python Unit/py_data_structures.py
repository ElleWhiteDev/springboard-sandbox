# STR is immutable 

# len('string')
#


# ~~~~~~~~~~~~~~~~~~~~~~~~ LISTS ~~~~~~~~~~~~~~~~~~~~~~~~~
# mutable


# vegan_no_nos = ['eggs','meats','milk','fish','figs']

# pie_ingredients = ['flour','apples','sugar','eggs','salt']

# for food in pie_ingredients:
#     if food in vegan_no_nos:
#         print(f"OH NO, CANNOT EAT {food}! IT'S NOT VEGAN")
#     else:
#         print(f"YUM, I LOVE {food}!")

# vegan_no_nos[0] egggs
# vegan_no_nos[1] meats
# vegan_no_nos[2] milk
# vegan_no_nos[-1] figs
# vegan_no_nos[-2] fish
# vegan_no_nos[-3] milk

# vegan_no_nos[2] = 'dairy' vegan_no_nos = ['eggs', 'meats', 'dairy', 'fish', 'figs']


# vegan_no_nos[2:4:1]  ['milk', 'fish']
# vegan_no_nos[0:5:2]['eggs', 'milk', 'figs']
# vegan_no_nos[2:]  ['milk', 'fish', 'figs']
# vegan_no_nos[2:4] ['milk', 'fish']
# vegan_no_nos[:3] ['eggs', 'meats', 'milk'] 
# vegan_no_nos[::2] ['eggs', 'milk', 'figs']
# vegan_no_nos[3:0:-1] ['fish', 'milk', 'meats']
# vegan_no_nos[::-2] ['figs', 'milk', 'eggs']

# colors = ['red','orange','yellow']

# colors[0:1] = ['dark red', 'pink'] 
#   colors = ['dark red','pink','orange','yellow']

# colors[3:] = ['dark yellow','green','blue','purple'] 
#     colors = ['dark red', 'pink','orange','dark yellow','green','blue','purple']

# colors[5:] = []
#     colors = ['dark red', 'pink','orange','dark yellow','green'] 
# 
#colors = [::2] = ['LOL', 'LOL', 'LOL']  # needed
    # colors = ['LOL','pink','LOL','dark yellow','LOL']


# chickens.append()  takes only 1 arg
# chickens.copy()  shallow copy(will list nested but only points to org)
# chickens.count()
# chickens.extend()   adds items in arg to chickens will iterate over
#     string
# chickens.index()   only first instance of  if not in list, error
#     combine with in operator
# chickens.insert(2, 'carrie')    everything shifted right   inserting 
    # a list as an arg inserts it as a single list ele [3,4,5,['d','c']]
# chicken.pop()   no arg last default, arg = index
# chicken.reverse()
# chickens.sort()   can reverse=True  homogenous types req


# price = 3.50

# qty = 7

# print(f"Your total is ${price * qty}")

# str(5.6)

# 3 in nums   True
# '$' in price   False
# for char in str:
#     print(char)


# s.count()  case sensitive
# s.endswith('x')
# s.startswith('x')
# s.find('x')   first occurence  not found -1
# s.isdigit()    all digits
# "|".join(chickens)  'annabelle|butters|henry|lady gray'
# s.lower()/upper() 
# s.capitalize()
# s.isupper()/islower()
# s.replace(',','.',1)   default all  makes new str
# s.split(",")   new list elements seperated by arg
# s.splitlines()   each line is an element in list 
# s.strip()    removes leading and trailing space 


# ~~~~~~~~~~~~~~~~~~~~~~~~ DICT ~~~~~~~~~~~~~~~~~~~~~~~~~
# mutable 


# person = {
#     'first':'Henry McGerkin',
#     'age':'60',
#     'breed':'hooman'
# }

# stuff = {
#     True: 34,
#     100: 'awesome'
# }
#     key must be immutable type (no dictionary or list)


# 'breed' in person    True
# 'hooman' in person   False  keys, not values
# person['breed']     'hooman'
# person['name'] = 'numer 12'
#     if !present error
# person.get('weight')    none
# person.get('weight', '160lbs')    '160lbs'


# dict([True,0],[False,1])  {True:0, False:1}

# chicken = {
#     'name': 'Lady Gray',
#     'breed': 'Silkie',
#     'total_egg_count': 12,
#     'egg_chart': {
#         'M': True,
#         'T': True,
#         'W': True,
#         'TH': True,
#         'F': True,
#         'S': False,
#         'SU': True
#     },
#     'coop_mates': ['Butters','Stevie','Henry']
# }

# chicken.keys()    dict_keys(['name', 'breed', 'total_egg_count',
#                              'egg_chart', 'coop_mates'])

# for key in chicken.keys():    dict values obj iterable, not a list
#     print(key)

# for value in chicken.values():
#     print(value)

# for pair in chicken.items():
#     print(pair)

# for (k,v) in chicken.items():
#     print(k,'---->',v)


# d.popitem()   removes random key pair (?)
# {}.fromkeys('MTWHF', True)  {'M': True, 'T': True, 'W': True, 'H':
#                              True, 'F': True}


#~~~~~~~~~~~~~~~~~~~~~~~~ SETS ~~~~~~~~~~~~~~~~~~~~~~~~~
# immutable


# languages = {'ruby','python','javascript'}     set only immutable

# voted_languages = ['ruby','python','javascript','scala','python','python','scala']   list

# set(voted_languages)  {'ruby','python','javascript','scala'}  => set
# set('#$$%^&')  {'#','$','%','^','&'}

  
# moods = {'happy','sad','grumpy'}
# dwarfs = {'happy','grumpy','doc'}
# jobs = ['miner','doc','cleaner','cooker']

# moods | dwarfs    #union {'happy','sad','grumpy','doc'}
# moods & dwarfs    #intersection {'happy','grumpy'}
# moods - dwarfs    #difference {'sad'}
# dwarfs - moods                {'doc'}
# moods ^ dwarfs    #symmetric difference {'sad','doc'} 
# dwarfs.intersection(jobs)  {'doc'}   can't mix types w/ shorthand
# /////jobs.intersection)dwarf   job not set, can't call 


# for adj in dwarfs | moods | set(jobs):
#     print(adj)

# list(moods)
# list(dwarfs & moods)


# ~~~~~~~~~~~~~~~~~~~~~~~~ TUPLES ~~~~~~~~~~~~~~~~~~~~~~~~~
# immutable
# 

# tup = (3,)     <2 things it just evals val

# colors = ('red','yellow','green')

# board = {
#     (0,0): 'X',
#     (0,1):  None,
#     (0,2): 'O',
#     (1,0): 'X',
#     (1,1): 'O'
# }

# # board([0,2])   'O'

# # (1,2,1,3,1,4,1).count(1)   4
# (1,2,1,3,1,4,1).index(3)     3


# ~~~~~~~~~~~~~~~~~~~~~~~~ COMPREHENSIONS ~~~~~~~~~~~~~~~~~~~~~~~~~
#          ~~~~~~~~~~~~~~~~~~~ LISTS ~~~~~~~~~~~~~~~~~~~~
# mapping
# creates a new list

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# evens = []

# for num in nums:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)

# evens = [num for num in nums if num % 2 == 0]

#
# [num * 2 for num in nums]
# 
# new_list = []
# for num in nums:
#     new_list.append(num*2)

# ['HIIII' for num in nums] 
#                                     ['HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII',
#                                     'HIIII']


# [n * n for n in [2, 4, 6, 8]]   [4, 16, 36, 64]

# [char.upper() + '.' for char in 'lmfao']  ['L.', 'M.', 'F.', 'A.', 'O.']

# [num for num in range(10, 20)]  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]



# [[0 for y in range(3)] for x in range(3)]

# def gen_board(size, initial_val=None):
#     return [[initial_val for x in range(size)] for y in range(size)]

# chickens = [
#     {'name': 'Henry', 'sex': 'Rooster'},
#     {'name': 'Lady Gray', 'sex': 'Hen'},
#     {'name': 'Junior', 'sex': 'Rooster'},
#     {'name': 'Stevie Chicks', 'sex': 'Hen'},
#     {'name': 'Rocket', 'sex': 'Hen'},
#     {'name': 'Butters', 'sex': 'Rooster'},
# ]

# hens = [bird['name'] for bird in chickens if bird['sex'] == 'Hen']

# scores = [55,89,99,87,60,70,74,76,90,50,82]

#  # grades = ['PASS' for score in scores if score >= 70]
# grades = ['PASS' if score >= 70 else 'FAIL' for score in scores]

# def get_letter(ltr):
#     morse_lookup = { 'A':'.-', 'B':'-...',
#                     'C':'-.-.', 'D':'-..', 'E':'.',
#                     'F':'..-.', 'G':'--.', 'H':'....',
#                     'I':'..', 'J':'.---', 'K':'-.-',
#                     'L':'.-..', 'M':'--', 'N':'-.',
#                     'O':'---', 'P':'.--.', 'Q':'--.-',
#                     'R':'.-.', 'S':'...', 'T':'-',
#                     'U':'..-', 'V':'...-', 'W':'.--',
#                     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#                     '1':'.----', '2':'..---', '3':'...--',
#                     '4':'....-', '5':'.....', '6':'-....',
#                     '7':'--...', '8':'---..', '9':'----.',
#                     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#                     '?':'..--..', '/':'-..-.', '-':'-....-',
#                     '(':'-.--.', ')':'-.--.-'}
#     return morse_lookup.get(ltr.upper(), '')

# msg = [get_letter(char) for char in 'SOS']

# def get_morse_code(phrase):
#     return ' '.join([get_letter(char) for char in phrase])

#                       get_morse_code('hello')  '.... . .-.. .-.. ---'


#          ~~~~~~~~~~~~~~~~~~~ DICT ~~~~~~~~~~~~~~~~~~~~

# {day:0 for day in 'MTWRFSU'}  
#             {'M': 0, 'T': 0, 'W': 0, 'R': 0, 'F': 0, 'S': 0, 'U': 0}
# {num: num * num for num in range(1,10)}
#           {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# {num: num * num for num in range(1,10) if num % 2 == 0}


#          ~~~~~~~~~~~~~~~~~~~ SET ~~~~~~~~~~~~~~~~~~~~

# {char for char in 'abracadabra'} {'a', 'b', 'c', 'd', 'r'}

# {char for char in 'hello darkness my old friend' if char not in 'aeiou'}
