# for the back end create a class that has methods to open a connnection with postgress and to input entries into tables
import psycopg2
from psycopg2 import sql



#create a class that edits/creates/deletes tables, one method that automatically creates a table for users in the database
# Another that creates a table named budget if it doesnt exist
#another that creates a table for income and expenses
# method that deletes tables
class connect:
 
 def createdbase(self):
  try:
    self.connection = psycopg2.connect(
        host='localhost',
        port='5432',
        dbname='postgres',
        user='postgres',
        password='cos102'
    )
    
    self.connection.autocommit = True 
    print("Connection to PostgreSQL server successful")
    cursor = self.connection.cursor()
    new_dbname = 'cosexamproject'

    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname))


    cursor.execute(create_db_query)
    print(f"Database '{new_dbname}' created successfully")

    cursor.close()
    self.connection.close()

  except Exception as error:
    print(f"Error creating the database: {error}")

 def connectserv(self):
  try:
    self.connection = psycopg2.connect(
        host='localhost',
        port='5432',
        dbname='cosexamproject',
        user='postgres',
        password='cos102'
    )
    print("Connection to PostgreSQL server successful")
  except Exception as error:
    print(f"Error connecting to Postgre Server: {error}")


call = connect()
call.connectserv
def budget():
 budget_exists = True
 return budget_exists

