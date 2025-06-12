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
                password='cos102'
            )
            self.cursor = self.connection.cursor()
            print("Connected to 'cosexamproject' database successfully")
        except Exception as error:
            print(f"Error connecting to project database: {error}")

    def create_users_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    Id SERIAL PRIMARY KEY,
                    Username TEXT UNIQUE NOT NULL,
                    Password TEXT
                );
            """)
            self.connection.commit()
            print("Users table created")
        except Exception as error:
            print(f"Error creating users table: {error}")

    def create_budget_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Budget (
                    Id SERIAL PRIMARY KEY,
                    User_id INTEGER REFERENCES users(Id),
                    Month TEXT NOT NULL,
                    Total_amount REAL NOT NULL,
                    Unallocated_funds REAL NOT NULL
                );
            """)
            self.connection.commit()
            print("Budget table created")
        except Exception as error:
            print(f"Error creating budget table: {error}")

    def create_Category_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS Category
                    Id SERIAL PRIMARY KEY,
                    User_id INTEGER REFERENCES user(id),
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
                CREATE TABLE IF NOT EXISTS Tranaction(
                    Id SERIAL PRIMARY KEY,
                    User_id INTEGER REFERENCES users(id),
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
call.connectserv
def budget():
 budget_exists = True
 return budget_exists