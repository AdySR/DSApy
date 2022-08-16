"""
Problem: We want to WAP to identify the position of card from a stack of cards. 
> A list of numbers provided in an array
> query: a number whoes position we want to find out
"""

import re
from turtle import pos, position


def locate_cards(cards,query):
    position=0
    while(position<len(cards)):
        if cards[position]==query:
            return position
        position+=1

        if position==len(cards):
            return -1


cards = [13,11,33,5,33,5,211,52,433,5,3,5,7,8,5,4,33,3]
query =7

print(locate_cards(cards,query))