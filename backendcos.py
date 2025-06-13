# for the back end create a class that has methods to open a connnection with postgress and to input entries into tables
import psycopg2
from psycopg2 import sql


#create a class that edits/creates/deletes tables, one method that automatically creates a table for users in the database
# Another that creates a table named budget if it doesnt exist
#another that creates a table for income and expenses
# method that deletes tables
class Connect:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def createdbase(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                port='5432',
                dbname='postgres',
                user='postgres',
                password='cos101'  
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            new_dbname = 'cosexamproject'
            create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname))
            self.cursor.execute(create_db_query)

            print(f"Database '{new_dbname}' created successfully")

        except psycopg2.errors.DuplicateDatabase:
            print(f"Database '{new_dbname}' already exists")

        except Exception as error:
            print(f"Error creating the database: {error}")

        finally:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

    def connectserv(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                port='5432',
                dbname='cosexamproject',
                user='postgres',
                password='cos101'
            )
            self.cursor = self.connection.cursor()
            print("Connected to 'cosexamproject' database successfully")
        except Exception as error:
            print(f"Error connecting to project database: {error}")

    def create_users_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT
                );
            """)
            self.connection.commit()
            print("Users table created")
        except Exception as error:
            print(f"Error creating users table: {error}")

    def get_username(self,u):
        
        try:
            self.cursor.execute("""
                SELECT username from users WHERE username = %s;
            """, (u,))
            self.username= u
        except Exception as error:
            print(f"Username '{u}' doesn't exist")

#Signup
    def signup(self, u, p):
        try:
            # Check if username already exists
            self.cursor.execute("""
                SELECT 1 FROM users WHERE username = %s;
            """, (u,))
            if self.cursor.fetchone():
                print(f"Username '{u}' is already taken.")
                return False

            # Insert new user
            self.cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (%s, %s);
            """, (u, p))
            self.connection.commit()
            print(f"User '{u}' signed up successfully.")
            return True

        except Exception as error:
            print(f"Error during signup: {error}")
            return False
        
#Signin 
    def signin(self, u, p):
        try:
            # Fetch the stored password for the given username
            self.cursor.execute("""
                SELECT password FROM users WHERE username = %s;
            """, (u,))
            result = self.cursor.fetchone()

            if result is None:
                print("Username not found.")
                return False

            stored_password = result[0]

            if stored_password == p:
                print("Login successful.")
                return True
            else:
                print("Incorrect password.")
                return False

        except Exception as error:
            print(f"Error during signin: {error}")
            return False

    def create_budget_table(self):
        global budget_name
        try:
            budget_name = self.username + '_budget'
            query = sql.SQL("""
                 CREATE TABLE IF NOT EXISTS {} (
                    Id SERIAL PRIMARY KEY,
                    Month TEXT NOT NULL,
                    Total_amount REAL NOT NULL,
                    Warning_amount REAL NOT NULL
                    Date_created DATE NOT NULL
                );
            """).format(sql.Identifier(budget_name))

            self.cursor.execute(query)
            self.connection.commit()
            print(f"Budget table '{budget_name}' created")
        except Exception as error:
            print(f"Error creating budget table '{budget_name}': {error}")

#function to get budget


    def budget_table_insert(self,b,c,d,e):
        try:
            insert_query = sql.SQL("""
                INSERT INTO {} (Month, Total_amount, Warning_amount, Date_creted)
                VALUES (%s, %s, %s);
            """).format(sql.Identifier(budget_name))
            data_to_insert = (b, c, d, e)

            self.cursor.execute(insert_query,data_to_insert)
            print("Data inserted successfully")
        except Exception as error:
            print(f"Error inserting data: {error}")

    def budget_table_exists(self):
        try:
            table_name = budget_name
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' AND table_name = %s
                );
            """, (table_name,))
            exists = self.cursor.fetchone()[0]
            print(f"Budget table '{table_name}' exists: {exists}")
            return exists
        except Exception as error:
            print(f"Error checking for budget table existence: {error}")
            return False

    def create_category_table(self):
            global category_name
            try:
                category_name = self.username + 'category'
                query = sql.SQL("""
                    CREATE TABLE IF NOT EXISTS Category(
                        Id SERIAL PRIMARY KEY,
                        Name TEXT NOT NULL,
                        Money_allocated FLOAT NOT NULL,
                        Warning_amount FLOAT NOT NULL,
                        Total_spent  FLOAT DEFAULT 0,
                        Total_left_to_spend FLOAT,
                        Date DATE NOT NULL
                    );
                """).format(sql.Identifier(category_name))

                self.cursor.execute(query)            
                self.connection.commit()
                print(f"Category table '{category_name}' created")
            except Exception as error:
                print(f"Error creating category table: '{category_name}' : {error}")

    def category_table_insert(self,b,c,d,e):
        try:
            insert_query = sql.SQL("""
                INSERT INTO {} (Name, Money_allocated, Warning_amount, Date)
                VALUES (%s, %s, %s, %s);
            """).format(sql.Identifier(category_name))
            data_to_insert = (b, c, d, e)

            self.cursor.execute(insert_query,data_to_insert)
            print("Data inserted successfully")
        except Exception as error:
            print(f"Error inserting data: {error}")

#total allocated to catgories
    def get_total_in_categories(self):
        try:
            self.cursor.execute(sql.SQL("""
                SELECT SUM(Money_allocated) FROM {};
            """).format(sql.Identifier(category_name)))
            result = self.cursor.fetchone()[0]
            return result if result else 0.0
        except Exception as error:
            print(f"Error calculating total in categories: {error}")
            return 0.0


# unallocated funds
    def get_unallocated_funds(self):
        try:
            # Get total budget
            self.cursor.execute(sql.SQL("""
                SELECT Total_amount FROM {} ORDER BY Date_created DESC LIMIT 1;
            """).format(sql.Identifier(budget_name)))
            budget = self.cursor.fetchone()
            if not budget:
                return 0.0
            total_budget = budget[0]

            # Reuse total in categories
            total_allocated = self.get_total_in_categories()
            return total_budget - total_allocated
        except Exception as error:
            print(f"Error calculating unallocated funds: {error}")
            return 0.0


    def create_transaction_table(self):
        global transaction_name 
        try:
            transaction_name = self.username + 'Transaction'
            query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS Transaction(
                    Id SERIAL PRIMARY KEY,
                    Name TEXT NOT NULL
                    Date DATE NOT NULL,
                    Amount REAL NOT NULL,
                    Category TEXT NOT NULL,
                    Description TEXT,
                    Type TEXT NOT NULL
                );
            """).format(sql.Identifier(transaction_name))

            self.cursor.execute(query)
            self.connection.commit()
            print(f"Transaction table created '{transaction_name}' created")
        except Exception as error:
            print(f"Error creating transactions table: '{transaction_name}' : {error}")

    def transaction_table_insert(self,b,c,d,e,f,g):
        try:
            insert_query = sql.SQL("""
                INSERT INTO {} (Date, Amount, Category, Descripton, Type)
                VALUES (%s, %s, %s, %s, %s, %s);
            """).format(sql.Identifier(transaction_name))
            data_to_insert = (b, c, d, e, f, g)

            self.cursor.execute(insert_query,data_to_insert)
            print("Data inserted successfully")
        except Exception as error:
            print(f"Error inserting data: {error}")

#total spent from expenses
    def get_total_spent(self):
        try:
            self.cursor.execute(sql.SQL("""
                SELECT SUM(Amount) FROM {} WHERE Type = 'Expense';
            """).format(sql.Identifier(transaction_name)))
            result = self.cursor.fetchone()[0]
            return result if result else 0.0
        except Exception as error:
            print(f"Error calculating total spent: {error}")
            return 0.0
        
#total spent from each category
    def get_total_spent_cat(self,a,b,c):
        try:
            # Step 1: Get allocated budget per category
            self.cursor.execute(sql.SQL("""
                SELECT Name, Total_spent
                FROM {}
            """).format(sql.Identifier(a)))
            category_data = self.cursor.fetchall()
            
            self.cursor.execute(sql.SQL("""
                SELECT Name, Money_allocated
                FROM {}
            """).format(sql.Identifier(a)))
            category_data1 = self.cursor.fetchall()

            if c== 'Expense':
                total_spent = category_data + b
            else:
                total_spent = category_data - b
            
            total_left_to_spend = category_data1 - total_spent

            self.cursor.execute(sql.SQL("""
            UPDATE {}
            SET total_spent = %s,
                total_left_to_spend = %s
            WHERE Name = %s
        """).format(sql.Identifier(category_name)), (total_spent, total_left_to_spend))


        except Exception as error:
            print(f"Error calculating remaining budget per category: {error}")
            return {}
        



#total left after subtracting categories from budget allocated
    def get_total_left(self):
        try:
            # Get total budget
            self.cursor.execute(sql.SQL("""
                SELECT Total_amount FROM {} ORDER BY Date_created DESC LIMIT 1;
            """).format(sql.Identifier(budget_name)))
            budget = self.cursor.fetchone()
            if not budget:
                return 0.0
            total_budget = budget[0]

            # Get total spent
            total_spent = self.get_total_spent()
            return total_budget - total_spent
        except Exception as error:
            print(f"Error calculating total left: {error}")
            return 0.0
        
#warning amount
    def check_category_warning(self, category_name, category_title):
        try:
            # Step 1: Get the warning amount and money allocated
            self.cursor.execute(sql.SQL("""
                SELECT Warning_amount, Money_allocated
                FROM {}
                WHERE Name = %s
            """).format(sql.Identifier(category_name)), (category_title,))
            
            result = self.cursor.fetchone()
            if not result:
                print(f"Category '{category_title}' not found in table '{category_name}'")
                return False

            warning_amount, allocated_amount = result

            # Step 2: Get total expenses for this category from the transactions table
            self.cursor.execute(sql.SQL("""
                SELECT COALESCE(SUM(Amount), 0)
                FROM {}
                WHERE Category = %s AND Type = 'Expense'
            """).format(sql.Identifier(transaction_name)), (category_title,))
            
            total_spent = self.cursor.fetchone()[0]

            print(f"Total spent in '{category_title}': {total_spent} | Warning level: {warning_amount}")

            # Step 3: Check if spent exceeds or meets warning
            if total_spent >= warning_amount:
                print(f"⚠️ Warning: You have reached the warning threshold for '{category_title}'!")
                return True
            else:
                return False

        except Exception as error:
            print(f"Error checking warning level for category '{category_title}': {error}")
            return False


    def create_calculation_table(self):
        global calculate_name 
        try:
            calculation_name = self.username + 'calculation'
            query = sql.SQL("""
                CREATE TABLE IF NOT EXISTS calculation(
                    Id SERIAL PRIMARY KEY,
                    unallocated_funds REAL NOT NULL
                    total_amounts_spent REAL NOT NULL,
                    total_allocated_to_category REAL NOT NULL
                
                            
                );
            """).format(sql.Identifier(calculation_name))

            self.cursor.execute(query)
            self.connection.commit()
            print(f"Transaction table created '{calculation_name}' created")
        except Exception as error:
            print(f"Error creating transactions table: '{calculation_name}' : {error}")

    def get_category_names(self, category_table):
        try:
            self.cursor.execute(sql.SQL("""
                SELECT Name FROM {}
            """).format(sql.Identifier(category_table)))
            
            results = self.cursor.fetchall()
            return [row[0] for row in results]
        
        except Exception as error:
            print(f"Error getting category names: {error}")
            return []
        
    def money_allocated(self):
        try:
            # Replace 'category_name' and 'budget_name' with your actual global variables if needed
            query = sql.SQL("""
                SELECT c.Money_allocated, c.Date, b.Month
                FROM {} AS c
                JOIN {} AS b ON DATE_TRUNC('month', c.Date) = DATE_TRUNC('month', b.Date_created);
            """).format(
                sql.Identifier(category_name),
                sql.Identifier(budget_name)
            )

            self.cursor.execute(query)
            results = self.cursor.fetchall()

            # Each result will be a tuple: (money_allocated, date, month)
            return results

        except Exception as error:
            print(f"Error retrieving category allocations with dates and months: {error}")
            return []


    def get_money_left_list(self, category_table, transaction_table):
        try:
            self.cursor.execute(sql.SQL("""
                SELECT Name, Money_allocated FROM {}
            """).format(sql.Identifier(category_table)))
            
            categories = self.cursor.fetchall()
            money_left_list = []

            for category_name, allocated in categories:
                # Get total expenses
                self.cursor.execute(sql.SQL("""
                    SELECT COALESCE(SUM(Amount), 0)
                    FROM {}
                    WHERE Category = %s AND Type = 'Expense'
                """).format(sql.Identifier(transaction_table)), (category_name,))
                total_expense = self.cursor.fetchone()[0]

                # Get total income
                self.cursor.execute(sql.SQL("""
                    SELECT COALESCE(SUM(Amount), 0)
                    FROM {}
                    WHERE Category = %s AND Type = 'Income'
                """).format(sql.Identifier(transaction_table)), (category_name,))
                total_income = self.cursor.fetchone()[0]

                # Compute money left
                money_left = allocated - total_expense + total_income
                money_left_list.append(money_left)

            return money_left_list

        except Exception as error:
            print(f"Error calculating money left: {error}")
            return []



    def delete_table(self):
        """Delete a table by name"""
        try:
            self.cursor.execute(sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(budget_name, category_name, transaction_name)))
            self.connection.commit()
            print(f"Table '{budget_name, category_name, transaction_name}' deleted.")
        except Exception as error:
            print(f"Error deleting table '{budget_name, category_name, transaction_name}': {error}")

    def close(self):
        """Close the DB connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")
    

call = Connect()
call.createdbase()
call.connectserv()
call.create_users_table()
def budget():
    budget_exists = True
    return budget_exists
