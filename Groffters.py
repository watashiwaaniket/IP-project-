
#Program version 0.5
#Ready for the Use
#Login function is coded
#Login function properly now
#Register function is complete
#Admin login is complete
#Admin control is fully developed

"""
plans:

will try to add cart system which requres table joints
try to make the program more user friendly! :)
peace ~('='~(/)

"""

def index():
      #importing necessary modules.
      import pandas as pd
      import numpy as np
      import mysql.connector as root
      mycon=root.connect(host="localhost",user="root",password="tiger",database="Groffters",charset="utf8")
      cursor=mycon.cursor(dictionary="true")
      """
      Currently in Development:
      """
      #query for admintable
      admins="create table if not exists admin (ID int not null,name varchar(20),passwd varchar(16) not null);"
      cursor.execute(admins)
      mycon.commit()


      #query for grocerytable
      grocery="create table if not exists grocery (item_ID int not null unique,item_name varchar(20),item_value int(250),item_cost double);"
      cursor.execute(grocery)


      #query for logintable
      login_table="create table if not exists login (Name varchar(30) not null,User_name varchar(15) unique,Passwd varchar(16) not null,Phone varchar(13),email_ID varchar(45))"
      cursor.execute(login_table)

      






      def buywin():
            print("="*55)
            print(" "*33,"Buy Menu.")
            print("="*55)
            print("Payment option:")
            print("i. Card")
            print("ii. COD")
            print("="*55)

            input1=int(input("[1,2]: "))

            if input1 == 1 :
                  print("="*55)
                  print("Card Payment")
                  print("="*55)
                  address=input("Address: ")
                  cno=input("Card Details: ")
                  cvv=input("Input CVV: ")
                  print("="*55)



                  print("Payment Successful!")
                  print("Thankyou for shopping with Groffters!!")


            elif input1 == 2:
                  print("="*55)
                  print("Card Payment")
                  print("="*55)
                  address=input("Address: ")
                  
                  print("="*55)



                  print("Order on it's way.")
                  print("Thankyou for shopping with Groffters!!")




            
            


      #function containing table values.
      def installation():
            adminf="insert into admin values (1,'ANIKET','12345678');"
            
            adminf2="insert into admin values (3,'ABISKAR','12345678');"
            item1="insert into grocery values (101,'Horlicks',200,73.2)"
            item2="insert into grocery values (102,'Coffee',220,49.5)"
            item3="insert into grocery values (103,'Cornflakes',240,59.0)"
            item4="insert into grocery values (104,'Boost',240,59.0)"
            item5="insert into grocery values (105,'Rajma',240,80.0)"
            item6="insert into grocery values (106,'Sugar',240,40.0)"
            item7="insert into grocery values (107,'Sunflower Oil',240,59.0)"
            item8="insert into grocery values (108,'Peanut',240,40.0)"
            item9="insert into grocery values (109,'Soya Buddy',240,79.0)"
            item10="insert into grocery values (110,'Rice',240,69.0)"
            item11="insert into grocery values (111,'Moong Daal',240,73.0)"
            item12="insert into grocery values (112,'Garam Masala',240,23.0)"
            cursor.execute(adminf)
            
            cursor.execute(adminf2)
            cursor.execute(item1)
            cursor.execute(item2)
            cursor.execute(item3)
            cursor.execute(item4)
            cursor.execute(item5)
            cursor.execute(item6)
            cursor.execute(item7)
            cursor.execute(item8)
            cursor.execute(item9)
            cursor.execute(item10)
            cursor.execute(item11)
            cursor.execute(item12)
            mycon.commit()
            print("Do you wanna continue?")
            input9=input("==> ")
            if input9 == 'y':
                  home()
            else:
                  print("See you soon ;)")


      #login function
      def login():
            print("""

 
                  """*10)
            print("="*55)
            print(" "*38,"Login")
            print("="*55)
            username=input("User Name: ") #Username
            password=input("Password: ") #password
            print("="*55)
            

            if username == "" or password == "": #this will pop up if any of the above feild is left empty.
                  print("Please complete the required field!")
                  


            #query to check if password and username is correct
            cursor.execute("select * from login where User_name = '{}' and passwd = '{}'".format(username,password))
            
            if cursor.fetchone() is not None: #opening the buying menu
                  
                  print("-"*55)
                  print(" "*35,"Welcome",username)
                  print("-"*55)
                  print()
                  print(" "*38,"i.Buy")
                  print(" "*36,"ii.Edit Profile")
                  print("-"*55)
                  choice3=int(input("Select your choice [1/2]: "))
                  print("-"*55)

                  if choice3 ==1:
                        
                        print("Proceed to buy: [y/n]")
                        choice=input("==> ")
                        if choice == "y" or choice == "Y":               #buying one item
                              
                              
                              show_table="select * from grocery"
                              cursor.execute(show_table)
                              data=cursor.fetchall()
                              print("="*55)
                              print(" "*28,"Current List")
                              print("="*55)
                              for df in data:                                    
                                    print(df)
                              print("="*55)

                              print("="*55)
                              print(" "*30,"What you wanna buy?")
                              print("="*55)

                              a1=input("==>")

                              #grocery (item_ID int not null unique,item_name varchar(20),item_value int(250),item_cost double)
                              #grocery table for reference
                              ID="select item_ID, item_name,item_cost from grocery where item_ID = '%s'"%(a1)
                              cursor.execute(ID)
                              data=cursor.fetchall()
                              df1=pd.DataFrame(data,["1"],["Product ID","Product Name","Cost"])
                              print("="*55)
                              print(df1)
                              print("="*55)
                              print("Proceed to Buy [y/n]")
                              print("="*55)
                              buy=input("==>")
                              print("="*55)


                              if buy == 'y' or buy == 'Y':
                                    buywin()

                              else:
                                    print("="*55)
                                    print("Go back to shopping? [y/n]")
                                    print("="*55)
                                    input1=input("==>")

                                    if input1 == "y" or input1 == "Y":
                                          login()

                                    else:
                                          print("See you soon :)")
                                          

                        else:
                              print("="*55)
                              print(" "*20,"Go back [y/n]")
                              print("="*55)
                              input2=input("==>")
                              print("="*55)


                              if input2 == "y" or input2 =="Y" :
                                    index()

                              else:
                                    print("See you soon :)")
                                    

                              


                              
                              



      #reference to login table to code the following program
      #login (Name varchar(30) not null,User_name varchar(15) unique,Passwd varchar(16) not null,Phone varchar(13),email_ID varchar(20)
                  elif choice3 == 2:

                        #this menu will deal with changing values like password, username,etc
                        print("="*100)
                        print("i.Change username.")
                        print("ii.Change password.")
                        print("iii.Change phone.")
                        print("iv.Change email.")
                        print("="*100)

                        
                        choice=int(input("Select your choice [1/2/3/4]: "))
                        print("="*100)

                        if choice == 1: #to change username
                              newname=input("Enter new username: ")
                              email=input("Enter your email id: ")

                  
                              query="update login set User_name = '%s' where email_ID = '%s'"%(newname,email)
                              cursor.execute(query)
                              mycon.commit()
                              login()
            
                        elif choice == 2: #to change password
                              newpass=input("Enter new password: ")
                              email=input("Enter your email id: ")

                  
                              query="update login set Passwd = '%s' where email_ID = '%s'"%(newpass,email)
                              cursor.execute(query)
                              mycon.commit()
                              login()
 
                        elif choice == 3: #to change phone number
                              newphone=input("Enter new Phone number: ")
                              email=input("Enter your email id: ")

                  
                              query="update login set Phone = '%s' where email_ID = '%s'"%(newphone,email)
                              cursor.execute(query)
                              mycon.commit()
                              login()

                        elif choice == 4: #to change email ID
                              newemail=input("Enter new Email: ")
                              passwd=input("Enter your Passwd: ")

                  
                              query="update login set email_ID = '%s' where Passwd = '%s'"%(newemail,passwd)
                              cursor.execute(query)
                              mycon.commit()
                              login()


            else:
                  print("No profile exist with the name",username)
                  print("No profile? Register yourself for Free!!") #Ah! I love this part...
                  

            

      def register():
            print("""

                  """*20)
            #this place deals with registration of new customers!!!
            mycon=root.connect(host="localhost",user="root",password="tiger",database="test",charset="utf8")
            cursor=mycon.cursor()
            print("-"*55)
            print(" "*30,"Registration.")
            print("-"*55)
            
            name=input("Your Name: ")
            user_name=input("User Name: ")
            passwrd=input("Password: ")
            phno=int(input("Phone Number: "))
            email=input("e-mail address: ")


            #query to  add values into login table.
            addition="insert into login values ('{}','{}','{}',{},'{}')".format(name,user_name,passwrd,phno,email)
            cursor.execute(addition)
            mycon.commit()

            
            print("-"*55)
            print("Go to login screen [y/n].")
            conte=input("==>")
            print("-"*55)
            if conte == "y":
                  login()

      
      
                     
      
      
      def Adminlogin(event=None):
            print("""


                  """*10)

      #Sorry can't tell, only for Admins.
      #lol just kidding
      #this area deals with admin login and basically it's the brain of the whole program.
            print("-"*55)
            print(" "*35,"Admin Login")
            print("-"*55)
            user=input("User Name: ")
            passwd=input("Password: ")
            print("-"*55)

            if user == "" or passwd == "":
                  print("Please complete the required field!")
            else:
                  cursor.execute("select * from admin where name = '{}' and passwd = '{}'".format(user,passwd))
            
                  if cursor.fetchone() is not None: #checking if the password and username are correct.
                        print("="*55)
                        print(" "*35,"Welcome",user)
                        print("="*55)
                        print()
                        print(" "*38,"i.Add item")                    #adding item
                        print(" "*36,"ii.Remove item")              #remove item
                        print(" "*36,"iii.Update price")             #changing price           
                        print(" "*36,"iv.Update value")            #change value
                        print(" "*37,"v.Current list")
                        print("="*55)
                        choice2=int(input("Select your choice [1/2/3/4/5]: "))
                        print("="*55)

                                        

                        if choice2 ==1 :
                              print("="*55)
                              show_table="select * from grocery"  #query to select whole grocery table
                              cursor.execute(show_table)
                              data=cursor.fetchall()              #it collects the table data  
                              print("="*55)
                              print(" "*28,"Current List")
                              print("="*55)
                              for df in data:               #it prints the grocery table
                                    print(df)
                              print("="*55)
                              item_ID=int(input("Item code (unique): "))
                              item_name=input("Item name: ")
                              item_value=int(input("How many items: "))
                              item_cost=input("Item cost: ")
                              print("="*55)
                              additn="insert into grocery values ({},'{}',{},{})".format(item_ID,item_name,item_value,item_cost)
                              cursor.execute(additn)  #adding item
                              mycon.commit()
                              print("Wanna continue?")
                              conte=input("==> ")
                              if conte == 'y':
                                    home()
                              else:
                                    print("See you soon ;)")



                        elif choice2 == 2:
                              print("="*100)
                              show_table="select * from grocery"
                              cursor.execute(show_table)
                              data=cursor.fetchall()
                              print("="*100)
                              print(" "*28,"Current List")
                              print("="*100)
                              for df in data:                                    
                                    print(df)
                              print("="*100)
                              print("="*100)
                              print("Item name (OR) Item code: ")
                              print("-"*10)
                              choose=int(input("[1/2] ==> "))

                              if choose == 1:
                                    print("="*100)
                                    Itname=input("Item name: ")
                                    print("="*100)
                                    query="delete from grocery where item_name='%s'"%(Itname)
                                    cursor.execute(query)
                                    mycon.commit()
                              elif choose == 2:
                                    print("="*100)
                                    Itcode=int(input("Item Code: "))
                                    print("="*100)
                                    query="delete from grocery where item_ID='%s'"%(Itcode)
                                    cursor.execute(query)
                                    mycon.commit()

                        elif choice2 == 3 :
                              print("="*100)
                              show_table="select * from grocery"
                              cursor.execute(show_table)
                              data=cursor.fetchall()
                              print("="*100)
                              print(" "*28,"Current List")
                              print("="*100)
                              for df in data:                                    
                                    print(df)
                              print("="*100)
                              print("="*100)
                              choose=input("Select Item: ")
                              choose1=float(input("New Cost: "))
                              update="update grocery set item_cost = %s where item_name = '%s'"%(choose1,choose)
                              cursor.execute(update)
                              mycon.commit()
                              print("="*100)
                              print("Display New Table? [y/n]")
                              choice=input("==>")
                              if choice == 'y':
                                    print("="*100)
                                    show_table="select * from grocery"
                                    cursor.execute(show_table)
                                    data=cursor.fetchall()
                                    print("="*100)
                                    print(" "*28,"Current List")
                                    print("="*100)
                                    for df in data:                                    
                                          print(df)
                                    print("="*100)
                              else:
                                    Adminlogin()

                        elif choice2 == 4:
                              
                              print("="*100)
                              show_table="select * from grocery"
                              cursor.execute(show_table)
                              data=cursor.fetchall()
                              print("="*100)
                              print(" "*28,"Current List")
                              print("="*100)
                              for df in data:                                    
                                    print(df)
                              print("="*100)
                              print("="*100)
                              choose=input("Select Item: ")
                              choose1=float(input("New Value (max 250): "))
                              update="update grocery set item_value = %s where item_name = '%s'"%(choose1,choose)
                              cursor.execute(update)
                              mycon.commit()
                              print("="*100)
                              print("Display New Table? [y/n]")
                              choice=input("==>")
                              if choice == 'y':
                                    print("="*100)
                                    show_table="select * from grocery"
                                    cursor.execute(show_table)
                                    data=cursor.fetchall()
                                    print("="*100)
                                    print(" "*28,"Current List")
                                    print("="*100)
                                    for df in data:                                    
                                          print(df)
                                    print("="*100)
                              else:
                                    Adminlogin()      

                              
                           
                                    
                        elif choice2 == 5 :
                              print("-"*55)
                              show_table="select * from grocery"
                              cursor.execute(show_table)
                              data=cursor.fetchall()
                              print("-"*55)
                              print(" "*28,"Current List")
                              print("-"*55)
                              for df in data:                                    
                                    print(df)
                              print("-"*55)





      def home():
            print("="*55)
            print(" "*35,"Login Screen")
            print("="*55)
            print()
            print(" "*38,"i.Login")
            print(" "*36,"ii.Register")
            print(" "*36,"iii.Admin Login")
            print(" "*30,"iv. First time using? choose this.")
            print("="*55)
            print("""

                  """*5)
            input1=int(input("Select your choice [1]/[2]/[3]/[4]: "))
            print("-"*55)
            
      
            if input1==1:
                  login()
            elif input1==2:
                  register()
            elif input1==3:
                  Adminlogin()
            elif input1 == 4:
                  installation()
            else:
                  print("Invalid argument!")



#=============================================================================================================#
#=============================================================================================================#
      home()





print("="*55)
print(" "*28,"  Welcome To Groffters!  "," "*20)
print("="*55)
print()
print(" "*30,"  The worlds largest  ")
print(" "*26,"    online grocery store!!!!    ")
print()
print("="*55)

start=input("Type [y] to proceed: ")

if start=="y" or start=="Y":
      print("""

            """*20)
      index()
else:
      print("Thanks for stopping by :)")



