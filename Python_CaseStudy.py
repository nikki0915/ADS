#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def roll_dice():
    min_value = 1
    max_value = 6

    while True:
        # Generate a random number between 1 and 6
        dice_roll = random.randint(min_value, max_value)
        print("You rolled:", dice_roll)

        roll_again = input("Do you want to roll the dice again? (yes/no): ")
        if roll_again.lower() != "yes" and roll_again.lower() != "y":
            break

roll_dice()


# In[ ]:




