import sqlite3

id = 0
name = ""
occupation = ""
location = ""

conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute('select * from People')

records = c.fetchall()

print records

for record in records:
    id = record[0]
    name = record[1]
    occupation = record[2]
    location = record[3]

print "Current record:", id
print "Name: ", name
print "Occupation: ", occupation
print "Location: ", location

question = raw_input("Do you want to set location? (y/n) ")
if question == "y":
    print "Current location is ", location
    newloc = raw_input("Change it to what (string)? ")
    if newloc != location:
        location = newloc
        print "Location has changed! ", location

        c.execute('''UPDATE People SET location == :update_id''',
        {'update_id': newloc})

        conn.commit()
        conn.close()

raw_input("Press any key to exit")