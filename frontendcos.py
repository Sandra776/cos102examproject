import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox as mg
from backendcos import budget
from backendcos import Connect

backend = Connect()
backend.connectserv()
colback = "#394D7B"
colman = 'white'
def image(a):
         icon = Image.open(a)
         icon1 = icon.resize((130,150))
         icon2 = ImageTk.PhotoImage(icon1) 
         return icon2

def input1(frame,text,yl,ye):
        label = tk.Label(frame, text=text,bg=colback, font=15, fg='white')
        label.place(relx= 0.5, rely=yl,anchor='center')
        entry = tk.Entry(frame, relief= tk.FLAT)
        entry.place(relx= 0.5, rely=ye,anchor='center')
        entry.config(width=40)
        return entry

class create_info():
   def __init__(self,window):
      self.window=window
   def submit(self,frame,name,setamount,wamount,date,e,f):
       try:
           d = datetime.strptime(date.get(),'%d/%m/%Y')   
       except:
           mg.showerror('Info Value', 'Please Input The right Date Format')
           self.iserror = True
       try:
          n= name.get().lower()
          m = float(setamount.get())
          c = float(wamount.get())                                  
          my=  [name,setamount,wamount,date]
          #see = backend.get_set_budget_amount() gets the amount left to spend in the budget and returns it
          if n == '' or c == '' or d == '':
              mg.showerror('Info Error', 'Please Input In Every Field')
              self.iserror = True
          elif c>=m:
            mg.showerror('Info Error', 'Warning Amount Cannot \nbe higher than or Equal to Set Amount')
          else:
           for i in my:
             i.delete(0,'end')
           mg.showinfo(e,f)
           if frame == self.framd:
             backend.create_budget_table(username)
             #backend.budget_table_insert(n,m,c,d)
             #backend.budget_Create_category_table(username)
             #backend.create_Transaction_table(username)
           else:
              print('info')
              #backend.category_table_insert(n,m,c,d)
              #backend.unallocated_remove()

       except ValueError:
             mg.showerror('Info Value', 'Error Inputting Values')
             self.iserror = True

   def delete(self):
      b= mg.askyesno('Delete Confirmation','Are you Sure You Want to Delete This Budget')
      if  b == True:
       #this will be to run a method in the backend that deletes the budget table and sets budget exists to false
       #backend.delete_table()
       mg.showinfo('Delete', 'Budget Succesfully Deleted') 
   
   def display(self):
        #CREATE BUDGET
        self.framd = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)
        enam = tk.Label(self.framd, text='Create Budget',bg=colback,font=(None,20,'bold'),fg=colman)
        enam.place(relx= 0.5, rely=0.1,anchor='center')
        
        #check if budget exist
        #backend.check_budget_exists()
        if budget() == True:
         nam = tk.Label(self.framd, text='Budget Already Exists\n To create Another Budget \nDelete The Current One',bg=colback,font=(None,20,'italic'),fg=colman)
         nam.place(relx= 0.5, rely=0.4,anchor='center')
         delt = tk.Button(self.framd, text='Delete Budget',relief=tk.FLAT, command= self.delete)
         delt.place(relx= 0.5, rely=0.6,anchor='center')
        else:
         self.enameentry=input1(self.framd,'Input Budget Name',0.25,0.29,)
         self.espendentry = input1(self.framd,'Input Money Allocated(Number)',0.35,0.39,)
         self.ewarningentry = input1(self.framd,'Input Warning Amount For Money(Number)',0.45,0.49,)
         self.edateentry = input1(self.framd,'Input Date Created (DD/MM/YYYY)',0.55,0.59,)

         esubmit = tk.Button(self.framd, text='Submit', relief=tk.FLAT, bg= 'white',
                            command=lambda:self.submit(self.framd,self.enameentry,self.espendentry,self.ewarningentry,self.edateentry,'Budget','Budget Successfully Created'))
         esubmit.place(relx= 0.5, rely=0.65,anchor='center')

        #CREATE CATEGORY
        
        self.framd1 = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd1.place(x=750,y=45)
        inam = tk.Label(self.framd1, text='Create Category',bg=colback,font=(None,20,'bold'),fg=colman)
        inam.place(relx= 0.5, rely=0.1,anchor='center')

        if budget() == False:
             nam1 = tk.Label(self.framd1, text='Cannot Create \nCategories Without A budget',bg=colback,font=(None,17,'bold'),fg=colman)
             nam1.place(relx= 0.5, rely=0.4,anchor='center')
        else:     
         self.inameentry=input1(self.framd1,'Input Name Of Category',0.25,0.29,)
         self.ispendentry = input1(self.framd1,'Input Money Allocated',0.35,0.39,)
         self.iwarningentry = input1(self.framd1,'Input Warning Amount',0.45,0.49,)
         self.idateentry = input1(self.framd1,'Input Date Created (DD/MM/YYYY)',0.55,0.59,)

         esubmit = tk.Button(self.framd1, text='Submit', relief=tk.FLAT, bg= 'white',
                            command=lambda:self.submit(self.framd1,self.inameentry,self.ispendentry,self.iwarningentry,self.idateentry,'Category','Category Successfully Created'))
         esubmit.place(relx= 0.5, rely=0.65,anchor='center')

class dashboard_info():

   def __init__(self,window):
      self.window=window

   def display(self):
    m =navbar(window)

    #backend.check_budget_exists()

    budget()
    if budget()== False:
            m.nobudget('Cannot Show Budget And Category Info\n Because Budget Does Not Exist')
    else:
      #BUDGET DISPLAY FRAME
      #bug_info=backend.get_budget_info() gets a list of [unallocated fund,,total amount left to spend,total spent]
      self.fram = tk.Frame(self.window,bg=colback, width=700,height=180, padx=10)
      self.fram.place(x=180,y=40)
      
      monnam = tk.Label(self.fram, text='Month',bg=colback,font=(None,40,'bold'),fg=colman)
      monnam.place(relx=0.05, rely=0.08)
      datnam= tk.Label(self.fram, text='Date Created',bg=colback,font=(None,20,'italic'),fg=colman)
      datnam.place(relx=0.05, rely=0.45)
      spenam= tk.Label(self.fram, text='Money To Spend',bg=colback,font=(None,20,'bold'),fg=colman)
      spenam.place(relx=0.05, rely=0.7)
      
      #UNALLOCATED FUNDS DISPLAY FRAME
      self.fram1 = tk.Frame(self.window,bg=colback, width=330,height=85, padx=10)
      self.fram1.place(x=890, y=40)
      unam = tk.Label(self.fram1, text='Unallocated Funds',bg=colback,font=(None,15,'bold'),fg=colman)
      unam.place(relx=0.01,rely=0.3)

      #TOTAL SPENT DISPLAY FRAME
      self.fram2 = tk.Frame(self.window,bg=colback, width=330,height=85, padx=10)
      self.fram2.place(x=890, y=135)
      snam = tk.Label(self.fram2, text='TOTAL SPENT',bg=colback,font=(None,15,'bold'),fg=colman)
      snam.place(relx=0.01,rely=0.3)
      
      #cat_nam=backend.get_category_name() returns list of category names
      #cat_spent=backend.get_category_left_spend() returns list of category left to spent
      #cat_spent=backend.get_category_spent() returns list of category spent amount
      #cat_check_warning=backend_check_warning() gets warning amount for category, gets spent in category,get amount,
      #  checks wether it is above warning amount,or above the amount set, if it is above warning amount and below amount set 
      # colour=yellow, if it is above set amount colour=red, if it is below warning amount  colour= green, return colour


      # for loop uses cat_nam length and inputes values into each frame


      #CATEGORY DISPLAY FRAMES
      wi1=self.widget('red',180,250)
      wi2= self.widget('green',180,460)
      wi3=self.widget('yellow',390,460)
      wi4= self.widget('green',390,250)
      wi5=self.widget('yellow',600,250)
      wi6= self.widget('red',600,460)
      wi7=self.widget('yellow',810,250)
      wi8= self.widget('green',810,460)
      wi9=self.widget('red',1020,250)
      wi10= self.widget('green',1020,460)

      widget = [wi1,wi2,wi3,wi4,wi5,wi6,wi7,wi8,wi9,wi10]
      
    # check if you have gone over warning amount
   def widget(self,colour,a,b,m=colback):
      if colour=='red':
         m= "#B17474"
      elif colour=='green':
         m="#80B174"
      elif colour =='yellow':
         m= "#B0B174"
      self.wig = tk.Frame(self.window,bg=m, width=200,height=200, padx=10)
      self.wig.place(x=a, y=b)
      name= tk.Label(self.wig, text='CATEGORY NAME',bg=m, font=(None,10,'bold'))
      name.place(rely= 0.2, relx=0.5,anchor='center')
      bugsp= tk.Label(self.wig, text='TOTAL AMOUNT \nTO SPEND',bg=m, font=(None,10,'italic'))
      bugsp.place(rely= 0.4, relx=0.5,anchor='center')
      bugspt= tk.Label(self.wig, text='TOTAL AMOUNT \nSPENT',bg=m, font=(None,10,'italic'))
      bugspt.place(rely= 0.6, relx=0.5,anchor='center')
      return self.wig

      
class profile_info():
    def __init__(self,window):
     self.window=window
   
    def display(self):
        label = tk.Label(self.window,bg='white',text='Profile Info', font=(None,40,'bold'))
        label.place(relx=0.1,rely=0.3)
        self.fr1am = tk.Frame(self.window,bg=colback, width=900,height=100, padx=10) 
        self.fr1am.place(relx=0.5,rely=0.5,anchor='center')

        #backend.get_user_info()
        userl = tk.Label(self.fr1am, text=f'Username:{username}', font=(None,12,'italic'),bg=colback,fg=colman)
        userl.place(relx=0.06,rely=0.15)

        passl = tk.Label(self.fr1am, text= f'Password:{password}', font=(None,12,'italic'),bg=colback,fg=colman)
        passl.place(relx=0.06,rely=0.55)
   

class track_info():
    def __init__(self,window):
       self.window=window  
    
    def form(self,frame,name,inam,mon,cat,date,des,a,b):
         enam = tk.Label(frame, text=name,bg=colback,font=(None,20,'bold'),fg=colman)
         enam.place(relx= 0.5, rely=0.1,anchor='center')
         nameentry=input1(frame,inam,0.25,0.29,)
         spententry = input1(frame,mon,0.35,0.39,)
         categoryentry = input1(frame,cat,0.45,0.49,)
         dateentry = input1(frame,date,0.55,0.59,) 
         desentry = input1(frame,des,0.65,0.69)

         esubmit = tk.Button(frame, text='Submit', relief=tk.FLAT, bg= 'white',
                            command= lambda:self.submit(frame,nameentry,spententry,categoryentry,dateentry,desentry,a,b))
         esubmit.place(relx= 0.5, rely=0.75,anchor='center')

    def submit(self,frame,name,money,category,date,des,a,b):
       try:
                d = datetime.strptime(date.get(),'%d/%m/%Y')  
       except:
             mg.showerror('Info Value', 'Wrong Date Format')
             self.iserror = True
       try:
          n= name.get().lower().strip()
          m = float(money.get().strip())
          c = category.get().lower().strip()
          e = des.get().lower().strip()                                  
          my=  [money,name,category,date,des]

          if n == '' or c == '':
              mg.showerror('Info Error', 'Please Input In Every Field')
              self.iserror = True
          else:
            if frame == self.framd:
              transaction_type = 'Expense'
            else:
              transaction_type='Income'
            for i in my:
             i.delete(0,'end')
            #backend.transaction_table_insert(n,d,m,c,d,transaction_type) this
            #  also subtracts or adds money left to spend in category, and then adds or subtract from  total spent
            mg.showinfo(a,b)

             
       except ValueError:
             mg.showerror('Info Value', 'Error Inputting Values')
             self.iserror = True
      

    def display(self): 
      m =navbar(window)
      budget()
      #
      if budget() == False:
            m.nobudget('Cannot Log Expenses And Income\n Because Budget Does Not Exist')
      else: 
        # EXPENSES FRAME
        self.framd = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)

        self.form(self.framd,'Log Expense','Input Name Of Expense','Input Money Spent(Number)','Input Category(If None input Unallocated)',
                 'Input Date Of Expense (DD/MM/YYYY)','Input Description(Optional)','Expense','Expense Succesfully Logged')

        #INCOME FRAME
        self.framd1 = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd1.place(x=750,y=45)
        self.form(self.framd1,'Log Income','Input Name Of Income','Input Money Gained(Number)','Input Category(If None input Unallocated)',
                 'Input Date Of Income (DD/MM/YYYY)','Input Description(Optional)','Income','Income Succesfully Logged')

class navbar():
    def __init__(self,windowname):
        self.window = windowname

    def nobudget(self,a):
   
       labelno = tk.Label(self.window,text=a,bg='white',font=(None,35,'bold'))
       labelno.place(relx= 0.54, rely=0.45,anchor='center')
       buttonno = tk.Button(self.window,text="Create Budget",bg=colback,relief=tk.FLAT,command=self.create1,fg='white',font=5)
       buttonno.place(relx= 0.54, rely=0.6,anchor='center')
       buttonno.config(width=14,height=2)
    
    def frame(self):
        global button, image
        #CREATES IMAGES FOR THE ICONS ON NAVBAR
        
        #EACH ICON IMAGE FILE
        dash = image(r"dash.png") 
        icona = image(r"logon.png")
        track = image(r"track.png")
        cren = image(r"create.png")
        prof = image(r"prof.png")
        
        #NAVBAR BACKGROUND
        self.fram = tk.Frame(self.window,bg=colback, width=100, padx=10)
        self.fram.pack(side= 'left', fill='y')

        #CREATES BUTTONS FOR THE ICONS ON NAVBAR
        def button(a,b,c):
         cbutton = tk.Button(self.fram, image= c, relief = tk.FLAT, bg=colback, command=b)
         cbutton.image = c
         cbutton.place(rely=a,relx=0.5, anchor='center')
         cbutton.config(width='0px', height='60px', activebackground=colback)
        
        self.dashboard=button(0.22, self.dashboard1, dash)
        self.track=button(0.39,self.track1,track)
        self.create=button(0.56,self.create1,cren)
        self.profile=button(0.73,self.profile1,prof)
        self.home= button(0.05,self.home1,icona)
    
    #METHODS TO SWITCH BETWEEN TABS
    def home1(self):
       self.destroy(0.05,self.home1,r"logon.png")
       home_info()
       
    def dashboard1(self):
        self.destroy(0.22, self.dashboard1,r"activedash.png")
        m = dashboard_info(window)
        window.title('Dashboard')
        m.display()
      
    def track1(self):
        self.destroy(0.39, self.track1,r"activetrack.png")
        m = track_info(window)
        window.title('Track')
        m.display()
      
    def create1(self):
        self.destroy(0.56, self.create1,r"activecrea.png")
        m = create_info(window)
        window.title('Create')
        m.display()

    def profile1(self):
        self.destroy(0.73, self.profile1,r"activeprof.png")
        m = profile_info(window)
        window.title('Profile')
        m.display()
    
    #METHOD USED TO DESTROY EVERYTHING ON PARENT WIDGET AND RECREATE NAVBAR AND EVERYTHING ON TAB CLICKED
    def destroy(self,dis,com,path):
       for widget in window.winfo_children():
          widget.destroy()
       nav1= navbar(window)
       nav1.frame()

       #CHANGES THE ICON TO AN ACTIVE ICON
       pic =image(path)

       button(dis,com,pic)

#HOME WINDOW
class loginsignin():
 
 def check_signin(self):
   password1=self.passe.get()
   user1=self.usere.get()

   #check= backend.check_user(user1,password1)

   if self.passe.get() == '' and self.usere.get() == '':
      mg.showerror('Input Error','Please Input In every field')
   else:
    for widget in window.winfo_children():
          widget.destroy()

    home_info()
    nav= navbar(window)
    nav.frame()
  
 def create_signup(self):
     global username,password
     username= self.usere1.get()
     password=self.passe1.get()
     
     if self.passe1.get() == '' and self.usere1.get() == '':
      mg.showerror('Input Error','Please Input In every field')
     else:
      #backend.user_table_insert(username,password)
      for widget in window.winfo_children():
          widget.destroy()

     home_info()
     nav= navbar(window)
     nav.frame()

 def sign_in(self):
   window.title('Sign In')
   button2.destroy()
   wel.destroy()
   button4.destroy()
   lend.destroy()
   background.destroy()

   back =tk.Button(window, text='Go Back',relief=tk.FLAT,bg=colback,fg=colman,command=intro)
   back.config(width=10)

   back.place(relx=0.9,rely=0.2,anchor='center')  
   title1 = tk.Label(window, text='Sign In',bg = colman, font=(None,20,'bold'))
   title1.place(relx=0.5,rely=0.2,anchor='center') 
   title1.config(width=8)
   self.usern = tk.Label(window, text='Username:',bg=colman,font=(None,10,'italic'))
   self.usern.place(relx=0.5,rely=0.3,anchor='center')
   self.usere = tk.Entry(window,bg=colback,relief=tk.FLAT,fg=colman)
   self.usere.place(relx=0.6,rely=0.35,anchor='center')
   self.usere.config(width=30)

   self.passn = tk.Label(window, text='Password:',bg=colman,font=(None,10,'italic'))
   self.passn.place(relx=0.5,rely=0.45,anchor='center')
   self.passe = tk.Entry(window,bg=colback,relief=tk.FLAT,fg=colman, show='*')
   self.passe.place(relx=0.6,rely=0.5,anchor='center')
   self.passe.config(width=30)

   buttonsign = tk.Button(window,text='Sign In',command=self.check_signin,relief=tk.FLAT,bg=colback,fg=colman)
   buttonsign.place(relx=0.6,rely=0.6,anchor='center')
   buttonsign.config(width=10)

 def sign_up(self):
   window.title('Sign Up')
   button2.destroy()
   wel.destroy()
   button4.destroy()
   lend.destroy()
   background.destroy()
   

   title1 = tk.Label(window, text='Sign Up',bg = colman, font=(None,20,'bold'))
   title1.place(relx=0.5,rely=0.2,anchor='center') 
   self.usern1 = tk.Label(window, text='Username:',bg=colman,font=(None,10,'italic'))
   self.usern1.place(relx=0.5,rely=0.3,anchor='center')
   self.usere1 = tk.Entry(window,bg=colback,relief=tk.FLAT,fg=colman)
   self.usere1.place(relx=0.6,rely=0.35,anchor='center')
   self.usere1.config(width=30)

   self.passn1 = tk.Label(window, text='Password:',bg=colman,font=(None,10,'italic'))
   self.passn1.place(relx=0.5,rely=0.45,anchor='center')
   self.passe1 = tk.Entry(window,bg=colback,relief=tk.FLAT,fg=colman, show='*')
   self.passe1.place(relx=0.6,rely=0.5,anchor='center')
   self.passe1.config(width=30)

   buttonsign = tk.Button(window,text='Sign Up',command=self.create_signup,relief=tk.FLAT,bg=colback,fg=colman)
   buttonsign.place(relx=0.6,rely=0.6,anchor='center')
   buttonsign.config(width=10) 
   back =tk.Button(window, text='Go Back',relief=tk.FLAT,bg=colback,fg=colman,command=intro)
   back.config(width=10)

   back.place(relx=0.9,rely=0.2,anchor='center')  



this=loginsignin()

def home_info():
 window.title('Welcome')
 window.geometry('1280x697')
 button2.destroy()

 picture = tk.Label(window, image=logo1,bg='white')
 picture.image = logo1
 picture.place(relx=0.25,rely=0.34,anchor='center')
 picture.config(width=260)
 
 apn = tk.Label(window,text='Pocket Aid',font=(None,40,'bold'),bg='white')
 apn.place(relx=0.25,rely=0.55,anchor='center')
 aps = tk.Label(window,text='Save Now, Benefit Later',font=(None,20,'italic'),bg='white')
 aps.place(relx=0.25,rely=0.65,anchor='center')

 title = tk.Label(window,text='Instructions',font=(None,30,'bold'),bg='white')
 title.place(relx=0.7,rely=0.2,anchor='center')

 body= tk.Label(window,text='Dashboard Tab- Shows the amount of money budgeted,\n unallocated funds and the category Info.\nEach category is color coded based on how much you spend.\n\nTrack- Allows you to log income and expenses.\n\nCreate- Allows You to create a monthly\nbudget and different categories.\n\nProfile- Allows you to see username and password.',font=(None,17,'italic'),bg='white')
 body.place(relx=0.7,rely=0.5,anchor='center')

window = tk.Tk()
window.geometry('700x500')
window.config(bg='white')
window.iconbitmap(r"logoico.ico")

window.title('Guide')
icon3 = Image.open(r"s.jpg")
icon5 = icon3.resize((600,500))
icon4 = ImageTk.PhotoImage(icon5)
picture5 = tk.Label(window, image=icon4)
picture5.image = icon4
picture5.pack(side= 'left', fill='y')
picture5.config(width=260)

logo = Image.open(r"logoico.ico")
logo1 = ImageTk.PhotoImage(logo)

def intro():
 window.title('Welcome')
 global wel,lend,button2,button4, background

 background = tk.Label(window,bg='white')
 background.pack()
 background.config(width=900,height=900)

 wel = tk.Label(window,text='Welcome To\n Pocket Aid Budgeting App',font=(None,20,'bold'),bg='white')
 lend = tk.Label(window,image=logo1, bg='white')
 lend.image= logo1
 lend.config(width=250,height=170)

 button2 = tk.Button(window, text='Sign In',command=this.sign_in,relief=tk.FLAT,bg=colback,fg=colman)
 button2.config(width=10)
 button4 = tk.Button(window, text='Sign Up',command=this.sign_up,relief=tk.FLAT,bg=colback,fg=colman)
 button4.config(width=10)
 
 wel.place(relx=0.68,rely=0.65,anchor='center')
 lend.place(relx=0.7,rely=0.34,anchor='center')
 button2.place(relx=0.58,rely=0.8,anchor='center')
 button4.place(relx=0.78,rely=0.8,anchor='center')

intro()

window.mainloop()