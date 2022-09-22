#--------------------------------------------------
#----instagram : @ddos_attack_co ------------------
#--------------------------------------------------
import pyautogui as pg #pip install pyautogui
import time
#file=open("/home/ddos/Documents/cours_python/text_do_have_encode.txt","r")#If you want to write text that is in a file

text="This is Code For Send Massage"#message OR code
#for i in file:
#    text+=i
#time.sleep(5)
times=int(input("The number of times:"))
print("Starting in 5 seconds......")
time.sleep(5)
while times > 0:
    for x in range(len(text)):#It is written with letters
       pg.write(text[x])
       print("%d/%d"%(len(text)-1,x))
       time.sleep(0.5)#you hav fast writ time.sleep(0)
    pg.press("Enter")
    times-=1
print("This is Finch")
print("Follower of instagram : @ddos_attack_co")
