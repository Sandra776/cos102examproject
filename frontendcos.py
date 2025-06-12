import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox as mg
from backendcos import budget



colback = "#303269"
colman = 'white'
def image(a):
         icon = Image.open(a)
         icon1 = icon.resize((160,160))
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

          if n == '' or c == '' or d == '':
              mg.showerror('Info Error', 'Please Input In Every Field')
              self.iserror = True
          else:
           for i in my:
             i.delete(0,'end')
           mg.showinfo(e,f)
           if frame == self.framd:
               create_type = 'budget'
           else:
               create_type = 'category' 
           #this will input values into table      
           
           
         

       except ValueError:
             mg.showerror('Info Value', 'Error Inputting Values')
             self.iserror = True

   def delete(self):
      b= mg.askyesno('Delete Confirmation','Are you Sure You Want to Delete This Budget')
      if  b == True:
       #this will be to run a method in the backend that deletes the budget table and sets budget exists to false
       budget() == False 
       mg.showinfo('Delete', 'Budget Succesfully Deleted') 
   
   def display(self):
        #CREATE BUDGET
        self.framd = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)
        enam = tk.Label(self.framd, text='Create Budget',bg=colback,font=(None,20,'bold'),fg=colman)
        enam.place(relx= 0.5, rely=0.1,anchor='center')

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
    budget()
    if budget()== False:
            m.nobudget('Cannot Show Budget And Category Info\n Because Budget Does Not Exist')
    else:
      #BUDGET DISPLAY FRAME
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
        label.place(relx=0.1,rely=0.05)
        self.fr1am = tk.Frame(self.window,bg=colback, width=900,height=100, padx=10) 
        self.fr1am.place(relx=0.5,rely=0.23,anchor='center')

        label1 = tk.Label(self.window,bg='white',text='History', font=(None,40,'bold'))
        label1.place(relx=0.1,rely=0.35)
        self.fr2am = tk.Frame(self.window,bg=colback, width=900,height=350, padx=10) 
        self.fr2am.place(relx=0.5,rely=0.72,anchor='center')

        userl = tk.Label(self.fr1am, text='Username:', font=(None,12,'italic'),bg=colback,fg=colman)
        userl.place(relx=0.08,rely=0.25,anchor='center')
        edu= tk.Button(self.fr1am,text='Edit Username',bg=colman, relief= tk.FLAT)
        edu.place(relx=0.92,rely=0.25,anchor='center')
        passl = tk.Label(self.fr1am, text='Password:', font=(None,12,'italic'),bg=colback,fg=colman)
        passl.place(relx=0.08,rely=0.65,anchor='center')
        passu= tk.Button(self.fr1am,text='Edit Password',bg=colman, relief= tk.FLAT)
        passu.place(relx=0.92,rely=0.65,anchor='center')
   

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
            mg.showinfo(a,b)
             
       except ValueError:
             mg.showerror('Info Value', 'Error Inputting Values')
             self.iserror = True
      

    def display(self): 
      m =navbar(window)
      budget()
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
        dash = image(r"C:\Users\sandr\Desktop\cos102examproject\dash.png") 
        icona = image(r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        
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
        self.track=button(0.39,self.track1,dash)
        self.create=button(0.56,self.create1,dash)
        self.profile=button(0.73,self.profile1,dash)
        self.home= button(0.05,self.home1,icona)
    
    #METHODS TO SWITCH BETWEEN TABS
    def home1(self):
       self.destroy(0.05,self.home1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
       home_info()
       
    def dashboard1(self):
        self.destroy(0.22, self.dashboard1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = dashboard_info(window)
        window.title('Dashboard')
        m.display()
      
    def track1(self):
        self.destroy(0.39, self.track1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = track_info(window)
        window.title('Track')
        m.display()
      
    def create1(self):
        self.destroy(0.56, self.create1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = create_info(window)
        window.title('Create')
        m.display()

    def profile1(self):
        self.destroy(0.73, self.profile1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
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
window = tk.Tk()
window.geometry('700x500')
window.config(bg='white')
window.iconbitmap(r"C:\Users\sandr\Desktop\cos102examproject\actualicon.ico")

window.title('Welcome')
nav= navbar(window)
icon3 = Image.open(r"C:\Users\sandr\Desktop\cos102examproject\s.jpg")
icon5 = icon3.resize((600,1000))
icon4 = ImageTk.PhotoImage(icon5)
picture = tk.Label(window, image=icon4)
picture.image = icon4
picture.pack(side= 'left', fill='y')
picture.config(width=240)

def sign_in():
   button2.destroy()


def home_info():
 nav.frame
 window.title('Welcome')
 window.geometry('1280x697')
 button2.destroy()
 logo = Image.open(r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
 logo1 = ImageTk.PhotoImage(logo)

 picture = tk.Label(window, image=logo1,bg='white')
 picture.image = logo1
 picture.place(relx=0.25,rely=0.4,anchor='center')
 picture.config(width=150)
 
 apn = tk.Label(window,text='Pocket Budget',font=(None,40,'bold'),bg='white')
 apn.place(relx=0.25,rely=0.55,anchor='center')
 aps = tk.Label(window,text='Save Now, Benefit Later',font=(None,20,'italic'),bg='white')
 aps.place(relx=0.25,rely=0.65,anchor='center')

 title = tk.Label(window,text='Instructions',font=(None,30,'bold'),bg='white')
 title.place(relx=0.7,rely=0.2,anchor='center')

 body= tk.Label(window,text='Dashboard Tab- Shows the amount of money budgeted,\n unallocated funds and the category Info.\nEach category is color coded based on how much you spend.\n\nTrack- Allows you to log income and expenses.\n\nCreate- Allows You to create a monthly\nbudget and different categories.\n\nProfile- Allows you to see and change username and password\nand check expenses and income.',font=(None,17,'italic'),bg='white')
 body.place(relx=0.7,rely=0.5,anchor='center')

button2 = tk.Button(window, text='open',command=sign_in)
button2.place(relx=0.5,rely=0.5,anchor='center')


window.mainloop()