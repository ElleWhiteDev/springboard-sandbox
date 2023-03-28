# num = 0

# while num <= 100:
#     if num == 50:
#         break
#     print(num)
#     num += 10

# print('all done')


# target = 37
# guess = None

# while guess != target:
#     guess = input('please enter a guess...')
#     if guess == 'q' or guess == 'quit':
#         break
#     guess = int(guess)
    

# print('see you next time')


# colors = ['red', 'orange', 'yellow', 'green']

# for color in colors:
#     print(color)

# for char in "ABCDEFGHIJKLMNOQRSTUVWXYZ":
#     print(char)


# for num in "abcde":
#     print('hello') 
#     # iterates hello 5x

# for n in range(10):
#     print(n)
#     # prints 0-9

# range(10) only make obj range(0,9)
# list(range(10)) makes array [0,1,2,...9]
# list(range(5,10)) [5,6,7,8,9]
# list(range(1,10,2)) [1,3,5,7,9]
# list(range(10,0,-1)) [10,9,8,..1]
# list('hello')  ['h','e','l','l','o']


# def greet(person):
#     return f'Hello there, {person}'

# def divide(a,b):
#     if type(a) is int and type(b) is int:
#         return a/b
#     return 'a and b must be intigers'


# def three_things(a,b,c):
#     print('hi~')

# def send_email(to_email, from_email, subject, body):
#     email = f'''
#         to: {to_email}
#         from: {from_email}
#         subject: {subject}
#         -----------------
#         body: {body}
#     '''
#     print(email)

# send_email('mum@cheri.com', 'me@loops.com', 'howdy', 'I just wanted to say HeLlO~!')

# send_email(subject='howdy', from_email='me@loppydoops.com', to_email= 'mum@cheri.com', body='Slorp from another dimension')


# def power(num, power=2):
#     return num ** power

# result = power(4)
# print(result)