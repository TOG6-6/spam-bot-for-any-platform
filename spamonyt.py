import string
import pyautogui
import time
import sys
import os
try: #what i am doing is i dont know if everyone will have the config file with them, so i am trying to import the config file, but if it aint there, just ignore
    import config
    from config import epicwords
except:
    pass

def thegodpart():
    print("""
    ████████╗░█████╗░░██████╗░░█████╗░  ░██████╗██████╗░░█████╗░███╗░░░███╗  ██████╗░░█████╗░████████╗
    ╚══██╔══╝██╔══██╗██╔════╝░██╔═══╝░  ██╔════╝██╔══██╗██╔══██╗████╗░████║  ██╔══██╗██╔══██╗╚══██╔══╝
    ░░░██║░░░██║░░██║██║░░██╗░██████╗░  ╚█████╗░██████╔╝███████║██╔████╔██║  ██████╦╝██║░░██║░░░██║░░░
    ░░░██║░░░██║░░██║██║░░╚██╗██╔══██╗  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║  ██╔══██╗██║░░██║░░░██║░░░
    ░░░██║░░░╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║  ██████╦╝╚█████╔╝░░░██║░░░
    ░░░╚═╝░░░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
    NOTE: MAKE SURE NOT TO GO OVER 50 AT A TIME!
    CREDITS TO TOG AND YT SUBS!
    """)

    print("[1] For Single Phrase!")
    print("[2] For Multiple Phrases!")
    print("[3] To Close The Program!")
    a = int(input("[?]: "))
    if a == 1:
        k = open('beemovie.txt', 'r')
        count = int(input("How Many Times Do You Want To Spam?: "))
        print("You Have 5 Seconds, Place The Mouse Cursor On The Chat Box Where You Type!")
        time.sleep(5) #making the program do nothing for 5 seconds: #for i in range is basically telling python how many times something should happen, for example here spamming something count number of times
        for word in k:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            time.sleep(7)
        print("Spammed " + k + " " + str(count) + " times!")
        thegodpart()

    elif a == 2:
        print("Update The Config File, And Then Continue!")
        print("Press Enter Once Done!")
        input("")
        l = int(input("How Many Times Do You Want To Spam The Message?: "))
        print("You Have 5 Seconds, Place The Mouse Cursor On The Chat Box Where You Type!")
        time.sleep(5)
        for a in range(l):
            for i in epicwords:
                pyautogui.typewrite(i)
                pyautogui.press("enter")
                time.sleep(0.1)
        print("Spammed Everything In Config File " + str(l) + " times!")
        thegodpart()

    elif a == 3:
        print("")

    else:
        print("Invalid Choice! Try Again!")
        thegodpart()

thegodpart()

#please make sure to join my server if you have any issues itll be my pleasure to help fix it :-)
#discord server in link :-)
#if you need the exe or app will be in the discord server also :-)