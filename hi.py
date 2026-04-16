import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class BudgetSimulator:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Budget Simulator - Pan-Atlantic University")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Initialize data structures
        self.monthly_budget = 0.0
        self.categories = {}  # Store budget allocations per category
        self.transactions = []  # Store all income and expense transactions
        self.category_spent = {}  # Track spending per category
        
        # Create the GUI
        self.create_widgets()
        
    def create_widgets(self):
        # Main title
        title_label = tk.Label(self.root, text="Personal Budget Simulator", 
                              font=("Arial", 18, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title_label.pack(pady=10)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Budget Setup Tab
        self.setup_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.setup_frame, text="Budget Setup")
        self.create_budget_setup()
        
        # Transaction Tab
        self.transaction_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.transaction_frame, text="Add Transaction")
        self.create_transaction_tab()
        
        # Overview Tab
        self.overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.overview_frame, text="Budget Overview")
        self.create_overview_tab()
        
    def create_budget_setup(self):
        # Monthly budget section
        budget_frame = ttk.LabelFrame(self.setup_frame, text="Set Monthly Budget", padding=10)
        budget_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(budget_frame, text="Total Monthly Budget ($):").pack(anchor='w')
        self.budget_entry = tk.Entry(budget_frame, font=("Arial", 12))
        self.budget_entry.pack(fill='x', pady=5)
        
        ttk.Button(budget_frame, text="Set Budget", command=self.set_monthly_budget).pack(pady=5)
        
        # Budget categories section
        categories_frame = ttk.LabelFrame(self.setup_frame, text="Budget Categories", padding=10)
        categories_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Category input
        input_frame = ttk.Frame(categories_frame)
        input_frame.pack(fill='x', pady=5)
        
        tk.Label(input_frame, text="Category:").grid(row=0, column=0, sticky='w', padx=5)
        self.category_entry = tk.Entry(input_frame)
        self.category_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(input_frame, text="Allocated Amount ($):").grid(row=0, column=2, sticky='w', padx=5)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=0, column=3, padx=5)
         
        ttk.Button(input_frame, text="Add Category", command=self.add_category).grid(row=0, column=4, padx=5)
        
        # Categories list
        self.categories_listbox = tk.Listbox(categories_frame, height=8)
        self.categories_listbox.pack(fill='both', expand=True, pady=5)
        
        ttk.Button(categories_frame, text="Remove Selected", command=self.remove_category).pack(pady=5)
        
    def create_transaction_tab(self):
        # Transaction input section
        trans_frame = ttk.LabelFrame(self.transaction_frame, text="Log Income/Expenses", padding=10)
        trans_frame.pack(fill='x', padx=10, pady=5)
        
        # Date input
        tk.Label(trans_frame, text="Date:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.date_entry = tk.Entry(trans_frame)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Amount input
        tk.Label(trans_frame, text="Amount ($):").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.trans_amount_entry = tk.Entry(trans_frame)
        self.trans_amount_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Category selection
        tk.Label(trans_frame, text="Category:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(trans_frame, textvariable=self.category_var, state="readonly")
        self.category_combo.grid(row=2, column=1, padx=5, pady=5)
        
        # Description input (optional)
        tk.Label(trans_frame, text="Description (Optional):").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.desc_entry = tk.Entry(trans_frame, width=30)
        self.desc_entry.grid(row=3, column=1, columnspan=2, padx=5, pady=5, sticky='ew')
        
        # Transaction type
        tk.Label(trans_frame, text="Type:").grid(row=4, column=0, sticky='w', padx=5, pady=5)
        self.trans_type_var = tk.StringVar(value="Expense")
        type_frame = ttk.Frame(trans_frame)
        type_frame.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        
        ttk.Radiobutton(type_frame, text="Income", variable=self.trans_type_var, value="Income").pack(side='left')
        ttk.Radiobutton(type_frame, text="Expense", variable=self.trans_type_var, value="Expense").pack(side='left')
        
        ttk.Button(trans_frame, text="Add Transaction", command=self.add_transaction).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Transaction history
        history_frame = ttk.LabelFrame(self.transaction_frame, text="Transaction History", padding=10)
        history_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Create treeview for transaction history
        columns = ('Date', 'Type', 'Category', 'Amount', 'Description')
        self.trans_tree = ttk.Treeview(history_frame, columns=columns, show='headings', height=8)
         
        for col in columns:
            self.trans_tree.heading(col, text=col)
            self.trans_tree.column(col, width=100)
        
        self.trans_tree.pack(fill='both', expand=True)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(history_frame, orient='vertical', command=self.trans_tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.trans_tree.configure(yscrollcommand=scrollbar.set)
        
    def create_overview_tab(self):
        # Budget summary section
        summary_frame = ttk.LabelFrame(self.overview_frame, text="Budget Summary", padding=10)
        summary_frame.pack(fill='x', padx=10, pady=5)
        
        self.summary_text = tk.Text(summary_frame, height=12, wrap='word', state='disabled')
        self.summary_text.pack(fill='both', expand=True)
        
        # Update button
        ttk.Button(summary_frame, text="Refresh Overview", command=self.update_overview).pack(pady=5)
        
        # Alerts section
        alerts_frame = ttk.LabelFrame(self.overview_frame, text="Budget Alerts", padding=10)
        alerts_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        self.alerts_text = tk.Text(alerts_frame, height=6, wrap='word', state='disabled', bg='#ffe6e6')
        self.alerts_text.pack(fill='both', expand=True)
        
    def set_monthly_budget(self):
        # Set the total monthly budget amount
        try:
            budget = float(self.budget_entry.get())
            if budget <= 0:
                messagebox.showerror("Error", "Budget must be a positive number")
                return
            
            self.monthly_budget = budget
            messagebox.showinfo("Success", f"Monthly budget set to ${budget:.2f}")
            self.budget_entry.delete(0, tk.END)
            self.update_overview()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def add_category(self):
        # Add a new budget category with allocated amount
        category = self.category_entry.get().strip()
        try:
            amount = float(self.amount_entry.get())
            
            if not category:
                messagebox.showerror("Error", "Please enter a category name")
                return
            
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            # Check if total allocation exceeds budget
            total_allocated = sum(self.categories.values()) + amount
            if total_allocated > self.monthly_budget and self.monthly_budget > 0:
                messagebox.showwarning("Warning", 
                    f"Total allocation (${total_allocated:.2f}) exceeds monthly budget (${self.monthly_budget:.2f})")
            
            # Add category
            self.categories[category] = amount
            if category not in self.category_spent:
                self.category_spent[category] = 0.0
            
            # Update displays
            self.update_categories_display()
            self.update_category_combo()
            
            # Clear inputs
            self.category_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            
            messagebox.showinfo("Success", f"Category '{category}' added with ${amount:.2f} allocation")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    
    def remove_category(self):
        #both
        # Remove selected category from the list
        selection = self.categories_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a category to remove")
            return
        
        # Get category name from selection
        category_text = self.categories_listbox.get(selection[0])
        category_name = category_text.split(" - ")[0]
        
        # Remove from data structures
        if category_name in self.categories:
            del self.categories[category_name]
        if category_name in self.category_spent:
            del self.category_spent[category_name]
        
        # Update displays
        self.update_categories_display()
        self.update_category_combo()
        messagebox.showinfo("Success", f"Category '{category_name}' removed")
    
    def update_categories_display(self):
        # Update the categories listbox display
        self.categories_listbox.delete(0, tk.END)
        for category, amount in self.categories.items():
            spent = self.category_spent.get(category, 0.0)
            remaining = amount - spent
            self.categories_listbox.insert(tk.END, 
                f"{category} - Allocated: ${amount:.2f}, Spent: ${spent:.2f}, Remaining: ${remaining:.2f}")
    
    def update_category_combo(self):
        # Update the category combobox with available categories
        categories = list(self.categories.keys())
        self.category_combo['values'] = categories
        if categories and not self.category_var.get():
            self.category_var.set(categories[0])
    
    def add_transaction(self):
        # Add income or expense transaction
        try:
            date = self.date_entry.get().strip()
            amount = float(self.trans_amount_entry.get())
            category = self.category_var.get()
            description = self.desc_entry.get().strip()
            trans_type = self.trans_type_var.get()
            
            # Validate inputs
            if not date:
                messagebox.showerror("Error", "Please enter a date")
                return
            
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            if not category and trans_type == "Expense":
                messagebox.showerror("Error", "Please select a category for expenses")
                return
            
            # For expenses, check if category exists and update spending
            if trans_type == "Expense":
                if category not in self.categories:
                    messagebox.showerror("Error", "Selected category does not exist")
                    return
                
                # Update category spending
                self.category_spent[category] = self.category_spent.get(category, 0.0) + amount
            
            # Add transaction to history
            transaction = {
                'date': date,
                'type': trans_type,
                'category': category if category else 'General',
                'amount': amount,
                'description': description
            }
            self.transactions.append(transaction)
            
            # Update transaction tree
            self.trans_tree.insert('', 'end', values=(
                date, trans_type, category or 'General', f"${amount:.2f}", description
            ))
            
            # Clear inputs
            self.date_entry.delete(0, tk.END)
            self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
            self.trans_amount_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            
            # Update displays
            self.update_categories_display()
            self.update_overview()
            self.check_alerts()
            
            messagebox.showinfo("Success", f"{trans_type} of ${amount:.2f} added successfully")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount")
    
    def update_overview(self):
        # Update the budget overview display
        self.summary_text.config(state='normal')
        self.summary_text.delete(1.0, tk.END)
        
        # Calculate totals
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        net_balance = total_income - total_expenses
        
        # Calculate category spending
        total_allocated = sum(self.categories.values())
        unallocated = self.monthly_budget - total_allocated if self.monthly_budget > 0 else 0
        
        # Build summary text
        summary = f"""BUDGET OVERVIEW
{'='*50}

Monthly Budget: ${self.monthly_budget:.2f}
Total Allocated: ${total_allocated:.2f}
Unallocated Funds: ${unallocated:.2f}

INCOME & EXPENSES
{'='*50}
Total Income: ${total_income:.2f}
Total Expenses: ${total_expenses:.2f}
Net Balance: ${net_balance:.2f}

CATEGORY BREAKDOWN
{'='*50}
"""
        
        for category, allocated in self.categories.items():
            spent = self.category_spent.get(category, 0.0)
            remaining = allocated - spent
            percentage = (spent / allocated * 100) if allocated > 0 else 0
            
            summary += f"{category}:\n"
            summary += f"  Allocated: ${allocated:.2f}\n"
            summary += f"  Spent: ${spent:.2f} ({percentage:.1f}%)\n"
            summary += f"  Remaining: ${remaining:.2f}\n\n"
        
        self.summary_text.insert(1.0, summary)
        self.summary_text.config(state='disabled')
    
    def check_alerts(self):
        # Check for budget alerts and warnings
        self.alerts_text.config(state='normal')
        self.alerts_text.delete(1.0, tk.END)
        
        alerts = []
        
        # Check for overspending in categories
        for category, allocated in self.categories.items():
            spent = self.category_spent.get(category, 0.0)
            
            if spent > allocated:
                alerts.append(f"⚠️ OVERSPENDING: {category} - Spent ${spent:.2f}, Budget ${allocated:.2f}")
            elif spent > allocated * 0.8:  # 80% threshold
                remaining = allocated - spent
                alerts.append(f"⚠️ APPROACHING LIMIT: {category} - Only ${remaining:.2f} remaining")
        
        # Check total budget
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'Expense')
        if self.monthly_budget > 0 and total_expenses > self.monthly_budget:
            alerts.append(f"🚨 BUDGET EXCEEDED: Total expenses ${total_expenses:.2f} exceed monthly budget ${self.monthly_budget:.2f}")
        
        # Check remaining balance
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'Income')
        net_balance = total_income - total_expenses
        if net_balance < 0:
            alerts.append(f"🚨 NEGATIVE BALANCE: Current balance is ${net_balance:.2f}")
        
        # Display alerts
        if alerts:
            alert_text = "BUDGET ALERTS:\n" + "\n".join(alerts)
        else:
            alert_text = "✅ No budget alerts. You're staying within your limits!"
        
        self.alerts_text.insert(1.0, alert_text)
        self.alerts_text.config(state='disabled')

def main():
    # Create and run the application
    root = tk.Tk()
    app = BudgetSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()