import tkinter as tk
from tkinter import ttk
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import messagebox as mg
from backendcos import Connect
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

backend = Connect()
backend.connectserv()
backend.create_users_table()
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
  
   def submit(self,frame,name,setamount,wamount):
       try:
          n= name.get().strip().title()
          m = float(setamount.get())
          c = float(wamount.get())                                  
          my=  [name,setamount,wamount]
          #see = backend.get_set_budget_amount() gets the amount left to spend in the budget and returns it
          if n == '' or c == '':
              mg.showerror('Info Error', 'Please Input In Every Field')
          elif c>=m:
            mg.showerror('Info Error', 'Warning Amount Cannot \nbe higher than or Equal to Set Amount')
          else:
           for i in my:
             i.delete(0,'end')
           if frame == self.framd:
             backend.create_budget_table()
             backend.budget_table_insert(n,m,c)
             backend.create_category_table()
             backend.create_transaction_table()
             mg.showinfo('Create Budget','Budget Created Succesfully')
           else:
              asky=mg.askyesno('Create Category','Are you Sure you want to create this category')
              if asky == True:
               print('info')
               backend.category_table_insert(n,m,c)
               #backend.unallocated_remove()
               mg.showinfo('Create Category', 'Category Created Succesfully')

       except ValueError:
             mg.showerror('Info Value', 'Error Inputting Values')
             self.iserror = True

   def delete(self):
      b= mg.askyesno('Delete Confirmation','Are you Sure You Want to Delete This Budget')
      if  b == True:
       #this will be to run a method in the backend that deletes the budget table and sets budget exists to false
       backend.delete_table()
       mg.showinfo('Delete', 'Budget Succesfully Deleted') 
   
   def display(self):
        #CREATE BUDGET
        self.framd = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)
        enam = tk.Label(self.framd, text='Create Budget',bg=colback,font=(None,20,'bold'),fg=colman)
        enam.place(relx= 0.5, rely=0.1,anchor='center')
        
        #check if budget exist
        check= backend.budget_table_exists()
        if check == True:
         nam = tk.Label(self.framd, text='Budget Already Exists\n To create Another Budget \nDelete The Current One',bg=colback,font=(None,20,'italic'),fg=colman)
         nam.place(relx= 0.5, rely=0.4,anchor='center')
         delt = tk.Button(self.framd, text='Delete Budget',relief=tk.FLAT, command= self.delete)
         delt.place(relx= 0.5, rely=0.6,anchor='center')
        else:
         self.enameentry=input1(self.framd,'Input Budget Name',0.25,0.29,)
         self.espendentry = input1(self.framd,'Input Money Allocated(Number)',0.35,0.39,)
         self.ewarningentry = input1(self.framd,'Input Warning Amount For Money(Number)',0.45,0.49,)

         esubmit = tk.Button(self.framd, text='Submit', relief=tk.FLAT, bg= 'white',
                            command=lambda:self.submit(self.framd,self.enameentry,self.espendentry,self.ewarningentry))
         esubmit.place(relx= 0.5, rely=0.55,anchor='center')

        #CREATE CATEGORY
        
        self.framd1 = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd1.place(x=750,y=45)
        inam = tk.Label(self.framd1, text='Create Category',bg=colback,font=(None,20,'bold'),fg=colman)
        inam.place(relx= 0.5, rely=0.1,anchor='center')

        if check == False:
             nam1 = tk.Label(self.framd1, text='Cannot Create \nCategories Without A budget',bg=colback,font=(None,20,'italic'),fg=colman)
             nam1.place(relx= 0.5, rely=0.5,anchor='center')
        else:     
         self.inameentry=input1(self.framd1,'Input Name Of Category',0.25,0.29,)
         self.ispendentry = input1(self.framd1,'Input Money Allocated',0.35,0.39,)
         self.iwarningentry = input1(self.framd1,'Input Warning Amount',0.45,0.49,)


         esubmit = tk.Button(self.framd1, text='Submit', relief=tk.FLAT, bg= 'white',
                            command=lambda:self.submit(self.framd1,self.inameentry,self.ispendentry,self.iwarningentry))
         esubmit.place(relx= 0.5, rely=0.55,anchor='center')

class dashboard_info():

   def __init__(self,window):
      self.window=window

   def display(self):
    m =navbar(window)

    che=backend.budget_table_exists()
    if che== False:
            m.nobudget('Cannot Show Budget And Category Info\n Because Budget Does Not Exist')
    else:
      #BUDGET DISPLAY FRAME
      #bug_info=backend.get_budget_info() gets a list of [unallocated fund,,total amount left to spend,total spent]
      self.fram = tk.Frame(self.window,bg=colback, width=700,height=180, padx=10)
      self.fram.place(x=180,y=40)
      
      # Get actual budget info from backend
      bug_info = backend.get_budget_info()
      unallocated = bug_info[0] if bug_info and len(bug_info) > 0 else 0
      total_left = bug_info[1] if bug_info and len(bug_info) > 1 else 0
      total_spent = bug_info[2] if bug_info and len(bug_info) > 2 else 0
       
      monnam = tk.Label(self.fram, text='Month',bg=colback,font=(None,40,'bold'),fg=colman)
      monnam.place(relx=0.05, rely=0.08)
      datnam= tk.Label(self.fram, text='Date Created',bg=colback,font=(None,20,'italic'),fg=colman)
      datnam.place(relx=0.05, rely=0.45)
      spenam= tk.Label(self.fram, text=f'Money To Spend: ${total_left:.2f}',bg=colback,font=(None,20,'bold'),fg=colman)
      spenam.place(relx=0.05, rely=0.7)
      
      #UNALLOCATED FUNDS DISPLAY FRAME
      self.fram1 = tk.Frame(self.window,bg=colback, width=330,height=85, padx=10)
      self.fram1.place(x=890, y=40)
      unam = tk.Label(self.fram1, text=f'Unallocated Funds: ${unallocated:.2f}',bg=colback,font=(None,15,'bold'),fg=colman)
      unam.place(relx=0.01,rely=0.3)

      #TOTAL SPENT DISPLAY FRAME
      self.fram2 = tk.Frame(self.window,bg=colback, width=330,height=85, padx=10)
      self.fram2.place(x=890, y=135)
      snam = tk.Label(self.fram2, text=f'TOTAL SPENT: ${total_spent:.2f}',bg=colback,font=(None,15,'bold'),fg=colman)
      snam.place(relx=0.01,rely=0.3)
      
      cat_nam=backend.get_category_names()
      cat_spend=backend.get_category_left_spend()  # returns list of category left to spent
      cat_spent=backend.get_category_spent()  # returns list of category spent amount
    
      #  checks wether it is above warning amount,or above the amount set, if it is above warning amount and below amount set 
      # colour=yellow, if it is above set amount colour=red, if it is below warning amount  colour= green, return colour
 

      #CATEGORY DISPLAY FRAMES - positions for up to 10 categories
      positions = [(180,250), (390,250), (600,250), (810,250), (1020,250),
                   (180,460), (390,460), (600,460), (810,460), (1020,460)]
      
      for i in range(len(cat_nam)):
         x, y = positions[i]
         wig = self.widget(x, y, cat_nam[i], 
                          cat_spend[i] if i < len(cat_spend) else 0, 
                          cat_spent[i] if i < len(cat_spent) else 0)
         catwarning=backend.check_category_warning(cat_nam[i])
         if catwarning == 'green':
            col= "#80B174"
         elif catwarning == 'yellow':
            col="#B0B174"
         elif catwarning == 'red':
            col= "#B17474"
         else:
            col = colback
            
         # Update the widget with category data and color
         for widget in wig.winfo_children():
            widget.configure(bg=col)
         catnam= tk.Label(wig,text=f'{cat_nam[i]}',bg=col,font=(None,15,'italic'),fg=colman)
         catnam.place(rely= 0.15, relx=0.5,anchor='center')
         catspend= tk.Label(wig,text=f'To Spend:\n${cat_spend[i]:.2f}' if i < len(cat_spend) else 'To Spend:\n$0.00',bg=col,font=(None,10,'italic'),fg=colman)
         catspend.place(rely= 0.4, relx=0.5,anchor='center')
         catspent= tk.Label(wig,text=f'Spent:\n${cat_spent[i]:.2f}' if i < len(cat_spent) else 'Spent:\n$0.00',bg=col,font=(None,10,'italic'),fg=colman)
         catspent.place(rely= 0.65, relx=0.5,anchor='center')
  
   def widget(self,a,b,cat_name='',cat_spend=0,cat_spent=0):
   
      self.wig = tk.Frame(self.window,bg='#FF9E42', width=200,height=200, padx=10)
      self.wig.place(x=a, y=b)
      label = tk.Label(self.wig,bg=colback)
      label.place(x=0,y=0)
      label.config(width=250,height=200)
      if cat_name:
         catnam= tk.Label(self.wig,text=f'{cat_name}',bg=colback,font=(None,15,'italic'),fg=colman)
         catnam.place(rely= 0.15, relx=0.5,anchor='center')
         catspend= tk.Label(self.wig,text=f'To Spend:\n${cat_spend:.2f}',bg=colback,font=(None,10,'italic'),fg=colman)
         catspend.place(rely= 0.4, relx=0.5,anchor='center')
         catspent= tk.Label(self.wig,text=f'Spent:\n${cat_spent:.2f}',bg=colback,font=(None,10,'italic'),fg=colman)
         catspent.place(rely= 0.65, relx=0.5,anchor='center')
      else:
         catnam= tk.Label(self.wig,text=f'No Category\n Here',bg=colback,font=(None,15,'italic'),fg=colman)
         catnam.place(rely= 0.5, relx=0.5,anchor='center')
      return self.wig
    
class profile_info():
    def __init__(self,window):
     self.window=window
   
    def update_credentials(self):
        new_username = self.username_entry.get().strip().lower()
        new_password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if new_username == '' or new_password == '':
            mg.showerror('Error', 'Please fill in all fields')
            return
        
        if new_password != confirm_password:
            mg.showerror('Error', 'Passwords do not match')
            return
        
        # Update username if changed
        if new_username != '' and new_username != backend.username:
            success, msg = backend.update_username(new_username)
            if not success:
                mg.showerror('Error', msg)
                return
        
        # Update password
        success, msg = backend.update_password(new_password)
        if success:
            mg.showinfo('Success', msg)
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')
            self.confirm_password_entry.delete(0, 'end')
        else:
            mg.showerror('Error', msg)
    
    def display(self):
        m = navbar(window)
        
        # Main frame for profile
        main_frame = tk.Frame(self.window, bg='white')
        main_frame.place(x=230, y=45, width=1050, height=640)
        
        # Title
        title = tk.Label(main_frame, text='Profile Settings', font=(None,25,'bold'), bg='white', fg=colback)
        title.place(relx=0.5, rely=0.05, anchor='center')
        
        # Edit Credentials Section
        cred_frame = tk.LabelFrame(main_frame, text='Edit Username & Password', bg=colback, fg=colman, font=(None,14,'bold'), padx=20, pady=15)
        cred_frame.place(relx=0.5, rely=0.15, anchor='center', width=450)
        
        # Current username display
        info = backend.get_userinfo()
        current_user = tk.Label(cred_frame, text=f'Current Username: {info[0]}', font=(None,11,'italic'), bg=colback, fg=colman)
        current_user.grid(row=0, column=0, columnspan=2, pady=(0,15))
        
        # New username entry
        tk.Label(cred_frame, text='New Username:', font=(None,11), bg=colback, fg=colman).grid(row=1, column=0, sticky='w', pady=5)
        self.username_entry = tk.Entry(cred_frame, relief=tk.FLAT, width=25)
        self.username_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # New password entry
        tk.Label(cred_frame, text='New Password:', font=(None,11), bg=colback, fg=colman).grid(row=2, column=0, sticky='w', pady=5)
        self.password_entry = tk.Entry(cred_frame, relief=tk.FLAT, width=25, show='*')
        self.password_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Confirm password entry
        tk.Label(cred_frame, text='Confirm Password:', font=(None,11), bg=colback, fg=colman).grid(row=3, column=0, sticky='w', pady=5)
        self.confirm_password_entry = tk.Entry(cred_frame, relief=tk.FLAT, width=25, show='*')
        self.confirm_password_entry.grid(row=3, column=1, pady=5, padx=5)
        
        # Update button
        update_btn = tk.Button(cred_frame, text='Update Profile', relief=tk.FLAT, bg='white', fg=colback, 
                             command=self.update_credentials, font=(None,11,'bold'))
        update_btn.grid(row=4, column=0, columnspan=2, pady=15)
        
        # Transaction History Section
        hist_frame = tk.LabelFrame(main_frame, text='Transaction History', bg=colback, fg=colman, font=(None,14,'bold'), padx=20, pady=10)
        hist_frame.place(relx=0.5, rely=0.52, anchor='center', width=700, height=280)
        
        # Create treeview for transactions
        columns = ('Name', 'Date', 'Amount', 'Category', 'Type')
        self.trans_tree = ttk.Treeview(hist_frame, columns=columns, show='headings', height=10)
        
        for col in columns:
            self.trans_tree.heading(col, text=col)
            self.trans_tree.column(col, width=130)
        
        self.trans_tree.pack(fill='both', expand=True, pady=5)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(hist_frame, orient='vertical', command=self.trans_tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.trans_tree.configure(yscrollcommand=scrollbar.set)
        
        # Load transactions
        self.load_transactions()
    
    def load_transactions(self):
        # Clear existing items
        for item in self.trans_tree.get_children():
            self.trans_tree.delete(item)
        
        # Get transactions from backend
        transactions = backend.get_transaction_history()
        
        if not transactions:
            self.trans_tree.insert('', 'end', values=('No transactions yet', '', '', '', ''))
        else:
            for trans in transactions:
                # Format date
                date_str = trans[1].strftime('%Y-%m-%d') if trans[1] else 'N/A'
                # Format amount with $ sign
                amount_str = f'${trans[2]:.2f}' if trans[2] else '$0.00'
                self.trans_tree.insert('', 'end', values=(trans[0], date_str, amount_str, trans[3], trans[5]))
   
class track_info():
    def __init__(self,window):
       self.window=window  
    
    def form(self,frame,name,inam,mon,cat,des,a,b):
         enam = tk.Label(frame, text=name,bg=colback,font=(None,20,'bold'),fg=colman)
         enam.place(relx= 0.5, rely=0.1,anchor='center')
         nameentry=input1(frame,inam,0.25,0.29,)
         spententry = input1(frame,mon,0.35,0.39,)
         categoryentry = input1(frame,cat,0.45,0.49,)
         desentry = input1(frame,des,0.55,0.59)

         esubmit = tk.Button(frame, text='Submit', relief=tk.FLAT, bg= 'white',
                            command= lambda:self.submit(frame,nameentry,spententry,categoryentry,desentry,a,b))
         esubmit.place(relx= 0.5, rely=0.75,anchor='center')

    def submit(self,frame,name,money,category,des,a,b):
        try:
            n= name.get().lower().strip()
            m = float(money.get().strip())
            c = category.get().lower().strip()
            e = des.get().lower().strip()
            my=  [money,name,category,des]

            if n == '' or c == '':
                mg.showerror('Info Error', 'Please Input In Every Field')
                self.iserror = True
            else:
                if frame == self.framd:
                    transaction_type = 'Expense'
                else:
                    transaction_type='Income'
                # Clear entry fields first
                for i in my:
                    i.delete(0,'end')
                # Insert the transaction into the backend
                backend.transaction_table_insert(n,m,c,e,transaction_type) 
                # Update category after transaction
                backend.update_category_after_transaction(c,m,transaction_type)
                # Check warning status for the category after transaction
                if c != 'unallocated' and c != '':
                    che= backend.check_category_warning(c)
                    if che == 'yellow':
                        mg.showwarning('Warning','You Are Reaching Your Category Limit')
                    elif che == 'red':
                        mg.showwarning('Warning','You Have Passed Your Category Limit')
                mg.showinfo(a,b)
                  
        except ValueError:
            mg.showerror('Info Value', 'Error Inputting Values')
            self.iserror = True
      

    def display(self): 
      m =navbar(window)
      check= backend.budget_table_exists()
      #
      if check == False:
            m.nobudget('Cannot Log Expenses And Income\n Because Budget Does Not Exist')
      else: 
        # EXPENSES FRAME
        self.framd = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd.place(x=230,y=45)

        self.form(self.framd,'Log Expense','Input Name Of Expense','Input Money Spent(Number)','Input Category(If None input Unallocated)',
                 'Input Description(Optional)','Expense','Expense Succesfully Logged')

        #INCOME FRAME
        self.framd1 = tk.Frame(self.window,bg=colback, width=500,height=590, padx=10)
        self.framd1.place(x=750,y=45)
        self.form(self.framd1,'Log Income','Input Name Of Income','Input Money Gained(Number)','Input Category(If None input Unallocated)',
                 'Input Description(Optional)','Income','Income Succesfully Logged')

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
        dash = image(os.path.join(BASE_DIR, "dash.png")) 
        icona = image(os.path.join(BASE_DIR, "logon.png"))
        track = image(os.path.join(BASE_DIR, "track.png"))
        cren = image(os.path.join(BASE_DIR, "create.png"))
        prof = image(os.path.join(BASE_DIR, "prof.png"))
        
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
       self.destroy(0.05,self.home1,os.path.join(BASE_DIR, "logon.png"))
       home_info()
       
    def dashboard1(self):
        self.destroy(0.22, self.dashboard1,os.path.join(BASE_DIR, "activedash.png"))
        m = dashboard_info(window)
        window.title('Dashboard')
        m.display()
      
    def track1(self):
        self.destroy(0.39, self.track1,os.path.join(BASE_DIR, "activetrack.png"))
        m = track_info(window)
        window.title('Track')
        m.display()
      
    def create1(self):
        self.destroy(0.56, self.create1,os.path.join(BASE_DIR, "activecrea.png"))
        m = create_info(window)
        window.title('Create')
        m.display()

    def profile1(self):
        self.destroy(0.73,self.profile1,os.path.join(BASE_DIR, "activeprof.png"))
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

class loginsignin():
 
 def check_signin(self):
   password1=self.passe.get()
   user1=self.usere.get().strip().lower()

   if self.passe.get() == '' and self.usere.get() == '':
      mg.showerror('Input Error','Please Input In every field')
   else:
    l= backend.get_signin(user1,password1)
    if l == True:
     mg.showinfo('Sign In','Sign In Successful')
     backend.get_username(user1)
     for widget in window.winfo_children():
          widget.destroy()
   
     home_info()
     nav= navbar(window)
     nav.frame()
    else:
       mg.showerror('Sign In Error','Could Not Find Username')
  
 def create_signup(self):
     global username,password
     username= self.usere1.get().strip().lower()
     password=self.passe1.get()
     
     if self.passe1.get() == '' or self.usere1.get() == '':
      mg.showerror('Input Error','Please Input In every field')
     else:
      l= backend.get_signup(username,password)
      if l == True: 
        backend.get_username(username)
        mg.showinfo('Sign Up','Sign Up Successful')
        for widget in window.winfo_children():
         widget.destroy()

        home_info()
        nav= navbar(window)
        nav.frame()

      else:
         mg.showerror('Sign Up Error','Username Already Exists')
       
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
   self.passe1 = tk.Entry(window,bg=colback,relief=tk.FLAT,fg=colman,show='*')
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
window.iconbitmap(os.path.join(BASE_DIR, "logoico.ico"))

window.title('Guide')
icon3 = Image.open(os.path.join(BASE_DIR, "s.jpg"))
icon5 = icon3.resize((600,500))
icon4 = ImageTk.PhotoImage(icon5)
picture5 = tk.Label(window, image=icon4)
picture5.image = icon4
picture5.pack(side= 'left', fill='y')
picture5.config(width=260)

logo = Image.open(os.path.join(BASE_DIR, "logoico.ico"))
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