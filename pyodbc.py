import pyodbc

#make a connection
conn = pyodbc.connect("driver = {MySQL ODBC 8.0 ANSI Driver};server=localhost;database=third;uid=root;password=password;",autocommit=True)

cursor = conn.cursor()

#creating a cursor for executing sql commands
c = cursor.execute()
c = cursor.execute("select * from first_table")
for i in c:
	print(i) #print whole row
    print(i[0]) #print first column only of the row

#inserting a row in table
cursor.execute("insert into first_table values(7,'from pyodbc','1997-05-05')")

#updating a column in table
cursor.execute("update first_table set name='aaa' where name ='a'")

#creating a new table
cursor.execute("create table second_table as select * from first_table where 0=1")
cursor.execute("insert into second_table values (20,'d','1997-06-28') ,(21,'e','1997-06-28'), (22,'f','1999-06-28')")

#innner join two tables
result = cursor.execute("select * from first_table inner join second_table on first_table.id = second_table.id ")
for i in result:
    print(i)

#cross join
result = cursor.execute("select * from first_table cross join second_table ")
for i in result:
    print(i)

#left join
result = cursor.execute("select * from first_table left join second_table on first_table.id = second_table.id ")
for i in result:
    print(i)
#right join
result = cursor.execute("select * from first_table right join second_table on first_table.id = second_table.id ")
for i in result:
    print(i)

#left join using 'using clause'
result = cursor.execute("select * from first_table left join second_table using (id) ")
for i in result:
    print(i)
