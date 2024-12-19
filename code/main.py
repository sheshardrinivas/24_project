import colorama
from colorama import Fore
from random import randint
from time import sleep
import json
def string_print(string_,time_,color_):
    print(" ")
    for i in range(len(string_)):
       print(f"{color_}{string_[i]}",end="")
       sleep(time_)
print('\033c', end='')
w=input("enter your weight in kgs -> ")
print(" ")
h=input("enter your height in meters -> ")
print(" ")
age=input("enter your age -> ")
print(" ")
act=input("enter how active your are  -> ")
print(" ")
age=float(age)
act=str(act)
w=float(w)
h=float(h)
hcm=h/100
bmi=w/h**2
bmr=10*w+6.25*hcm-5*age+5
status=""
act1=""
print(" ")
print(f"bmi {round(bmi)}")
print(" ")

if bmi <18.5:
    print("underweight")
    status="underweight"
elif bmi >18.5  and bmi <25 :
    print("normal")
    status="normal"
elif bmi >25  and bmi <30 :
    print("overweight")
    status="overweight"
elif bmi >30  and bmi <40 :
    print("obese")
    status="obese"
elif  bmi >40 :
    print("extermly obese")
    status="extermly obese"
if act=="no":
    bmr=bmr*1.2
    act=act1
if act=="light":
    bmr=bmr*1.375
    act=act1
if act=="normal":
    bmr=bmr*1.55
    act=act1
if act=="bit more":
    bmr=bmr*1.725
    act=act1
if act=="very more":
    bmr=bmr*1.725
    act=act1


print(f"bmr {bmr}")

print(" ")
print("18 and less is under weight. 18 to 25 is normal, 25 to 30 is overweight, 30 to 40 is obese ,And over 40 extermly obese")
print(" ")
print(" ")
map=[[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
     [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,0,0,1],
     [1,0,0,0,0,0,0,0,0,0,0,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,0,0,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,0,0,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,0,0,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,0,0,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,0,0,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,3,3,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,3,3,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,0,0,3,3,0,4,4,0,5,5,0,6,6,0,7,7,0,0,1],
     [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]]

def render_map():

    for i in range(len(map)):
        for x in range(len(map[i])):
            
            if map[i][x] ==0:
              print("   ",end="")
              

            if map[i][x] ==1:
             
              print(f"{Fore.WHITE} | ",end="")


            if map[i][x] ==2:
             
              print(f"{Fore.WHITE} . ",end="")
            if map[i][x] ==3:
             
              print(f"{Fore.LIGHTYELLOW_EX} - ",end="")
            if map[i][x] ==4:
             
              print(f"{Fore.GREEN} - ",end="")
            if map[i][x] ==5:
             
              print(f"{Fore.YELLOW} - ",end="")
            if map[i][x] ==6:
             
              print(f"{Fore.LIGHTRED_EX} - ",end="")
            if map[i][x] ==7:
             
              print(f"{Fore.RED} - ",end="")

            


        print("")
        sleep(0.04)
        
        


    


        
    
   
      
    
render_map()
print("  ") 
print(" ",end=" ") 
print(f"{Fore.LIGHTYELLOW_EX}underweight",end=" ")
print(f"{Fore.GREEN}normal",end=" ")
print(f"{Fore.YELLOW}overweight",end=" ")
print(f"{Fore.LIGHTRED_EX}obese",end=" ")
print(f"{Fore.RED}extermly obese",end=" ")

print(" ") 
print("  ") 
print(" ",end=" ") 
print(f"{Fore.LIGHTYELLOW_EX}less than 18.5",end=",")
print(f"{Fore.GREEN}18.5 to 25",end=",")
print(f"{Fore.YELLOW}25 to 30",end=",")
print(f"{Fore.LIGHTRED_EX}30 to 40",end=",")
print(f"{Fore.RED}more than 40",end=" ")

print(" ") 
print(" ") 
with open('code/test.json', 'r') as file:
            t1 = json.load(file)
if status == "underweight":

    string_print(t1["treatment1"][0],0.2,Fore.LIGHTYELLOW_EX)
    print(" ") 
    string_print(t1["treatment1"][1],0.2,Fore.LIGHTYELLOW_EX)
    print(" ") 
    string_print(t1["treatment1"][2],0.2,Fore.LIGHTYELLOW_EX)
    print(" ") 
    string_print(t1["treatment1"][3],0.2,Fore.LIGHTYELLOW_EX)
    print(" ") 
    print(" ") 
   

     