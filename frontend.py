import tkinter as tk
from PIL import Image, ImageTk
import backend

window = tk.Tk()
window.geometry('900x500')

class navbar():
    def __init__(self,windowname):
        self.window = windowname

    def frame(self):
        global button, image
        self.fram = tk.Frame(self.window,bg='#7476B1', width=100, padx=10)
        self.fram.pack(side= 'left', fill='y')

        def image(a):
         icon = Image.open(a)
         icon1 = icon.resize((250,250))
         self.icon2 = ImageTk.PhotoImage(icon1) 
         icon2 = ImageTk.PhotoImage(icon1)
         return icon2
        
        dash= image(r"C:\Users\sandr\Desktop\cos102examproject\ICON.png")   

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
       label= tk.Label(window, text='this is the dashboard')
       label.place(x=305,y=305)
       
      
    def track1(self):
        self.destroy(0.4, self.track1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        label= tk.Label(window, text='this is the track')
        label.place(x=305,y=315)
      
    def create1(self):
        self.destroy(0.6, self.create1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        label= tk.Label(window, text='this is the create tab')
        label.place(x=305,y=325)

    def profile1(self):
        self.destroy(0.8, self.profile1,r"C:\Users\sandr\Desktop\cos102examproject\ICONA.png")
        label= tk.Label(window, text='this is the profile tab')
        label.place(x=305,y=335)

    def destroy(self,dis,com,path):
       for widget in window.winfo_children():
          widget.destroy()
       nav1= navbar(window)
       nav1.frame()
       pic =image(path)
       button(dis,com,pic)


nav= navbar(window)
nav.frame()
window.mainloop()