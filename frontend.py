import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as mg
import backend

def input1(frame,text,yl,ye):
        label = tk.Label(frame, text=text,bg='#7476B1', font=15, fg='white')
        label.place(relx= 0.5, rely=yl,anchor='center')
        entry = tk.Entry(frame, relief= tk.FLAT)
        entry.place(relx= 0.5, rely=ye,anchor='center')
        entry.config(width=40)
        return entry

class create_info():
   def __init__(self,window):
      self.window=window

   def display(self):
    label= tk.Label(self.window, text='this is the create tab')
    label.place(x=305,y=325)

class dashboard_info():
   def __init__(self,window):
      self.window=window

   def display(self):
      #BUDGET DISPLAY FRAME
      self.fram = tk.Frame(self.window,bg='#7476B1', width=700,height=180, padx=10)
      self.fram.place(x=180,y=40)

      monnam = tk.Label(self.fram, text='MONTH',bg='#7476B1',font=(None,40,'bold'))
      monnam.place(relx=0.05, rely=0.08)
      datnam= tk.Label(self.fram, text='DATE CREATED',bg='#7476B1',font=(None,20,'italic'))
      datnam.place(relx=0.05, rely=0.45)
      spenam= tk.Label(self.fram, text='MONEY TO SPEND',bg='#7476B1',font=(None,20,'bold'))
      spenam.place(relx=0.05, rely=0.7)
      
      #UNALLOCATED FUNDS DISPLAY FRAME
      self.fram1 = tk.Frame(self.window,bg='#7476B1', width=330,height=85, padx=10)
      self.fram1.place(x=890, y=40)
      unam = tk.Label(self.fram1, text='UNALLOCATED FUNDS',bg='#7476B1',font=(None,15,'bold'))
      unam.place(relx=0.01,rely=0.3)

      #TOTAL SPENT DISPLAY FRAME
      self.fram2 = tk.Frame(self.window,bg='#7476B1', width=330,height=85, padx=10)
      self.fram2.place(x=890, y=135)
      snam = tk.Label(self.fram2, text='TOTAL SPENT',bg='#7476B1',font=(None,15,'bold'))
      snam.place(relx=0.01,rely=0.3)
      
      #CATEGORY DISPLAY FRAMES
      widget1=self.widget('red',180,250)
      widget2= self.widget('green',180,460)
      widget3=self.widget('yellow',390,460)
      widget4= self.widget('green',390,250)
      widget5=self.widget('yellow',600,250)
      widget6= self.widget('red',600,460)
      widget7=self.widget('yellow',810,250)
      widget8= self.widget('green',810,460)
      widget9=self.widget('red',1020,250)
      widget10= self.widget('green',1020,460)

   def widget(self,colour,a,b,m='#7476B1'):
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

      
class profile_info():
    def __init__(self,window):
     self.window=window   
   
    def display(self):
       label= tk.Label(window, text='this is the profile tab')
       label.place(x=305,y=335)

class track_info():
    def __init__(self,window):
       self.window=window   

    def submitexp(self):
          self.expnameentry= self.enameentry.get()
          self.expspententry = self.espententry.get()
          self.expcategoryentry = self.ecategoryentry.get()
          self.expdateentry = self.edateentry.get()
         
          m= [self.enameentry,self.espententry,self.ecategoryentry,self.edateentry]

          
          if self.expnameentry == '' or self.expnameentry.isdigit() == True:
             mg.showerror('Info Error', 'Invalid Value')
             self.iserror = True

          for i in m:
             i.delete(0,'end')

    def display(self):   
        # EXPENSES FRAME
        self.framd = tk.Frame(self.window,bg='#7476B1', width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)
        enam = tk.Label(self.framd, text='LOG EXPENSES',bg='#7476B1',font=(None,20,'bold'))
        enam.place(relx= 0.5, rely=0.1,anchor='center')
        
        self.enameentry=input1(self.framd,'Input Name Of Expenses',0.25,0.29,)
        self.espententry = input1(self.framd,'Input Money Spent',0.35,0.39,)
        self.ecategoryentry = input1(self.framd,'Input Category(If None input Unallocated)',0.45,0.49,)
        self.edateentry = input1(self.framd,'Input Date Of Expense',0.55,0.59,)

        esubmit = tk.Button(self.framd, text='Submit', relief=tk.FLAT, bg= 'white',command=self.submitexp)
        esubmit.place(relx= 0.5, rely=0.65,anchor='center')

        #INCOME FRAME
        
        self.framd1 = tk.Frame(self.window,bg='#7476B1', width=500,height=590, padx=10)
        self.framd1.place(x=750,y=45)
        inam = tk.Label(self.framd1, text='LOG INCOME',bg='#7476B1',font=(None,20,'bold'))
        inam.place(relx= 0.5, rely=0.1,anchor='center')

        self.inameentry=input1(self.framd1,'Input Name Of Income',0.25,0.29,)
        self.ispententry = input1(self.framd1,'Input Money Gained',0.35,0.39,)
        self.icategoryentry = input1(self.framd1,'Input Category(If None input Unallocated)',0.45,0.49,)
        self.idateentry = input1(self.framd1,'Input Date Of Income',0.55,0.59,)

        esubmit = tk.Button(self.framd1, text='Submit', relief=tk.FLAT, bg= 'white')
        esubmit.place(relx= 0.5, rely=0.65,anchor='center')


class navbar():
    def __init__(self,windowname):
        self.window = windowname
    
    def frame(self):
        global button, image
        #CREATES IMAGES FOR THE ICONS ON NAVBAR
        def image(a):
         icon = Image.open(a)
         icon1 = icon.resize((160,160))
         self.icon2 = ImageTk.PhotoImage(icon1) 
         icon2 = ImageTk.PhotoImage(icon1)
         return icon2
        
        #EACH ICON IMAGE FILE
        dash = image(r"C:\Users\sandr\Desktop\cos102examproject\dash.png") 
        icona = image(r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        
        #NAVBAR BACKGROUND
        self.fram = tk.Frame(self.window,bg='#7476B1', width=100, padx=10)
        self.fram.pack(side= 'left', fill='y')

        #CREATES BUTTONS FOR THE ICONS ON NAVBAR
        def button(a,b,c):
         cbutton = tk.Button(self.fram, image= c, relief = tk.FLAT, bg='#7476B1', command=b)
         cbutton.image = c
         cbutton.place(rely=a,relx=0.5, anchor='center')
         cbutton.config(width='0px', height='60px', activebackground='#7476B1')
        
        self.dashboard=button(0.3, self.dashboard1, dash)
        self.track=button(0.5,self.track1,dash)
        self.create=button(0.7,self.create1,dash)
        self.profile=button(0.9,self.profile1,dash)
        self.home= button(0.1,self.home1,icona)
    
    #METHODS TO SWITCH BETWEEN TABS
    def home1(self):
       self.destroy(0.1,self.home1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
       home_info()
       
    def dashboard1(self):
        self.destroy(0.3, self.dashboard1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = dashboard_info(window)
        window.title('Dashboard')
        m.display()
      
    def track1(self):
        self.destroy(0.5, self.track1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = track_info(window)
        window.title('Track')
        m.display()
      
    def create1(self):
        self.destroy(0.7, self.create1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
        m = create_info(window)
        window.title('Create')
        m.display()

    def profile1(self):
        self.destroy(0.9, self.profile1,r"C:\Users\sandr\Desktop\cos102examproject\activedash.png")
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
window.geometry('1280x672')
window.config(bg='white')

def home_info():
 window.title('Welcome')
 Label = tk.Label(window, text= 'WELCOME TO POCKET BUDGET...')
 Label.place(rely=0.5,relx=0.5,anchor='center')
 Label.config(width=40, bg='pink')
home_info()

nav= navbar(window)
nav.frame()

window.mainloop()