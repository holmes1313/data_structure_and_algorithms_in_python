# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:12:02 2019

@author: z.chen7
"""

# Sets and Maps
"""
A list has ordering for its elements
A set doesn't have that but instead doesn't allow for repeated elements
"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangolore']}
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia']['China'] = ['Shanghai']

locations

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

sorted(locations['North America']['USA'])

asia_cities = []
for country in locations['Asia']:
    for city in locations['Asia'][country]:
        city_country = city + ' - ' + country
        asia_cities.append(city_country)
asia_cities
for city_country in sorted(asia_cities):
    print(city_country)
    



# Hashing
"""
The purpose of a hash function if to transform some value into one that can
be stored and retrieved easily.
value -> (hash function) -> hash value (index that can be stored and retrieved easily)

Hashing algorithm also known as a hash function is the calculation applied to
a key to transform it into a relatively small indexed number that corresponds
to a position in the hash table

There's no one perfect way to design a hash function.

There are times when a hash function will spit out the same hash value for two different inputs.
This situation is termed a collision.
There are two main ways to fix a collision:
    1. to change the value in your hash function, or to change the hash function
    completely, so you have more than enough slots to store all of your potential
    values.
    2. to change the structure of your array. Instead of storing one hash value in 
    each slot, you can store some type of lists that contains all values hashed
    at that spot. These lists are generally called buckets in this context.
    Rather than storing one value in each slot, you can store multiple values or
    a collection in each bucket.

Hash Maps
You can use the keys as iputs to a hash function, then store the key value pair
in the bucket of the hash value produced by the function.

String Keys
Hash value = (ASCII value of first letter * 100) +  (ASCII value of second letter)
ord() to get ASCII value of a letter
chr() to get the letter associated with an ASCII value.

Load factor = number of entries / number of buckets
"""

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000
        
    def store(self, string):
        """Input a string that's stored in the table"""
        index = self.calculate_hash_value(string)
        if self.table[index] != None:
            self.table[index].append(string)
        else:
            self.table[index] = [string]
        
        
    def lookup(self, string):
        """"
        Return the hash value if the string is already in the table.
        Return -1 otherwise"""
        index = self.calculate_hash_value(string)
        if self.table[index] != None:
            if string in self.table[index]:
                return index
        return -1
        
    def calculate_hash_value(self, string):
        """Helper function to calculate a hash value from a string"""
        hash_value = ord(string[0]) * 100 + ord(string[1])
        return hash_value
        

# Setup
hash_table = HashTable()

# Test calculate_hash_value
hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
hash_table.lookup('UDACIOUS')
