# Generates random number generator
import random

# Generates userinterface
import pyautogui

# Need to store all letters and numbers.
chars = "abcdefghijklmnopqrstuvwxyz0123456789";

# transfer set of characters to list of characters.
allchar = list(chars)

# Message shows up on graphic user interface.
pwd = pyautogui.password("Enter your password")

# Need someplace to store the password.
sample_pwd = ""

""" So in this section its important to understand that we are getting the password
    from the user interface and are cross-referencing with the sample_pwd. Notice that 
    sample_pwd is "" because we want our loop to run this will cause the loop to begin 
    and make sure that there is a password entered.
"""
while(sample_pwd != pwd):
    
    # Generate random choices
    sample_pwd = random.choices(allchar, k=len(pwd))
    
    print("<========" + str(sample_pwd) + "========>")
    
    # Check the random choice.
    if (sample_pwd == list(pwd)):
        print("The Password is " + "".join(sample_pwd))
        break   
    