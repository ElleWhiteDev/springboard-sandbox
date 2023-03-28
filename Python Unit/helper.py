from random import randint, choice

def get_ran_year():
    return randint(1900, 2020)

def get_ran_month():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return choice(months)