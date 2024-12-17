import colorama
from colorama import Fore

from time import sleep

w=input("enter your weight in kgs -> ")
h=input("enter your height in meters -> ")
age=input("enter your age -> ")
age=float(age)
w=float(w)
h=float(h)
hcm=h/100
bmi=w/h**2
bmr=10*w+6.25*hcm-5*age+5
print(f"bmi {round(bmi)}")
print(f"bmr {bmr}")
if bmi <18:
    print("underweight")
elif bmi >18  and bmi <25 :
    print("normal")
elif bmi >25  and bmi <30 :
    print("overweight")
elif bmi >30  and bmi <40 :
    print("obese")
elif  bmi >40 :
    print("extermly obese")
print("18 and less is under weight. 18 to 25 is normal, 25 to 30 is overweight, 30 to 40 is obese ,And over 40 extermly obese")
map=[[0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
     [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]]

def render_map():

    for i in range(len(map)):
        for x in range(len(map[i])):
            if map[i][x] ==0:
             print("   ",end="")

            if map[i][x] ==1:
             
             print(f"{Fore.GREEN} | ",end="")

            if map[i][x] ==2:
             
             print(f"{Fore.BLUE} . ",end="")

             
        print("")
        


    


        
    
   
      
    
render_map()

     