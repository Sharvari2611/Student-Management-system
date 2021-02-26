<h1>Student-Management-system</h1>
This is a Management System Design Project using <br>
-Tkinter for GUI.<br>
-PDBC using SQLite3.<br>
-Data Science(Extraction, Analysis & Visualization).
<br>The main window has following options:<br>
 ----ADD<BR>
 ----VIEW<BR>
 ----UPDATE<BR>
 ----REMOVE<BR>
 ----SHOW BARGRAPH<BR>
Each button when clicked will take the user to respective window.<br>The ADD button will take the user to the window where there will be options for inserting RollNo,Name and Marks.
Roll no acts as primary key and the inserted data will be validated and then stored in the database and proper message is displayed.<br>The VIEW window displays all the records.
<br>The UPDATE window helps user update a record by inserting the Rollno
,if the roll no exists in table then only it would be updated else meassge will be displayed.
<br>The REMOVE window would remove the record from the table.
<br>The SHOW BARGRAPH Option would plot the student marks on the graph. 
<h3>Tkinter</h3>
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
Creating a GUI application using Tkinter is an easy task. All you need to do is perform the following steps −<br>
Import the Tkinter module.<br>
Create the GUI application main window.<br>
Add one or more of the above-mentioned widgets to the GUI application.<br>
Enter the main event loop to take action against each event triggered by the user.

<h3>Sqlite</h3>SQLite is a popular choice as embedded database software for local/client storage in application
software such as web browsers.SQLite is a C library that provides a lightweight disk-based database that doesn't 
require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.

<h3>Data Extraction</h3>Further data science concepts have been implemented which includes extracting data from a website using Beautiful Soup module provided by python.The daily live temperature and a Thought for the day is displayed which keeps changing daily.
<br>Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup languages.Beautiful Soup helps you pull particular content from a webpage, remove the HTML markup, and save the information.
 It is a tool for web scraping that helps you clean up and parse the documents you have pulled down from the web.Installing Beautiful Soup is easiest if you have pip or another Python installer already in place. 
