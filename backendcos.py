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
                    Username TEXT UNIQUE NOT NULL,
                    Password TEXT
                );
            """)
            self.connection.commit()
            print("Users table created")
        except Exception as error:
            print(f"Error creating users table: {error}")

    def create_budget_table(self,a):
        global budget_name
        try:
            budget_name = a + '_budget'
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

    def budget_table_insert(self,b,c,d,e):
        try:
            insert_query = sql.SQL("""
                INSERT INTO {} (Month, Total_amount, Warning_amount, Date_creted)
                VALUES (%s, %s, %s);
            """).format(sql.Identifier(budget_name))
            data_to_insert = (b, c, d,e)

            self.cursor.execute(insert_query,data_to_insert)
            print("Data inserted successfully")
        except Exception as error:
            print(f"Error inserting data: {error}")


    def create_Category_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Category(
                    Id SERIAL PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Money_allocated FLOAT NOT NULL,
                    Warning_amount FLOAT NOT NULL,
                    Date DATE NOT NULL
                );
            """)
            self.connection.commit()
            print("Category table crated.")
        except Exception as error:
            print(f"Error creating category table: {error}")

    

    def create_Transaction_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Transaction(
                    Id SERIAL PRIMARY KEY,
                    Date DATE NOT NULL,
                    Amount REAL NOT NULL,
                    Category TEXT NOT NULL,
                    Description TEXT,
                    Type TEXT CHECK (type IN ('income', 'expense')) NOT NULL
                );
            """)
            self.connection.commit()
            print("Transaction table created.")
        except Exception as error:
            print(f"Error creating transactions table: {error}")

    def delete_table(self, table_name):
        """Delete a table by name"""
        try:
            self.cursor.execute(sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table_name)))
            self.connection.commit()
            print(f"Table '{table_name}' deleted.")
        except Exception as error:
            print(f"Error deleting table '{table_name}': {error}")

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
