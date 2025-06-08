import tkinter as tk
from PIL import Image, ImageTk
import backend

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
      self.fram = tk.Frame(self.window,bg='#7476B1', width=700,height=180, padx=10)
      self.fram.place(x=180,y=40)
      self.fram1 = tk.Frame(self.window,bg='#7476B1', width=330,height=85, padx=10)
      self.fram1.place(x=890, y=40)
      self.fram2 = tk.Frame(self.window,bg='#7476B1', width=330,height=85, padx=10)
      self.fram2.place(x=890, y=135)
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
      name= tk.Label(self.wig, text='CATEGORY NAME',bg=m)
      name.place(rely= 0.2, relx=0.5, anchor='center')
      
class profile_info():
    def __init__(self,window):
     self.window=window   
   
    def display(self):
       label= tk.Label(window, text='this is the profile tab')
       label.place(x=305,y=335)

class track_info():
    def __init__(self,window):
       self.window=window   
   
    def display(self):    
        self.framd = tk.Frame(self.window,bg='#7476B1', width=500,height=590, padx=10)
        self.framd.place(x=210,y=40)
        self.framd = tk.Frame(self.window,bg='#7476B1', width=500,height=590, padx=10)
        self.framd.place(x=730,y=40)

class navbar():
    def __init__(self,windowname):
        self.window = windowname
    
    def frame(self):
        global button, image
        def image(a):
         icon = Image.open(a)
         icon1 = icon.resize((250,250))
         self.icon2 = ImageTk.PhotoImage(icon1) 
         icon2 = ImageTk.PhotoImage(icon1)
         return icon2
        
        dash = image(r"C:\Users\sandr\Desktop\cos102examproject\ICON.png") 

        self.fram = tk.Frame(self.window,bg='#7476B1', width=100, padx=10)
        self.fram.pack(side= 'left', fill='y')
        
        def button(a,b,c):
         cbutton = tk.Button(self.fram, image= c, relief = tk.FLAT, bg='#7476B1', command=b)
         cbutton.image = c
         cbutton.place(rely=a,relx=0.5, anchor='center')
         cbutton.config(width='40px', height='40px')
        
        self.dashboard=button(0.2, self.dashboard1, dash)
        self.track=button(0.4,self.track1,dash)
        self.create=button(0.6,self.create1,dash)
        self.profile=button(0.8,self.profile1,dash)

    def dashboard1(self):
       self.destroy(0.2, self.dashboard1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
       m = dashboard_info(window)
       m.display()
      
    def track1(self):
        self.destroy(0.4, self.track1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        m = track_info(window)
        m.display()
      
    def create1(self):
        self.destroy(0.6, self.create1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        m = create_info(window)
        m.display()

    def profile1(self):
        self.destroy(0.8, self.profile1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        m = profile_info(window)
        m.display()

    def destroy(self,dis,com,path):
       for widget in window.winfo_children():
          widget.destroy()
       nav1= navbar(window)
       nav1.frame()
       pic =image(path)
       button(dis,com,pic)

window = tk.Tk()
window.geometry('1280x662')
window.config(bg='white')

Label = tk.Label(window, text= 'WELCOME TO POCKET BUDGET...')
Label.place(rely=0.5,relx=0.5,anchor='center')
Label.config(width=40, bg='pink')
nav= navbar(window)
nav.frame()
window.mainloop()