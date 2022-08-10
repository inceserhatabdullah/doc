#!/usr/bin/env python3

"""                 HASH
#* The Hash table data structure stores elements in key-value pairs where
#? Key: unique integer that is used for indexing the values
#? Value: data that are associated with keys.

                    Hash Collision
#* When the hash function generates the same index for multiple keys, there will be a conflict (what value to be stored in that index). This is called a hash collision.
#? Collision resolution by chaining
#? Open Addressing: Linear/Quadratic Probing and Double Hashing
#* https://www.programiz.com/dsa/hash-table
"""

# Python program to demonstrate working of HashTable 

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n):
        n += 2
        
    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

removeData(123)

print(hashTable)