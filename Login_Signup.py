import json
out_dict={}
dict1={}
list1=[]
print('\n**********|->>> welcome in my websites <<<-|************\n')
print('\t\t>>>> 1.SIGNUP <<<< \n  \t\t>>>> 2.Login <<<< ')
user_ask = input("Would you want to login/signup \U0001f607 => ")
def signup():
    print("************|welcme to signup Page|*************\n")
    username = input("Enter your username \U0001f607 => " )
    phone_no = input("Enter your phone_number \U0001f607 => " )
    email = input("Enter your email \U0001f607 => ")
    password = input("Enter your password \U0001f607 => " )
    l, u, p, d = 0, 0, 0, 0
    for i in password:
        if (i.islower()):
            l+=1      
        if (i.isupper()):
            u+=1     
        if (i.isdigit()):
            d+=1           
        if(i=='@' or i=='$' or i=='_' or i=="#" ):
            p+=1           
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        print("\nYour Password is Valid \U0001f607")
        password2=input("Enter your confirm password \U0001f607 => ")
        if password==password2:
            print("\n****|--> \U0001f607 You Signed Up Succsefully \U0001f607 <--|****")
        else:
            print("\n****|--> \U0001f608 both password are wrong \U0001f608 <--|****")
    else:
        print("invalid")
    out_dict["user_name"]=username
    out_dict["user_phone_no."]=phone_no
    out_dict["user_email"]=email
    out_dict["user_password"]=password
    list1.append(out_dict)
    dict1["userinfo"]=list1
    try:
        with open("userdetails.json","r+")as f:
            j=f.read()
            fs=json.loads(j)
            for i in fs:
                if i == "userinfo":
                    s=fs[i]
                    s.append(out_dict.copy())
                    dict1["userinfo"]=s
                    json.dumps(dict1,f,indent=4)
                    f.close()
    except:
        with open("userdetails.json","w") as fil:
            fil.write(json.dumps(dict1,indent=4))
def login():
    print("************|welcme to login Page|*************\n")
    i=0
    k=0
    while 1: 
        username = input("Enter your email for login \U0001f607 => ")
        password = input("Enter your password for login \U0001f607 => ")
        with open("userdetails.json",'r') as fd:
            users_data = json.load(fd)
        for dics in users_data['userinfo']:
            if dics['user_email']==username and dics['user_password']==password:
                print()
                print("\U0001f607\U0001f607|succesfully logged IN|\U0001f607\U0001f607\n")
                k = 1 
                break
        if k == 1:
            break    
        elif i == 3:
            print("\n****|-->\U0001f608\U0001f608 User Not found \U0001f608\U0001f608<--|****\n")
            break
        else:
            print("\n****|--> \U0001f608\U0001f608<---You write the wrong password Please try again.\U0001f608\U0001f608 <--|****\n")
        i+=1
    print("****|-->\U0001f607\U0001f607\U0001f607 Thanks for visit in my website \U0001f607\U0001f607\U0001f607<--|****")
def main(user):
    if user=="1" or user=="signup":
        signup()
        b=input("\nDo you want login(1) or Exit(2) \U0001f607 => ")
        if b == "1":
            login()
        else:
            print("****|-->\U0001f607\U0001f607\U0001f607 Thanks for visit in my website \U0001f607\U0001f607\U0001f607<--|****")
    elif  user=="2" or user=='login':
        login()
    else:
        print("****|-->\U0001f608\U0001f608 unvalid operation \U0001f608\U0001f608<--|****")
main(user_ask)

  
