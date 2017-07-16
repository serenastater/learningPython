import sqlite3
import urllib

#connect to file where db is stored
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

#delete any table that could exist in db
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#create table that will be used
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#Prompts user for filename
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
#Reads each line of file
for line in fh:
    #Locates email address
    if not line.startswith('From: '): continue
    #splits into name and organization
    pieces = line.split()
    email = pieces[1]
    (emailname, organization) = email.split("@")
    print(email)
    #Update table with the correspondent information
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (organization,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (organization,))
    conn.commit()

#Get and print top 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print
print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
#close db
cur.close()
