#how to create table,INSERT,retrieve data,Update,delete,Drop table 


import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="pranu",
    charset="utf8",
    database="computer"

)

mycursor=mydb.cursor()


#For Create Table 
#mycursor.execute("CREATE TABLE custom (name VARCHAR(255), address VARCHAR(255))")

#For Insert
# sql = "INSERT INTO custom (name, address) VALUES (%s, %s)"
# val = ("John22", "Highway 21212")

# mycursor.execute(sql, val)

#FOR SELECT
# mycursor.execute("SELECT * FROM custom")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#FOR WHERE
# sql = "SELECT * FROM custom WHERE address ='Highway 21'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#FOR ORDER BY
# sql = "SELECT * FROM custom ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

#For DELETE
# sql = "DELETE FROM custom WHERE address = 'Highway 21'"

# mycursor.execute(sql)

#For Drop

# sql = "DROP TABLE IF EXISTS custom"

# mycursor.execute(sql)
mydb.commit()

#For Update
sql = "UPDATE custom SET address = 'Highwareey 21212'  WHERE address = 'Highway 21212'"

mycursor.execute(sql)

# print(mycursor.rowcount, "record(s) deleted")

# print(mycursor.rowcount, "record inserted.")

print(mycursor.rowcount, "record(s) affected")
