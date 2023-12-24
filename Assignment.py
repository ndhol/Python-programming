def menu():#def function
    while True:
        print("Select your character.")#print statement
        print("1.ADMIN")
        print("2.NEW CUSTOMER")
        print("3.REGISTERED CUSTOMER")
        print()
        selection=int(input("Please enter your selection."))#ask selection from user
        if selection==1:
            admin()#call function admin
            upload()#call function upload
            choice()#call function choice
        elif selection==2:
            newcustomer()#call function newcustomer
        elif selection==3:
            registeredcustomer()#call function registeredcustomer
            selection()#call function selection
        else:
            print("Invalid input.")


def admin():
    try:
        fhand=open('admin.txt','r')#open text file
    except:
        print("The file cannot open.")#print statement if file non-existent
        exit()#exit the system

    for line in fhand:#for the line in the text file
        line=line.rstrip()#removes any trailing characters
        adminid=input("Please insert your ID number.")#ask admin to insert his registered id
        if adminid==line.split('\t')[4]:
            print("Id enabled.")#if the id is in the text file,then it will print statement

            while True:
                Password=input("Please insert your password.")#ask admin to insert his registered password
                if Password==line.split('\t')[5]:
                    print("Login successful!")
                    upload()
                    break#if the password is in the text file,then it will print statement and call function upload
                else:
                    print("Password wrong.Please reenter your password.")
                    continue#if the password is not in the text file,then it will print statement and continue ask for password
            break
        else:
            print("ID you enter is wrong.Please reenter.")
            admin()#if the id is not in the text file,then it will print statement and call function admin
    
def upload():
    grocery_list=[]#make a list
    n=int(input("Please enter the number of grocery you want to insert."))#ask admin to enter number
    for i in range(n):#continue run in the range of admin insert
        details=[]
        Spec=input("Please write the specification of the grocery.")#ask user to insert information 
        details.append(Spec)#will append all the information user insert into the list
        Groceryname=input("PLease insert the grocery name.")
        details.append(Groceryname)
        Exp=input("What is the expired date of the grocery?")
        details.append(Exp)
        Price=input("What is the price of the grocery?")
        details.append(Price)
        grocery_list.append(details)#will append all the information in the list into the another list
        for item in grocery_list:
            print('Details -',Spec,Groceryname,'Exp:',Exp,'RM',Price)#if the item is in the list then print the statement

        repeat=input("Add another item?yes/no")#ask user want to add things or not
        if repeat=="yes":
            continue
        else:
            choice()
    
    try:
        fileHandler=open('Groceries.txt','a+')#open text file
    except:
        print("The file cannot open")
        exit()#if the text file non-existent then print statement and exit to the system

    for details in grocery_list:
        for gl in details:
            fileHandler.write(gl)#for the information in the list,write into the text file
            fileHandler.write('\t')#write the information with tab
        fileHandler.write('\n')#write the information in a new line
    fileHandler.close()#close the text file


def choice():#def function
    while True:#if true
        print("Select your action.")
        print("1.View the grocery list.")
        print("2.Search the grocery you want.")
        print("3.Modify the grocery list.")
        print("4.Delete grocery.")
        print("5.View customer's order.")
        print("6.Search order of customer.")
        print("7.Exit.")#print statement
        print()
        choice=int(input("Please enter your choice."))#ask user for input
        if choice==1:
            fhand=open('Groceries.txt')#open file
            inp=fhand.read()#read the file
            print(inp)#print the word in the file
            fhand.close()#close the file
            exit()
        elif choice==2:
            try:
                fhand=open('Groceries.txt','r')#try open file,
            except:
                print("The file cannot open.")
                exit()#if the text file non-existent then print statement and exit to the system

            search=input("What grocery you want to search.")#ask for input 

            for line in fhand:
                line=line.rstrip()
                if not search.lower()in line.lower():
                    continue
                print(line)#if is the word user insert then print the word
        elif choice==3:
            fhand=open('Groceries.txt','r')
            inp=fhand.read()
            print(inp)
            new=[]#make a list
            word=input("Which grocery you want to replace?")#ask for input
            rep=input("Which word you want to replace it with?")
            replace=inp.replace(word,rep)#replace the word
            print(replace)#print the word after replace
            new.append(replace)#append the replace word into the text file

            try:
                fileHandler=open('Groceries.txt','w')#try open file,w=write into the file
            except:
                print("The file cannot open")
                exit()#if the text file non-existent then print statement and exit to the system

            for replace in new:
                for gl in replace:
                    fileHandler.write(gl)#for the information in the list,write into the text file
                fileHandler.write('\n')#write the information in a new line
            fileHandler.close()#close the file
        elif choice==4:
            fhand=open('Groceries.txt')#open groceries text file
            search=input("Please insert the grocery you want to remove.")#ask for input
            new_list=[]#make a list
            for line in fhand:
                if not search.lower()in line.lower():
                    print(line)
                    new_list.append(line)#if not the word user insert then print line and append it into the file
                continue
            try:
                fileHandler=open('Groceries.txt','w')
            except:
                print("The file cannot open")
                exit()

            for line in new_list:
                for gl in line:
                    fileHandler.write(gl)#for the information in the list,write into the text file
                fileHandler.write('\n')#write the information in a new line
            fileHandler.close()
        elif choice==5:
            fhand=open('own order.txt')#open the file
            inp=fhand.read()#read the file
            print(inp)#print the word in the file
            
        elif choice==6:
            fhand=open('own order.txt')
            search=input("Please insert customer name you want to search.")#ask for input

            for line in fhand:
                line=line.rstrip()
                if not search.lower()in line.lower():
                    continue
                print(line)#if is the word user insert then print line
            fhand.close()
            exit()
        elif choice==7:
            exit()#exit from the system
        else:
            print("Invalid input.")


def newcustomer():
    regis=[]#make a list
    n=int(input("Enter the number you want to register."))#ask for input
    for i in range(n):#run the function in the range user insert
        customer_list=[]
        print("Cause you are a new customer, please do a registration.")#print statement
        Name=input("What is your name?")#ask for input
        customer_list.append(Name)#append the word user insert into a list
        Address=input("Please insert your address.")
        customer_list.append(Address)
        Email_ID=input("Please insert your email address.")
        customer_list.append(Email_ID)
        Contact_no=input("Please insert your contact number.")
        customer_list.append(Contact_no)
        Date_of_Birth=input("Please insert your date of birth.")
        customer_list.append(Date_of_Birth)
        User_ID=input("Please create any user ID you like.")
        customer_list.append(User_ID)
        Password=input("Please create a password for your ID.")
        customer_list.append(Password)
        Rewrite_password=input("Please write again your password.")
        regis.append(customer_list)#append the things in the list to another list
    
        try:
            fileHandler=open('new customer.txt','a+')#open the file,a+=write&append
        except:
            print('File cannot be open')
            exit()#if the text file non-existent then print statement and exit to the system

    for customer_list in regis:
        for reg in customer_list:
            fileHandler.write(reg)#for the information in the list,write into the text file
            fileHandler.write('\t')#write the information with tab
        fileHandler.write('\n')#write the information in a new line
    
    fileHandler.close()
    fhand=open('Groceries.txt')#open the file
    inp=fhand.read()#read the file
    print(inp)#print the word in the file

    fhand.close()#close the file
    
def registeredcustomer():
    try:
        fhand=open('registered personal information.txt','r')#open the file,r=read from the file
    except:
        print("The file cannot open.")
        exit()#if the text file non-existent then print statement and exit to the system

    for line in fhand:
        line=line.rstrip()#removes any trailing characters
        ID=input("Please insert your user_ID.")#ask for input
        if ID==line.split('\t')[5]:
            print("Id enabled.")#if the password is in the text file,then it will print statement

            while True:
                Password=input("Please insert your password.")
                if Password==line.split('\t')[6]:#if the password is in the text file
                    print("Login successful!")#then it will print statement
                    fhand=open('Groceries.txt')
                    inp=fhand.read()
                    print(inp)#open file, read file then print the information in the file
                    fhand.close()
                    selection()
                    break#call function selection then break
                else:
                    print("Password wrong.Please reenter your password.")
                    continue#if the password is not in the file then it will let you reenter
            break
        else:
            print("ID you enter is wrong.Please reenter.")
            registeredcustomer()#if the ID is not in the file then it will let you reenter and call function registeredcustomer


def selection():
    while True:#if true
        print("Select your action.")
        print("1.Place order and do payment.")
        print("2.View your personal information.")#print statement
        print("3.Exit")
        print()
        choice=int(input("Please enter your choice."))#ask for input
        if choice==1:
            order=[]#make a list
            n=int(input("Please enter the number of item you want to buy."))#ask for input in number
            for i in range (n):#run the system in the range user insert
                cus_order=[]
                userid=input("What is your id?")#ask for input
                cus_order.append(userid)#append the input into the list
                grocery=input("What grocery you want to buy?")
                cus_order.append(grocery)
                quantity=input("How many you want to buy?")
                cus_order.append(quantity)
                print ("Your groceries:\n",userid,grocery,quantity)#print the input user insert
                order.append(cus_order)#append the information in the list into another list

            try:
                fileHandler=open('own order.txt','a+')#open the file,a+=write&append
            except:
                print("This file cannot open")
                exit()#if the text file non-existent then print statement and exit to the system

            for cus_order in order:
                for item in cus_order:
                    fileHandler.write(item)#for the information in the list,write into the text file
                    fileHandler.write('\t')#write the information with tab
                fileHandler.write('\n')#write the information in a new line

            fileHandler.close()

            fhand=open('own order.txt','r')#open and view file
            inp=fhand.read()#read file
            print(inp)#print information in the file

            fhand.close()
            
            print("Payment method.")
            print("1.e Payment")
            print("2.Cash.")#print statement
            print()
            payment=int(input("Choose your payment method.1/2"))#ask for input
            if payment==1:
                print("Thank you to choose FRESHCO.Hope you have a nice day!")#if input=1 then print statement
            elif payment==2:
                print("Please bring your cash to delivery person. Hope you have a nice day!")#if input=2 then print statement
            else:
                print("Invalid number.")#if input=1 or 2 then print statement
        elif choice==2:
            fhand=open('registered personal information.txt')#open the file
            search=input("Please insert your name.")#get the input that want to search
            for line in fhand:
                line=line.rstrip()
                if not search.lower()in line.lower():
                    continue
                print(line)#if is the word user insert then print line
            fhand.close()
        elif choice==3:
            exit()
        else:
            print("Invalid number")#if input=1 or 2 then print statement


menu()#call function menu
