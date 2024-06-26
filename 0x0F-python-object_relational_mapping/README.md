# README.md

## Tasks

### 0. Get all states

Write a script that lists all states from the database `hbtn_0e_0_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 1. Filter states

Write a script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 2. Filter states by user input

Write a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name searched (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- You must use format to create the SQL query with the user input
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 3. SQL Injection...

Write a script that takes in arguments and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument, but this time, write one that is safe from MySQL injections!

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name searched (safe from MySQL injection)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- Results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 4. Cities by states

Write a script that lists all cities from the database `hbtn_0e_4_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only `execute()` once
- Results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 5. All cities by state

Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name (SQL injection free!)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by cities.id
- You can use only `execute()` once
- The results must be displayed as they are in the example provided
- Your code should not be executed when imported

### 6. First state model

Write a Python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
- Inherits from Base
- Links to the MySQL table states
- Class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
- Class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- You must use the module SQLAlchemy
- Your script should connect to a MySQL server running on localhost at port 3306
- WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

### 7. All states via SQLAlchemy

Write a script that lists all State objects from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

### 8. First state

Write a script that prints the first State object from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state
- Your script should connect to a MySQL server running on localhost at port 3306
- If the table states is empty, print Nothing followed by a new line
- Your code should not be executed when imported

### 9. Contains `a`

Write a script that lists all State objects that contain the letter a from the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state
- Your script should connect to a MySQL server running on localhost at port 3306
- Results must be sorted in ascending order by states.id
- The results must be displayed as they are in the example below
- Your code should not be executed when imported

### 10. Get a state

Write a script that prints the State object with the name passed as argument from the database `hbtn_0e_6_usa`.

- Your script should take 4 arguments: mysql username, mysql password, database name, and state name to search (SQL injection free!)
- You must use the module SQLAlchemy
- You must import State and Base from model_state
- Your script should connect to a MySQL server running on localhost at port 3306
- You can assume you have one record with the state name to search
- Results must display the states.id
- If no state has the name you searched for, display Not found
- Your code should not be executed when imported

### 11. Add a new state

Write a script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.

- Your script should take 3 arguments: mysql username, mysql password, and database name
- You must use the module SQLAlchemy
- You must import State and Base from model_state
- Your script should connect to a MySQL server running on localhost at port 3306
- Print the new states.id after creation
- Your code should not be executed when imported
