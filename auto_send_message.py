#--------------------------------------------------
#----instagram : @ddos_attack_co ------------------
#--------------------------------------------------
import pyautogui as pg #pip install pyautogui
import time
from click import clear
clear()
#file=open("/home/ddos/Documents/cours_python/text_do_have_encode.txt","r")#If you want to write text that is in a file
lang=input("Do you want to type in letters|L| or copy paste |C|? : ").upper()
if lang == "L":
    lang=False
elif lang == "C":
    lang = True
text=input("Enter Your Message: ").strip()  #message OR code
#for i in file:
#    text+=i
#time.sleep(5)
times=int(input("The number of times:"))
print("Starting in 5 seconds......")
time.sleep(5)
while times > 0:
    if lang==True:
        pg.write(text)
        pg.press("Enter")
        times-=1
        print(f"I stayed {times} times")
        time.sleep(5)
    else:
        for x in range(len(text)):#It is written with letters 
            pg.write(text[x])
            time.sleep(0.15)#you hav fast writ time.sleep(0)
        pg.press("Enter")
        times-=1
        print(f"I stayed {times} times")
        time.sleep(3)

print("This is Finch")
print("Follower of instagram : @ddos_attack_co")
