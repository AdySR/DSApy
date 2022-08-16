"""
Problem: We want to WAP to identify the position of card from a stack of cards. 
> A list of numbers provided in an array
> query: a number whoes position we want to find out
"""

import re
from turtle import pos, position
from adatix_array import Adatix_Array


def locate_cards_BinarySearch(cards,query):
    low =0
    high = len(cards) -1


    while low<high:
        mid_element_index = (low+high)//2
        mid_element = cards[mid_element_index]
        print("low: ",low, "High: ",high, "mid: ",mid_element)

        if mid_element == query:
            return mid_element
        elif mid_element > query:
            high = mid_element-1
        elif mid_element < query:
            low = mid_element + 1
    return -1




cards = [13,11,33,5,33,5,211,52,433,5,3,5,7,8,5,4,33,3,4]
cards = Adatix_Array.array_sort_asc(cards)
query =33
print("Array: ",cards)
print("output:  ",locate_cards_BinarySearch(cards,query))