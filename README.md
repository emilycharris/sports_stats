# sports_stats
database homework using sports stats from Duke mens basketball 14-15 season

_This assignment was completed as part of my work at The Iron Yard._

**Assignment Description:**

Let's create a program to input and search sports data on athletes.

Sports statistics are a fantastic use case for storing data that can be viewed best in a table. Let's build a "search engine" that allows you to add statistics for players into a database and also search on certain criteria.

**Objectives**
- Understand fundamentals of Database Schema design.
- Understand basic SQL syntax to:
- create tables
- query for data
- insert data
- Create helper functions to allow for easier interaction with your database.

**Deliverables**

I am expecting you to deliver a program that when run will ask if i'd like to search for data or create data. It is up to you to make your search as flexible as you would like. Can I search by name? Can I search by position? Can I search by age? Make an option for whatever you think best fits your data. And for inserting new data - make it a convenient experience. Prompt me for every column value as I enter it.

**Normal Mode**

- Design a database structure (schema) that will fit your data model. Your data model is how the statistics for your sport are organized. If you can't think of a sport to analyze - give american football a try. Here is a link to the Nebraska Cornhuskers stats from 1983 (http://www.sports-reference.com/cfb/schools/nebraska/1983.html). Find the Rushing and Receiving table and create a database table structure that allows you to store that data inside of it.
- Create a python file that will insert a sample of data (no more than 20 rows) into your database using the cursor.execute method with some INSERT statements. This .py file does not also need to contain the logic for your main program. Just allow it to be run by itself to create data.
- Write a program that connects to the database and asks the user to search for a player. Start with just the name but think about further criteria you could include (position? age?). For a given result set, have the program display the results in a clean manner to the user.
- Add a feature to your program that allows a user to insert new players into the database. Prompt the user for every column that you will need them to provide custom information on. Name?, Age?, etc.

I used Python in order to complete this assignment.
