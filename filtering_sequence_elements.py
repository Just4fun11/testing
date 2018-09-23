'''
Easiest way to filter data in a sequence is to use list comprehension
'''

#Example 1:
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
myList = [1,4,-5,10,-7,2,3,-1]
greater = [n for n in myList if n > 0]
less = [n for n in myList if n < 0]
print(greater)
print('~~')
print(less)

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
'''
filter() is used as an iterator so by using list() in front we create a list of results
'''
print(ivals)

#Ex 3:
import math
x = [math.sqrt(n) for n in myList if n>0]
print(x)


#Ex 4:
'''
Filtering with itertools.compress().. This takes an iterable and an accompanying boolean selector sequence as an input 
It then gives the output as all of the items in the iterable where the corresponding element in the selector is True
~~~ USEFUL WHEN TRYING TO APPLY THE RESULTS OF FILTERING ONE SEQUENCE TO ANOTHER RELATED SEQUENCE
'''

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
listComprehension = list(compress(addresses, more5))
print(listComprehension)



#Ex 5:
'''
Making a dictionary that is a subset of another dictionary
'''

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
# ALTERNATIVE p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names }
print (p2)
# ALTERNATIVE p2 = { key:prices[key] for key in prices.keys() & tech_names }
