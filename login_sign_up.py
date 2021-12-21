import json
import os
a={}
list=[]
c={}
d={}
file=open("userdetail.txt","w+")
user=int(input("1.login 2.sign_up"))
if user==1:
    user_name=input("enter a name")
    x = input("enter the  password:")
    if ('a' in x  or 'b' in x  or 'c' in x or 'd' in x or 'e' in x or 'f' in x or 'g' in x or 'h' in x or 'i' in x or 'j' in x or 'k' in x or 'l' in x or 'm' in x or 'n' in x or 'o' in x or 'p' in x or 'q' in x or 'r' in x or 's' in x or 't' in x or 'u' in x or 'v' in x or 'w' in x or 'x' in x or 'y' in x or 'z' in x ) and ('A' in x or 'B' in x or 'C' in x or 'D' in x or 'E' in x or 'F' in x or 'G' in x or 'H' in x or 'I' in x or 'J' in x or 'K' in x or 'L' in x or 'M' in x or 'N' in x or 'O ' in x or 'P' in x or 'Q' in x or 'R' in x or 'S' in x or 'T' in x  or 'U' in x or 'V' in x or 'W' in x or 'X' in x or 'Y' in x or 'Z'in x) and ('0'  in x or '1' in x or '2' in x or '3'in x or '4' in x or '5' in x or  '6' in x or '7' in x or '8' in x or '9' in x) and ('@'in x or '#'in x or '$'in x):
        print("congratets",user_name,"you login succesfullly!!!")
    else:
        print("wrong password,plz try again")
if user==2:
    Discription=input("what you like")
    user_name=input("enter a name")
    DOB=(input("enter a date of birth"))
    gender=input("enter a gender")
    Hobbies=input("enter a hobbies")
    x=input("enter a password")
    if ('a' in x  or 'b' in x  or 'c' in x or 'd' in x or 'e' in x or 'f' in x or 'g' in x or 'h' in x or 'i' in x or 'j' in x or 'k' in x or 'l' in x or 'm' in x or 'n' in x or 'o' in x or 'p' in x or 'q' in x or 'r' in x or 's' in x or 't' in x or 'u' in x or 'v' in x or 'w' in x or 'x' in x or 'y' in x or 'z' in x ) and ('A' in x or 'B' in x or 'C' in x or 'D' in x or 'E' in x or 'F' in x or 'G' in x or 'H' in x or 'I' in x or 'J' in x or 'K' in x or 'L' in x or 'M' in x or 'N' in x or 'O ' in x or 'P' in x or 'Q' in x or 'R' in x or 'S' in x or 'T' in x  or 'U' in x or 'V' in x or 'W' in x or 'X' in x or 'Y' in x or 'Z'in x) and ('0'  in x or '1' in x or '2' in x or '3'in x or '4' in x or '5' in x or  '6' in x or '7' in x or '8' in x or '9' in x) and ('@'in x or '#'in x or '$'in x):
        confirm_password=input("enter a confirm password")
        if x==confirm_password:
            # if os.stat("userdetail.json").st_size==0:
                print("congrates", user_name,"you are signed up succesfully")
                a["Discription"]=Discription
                a["D_O_B"]=DOB
                a["Gender"]=gender
                a["Hobbies"]=Hobbies
                d["user_name"]=user_name
                d["password"]=x
                d["profile"]=a
                f=json.dumps(d,indent=4)
                f1=open("Anjali.json","a")
                f1.writelines(f)
                f1.write("\n")
                f1.close()
        else:
            print("both password are not same plz try agin ")
    else:
        print("At least password should contain small latter,capital latter and one special character and one number")
    
    