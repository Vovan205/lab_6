import MySQLdb

db = MySQLdb.connect(
    host='localhost',
    user='dbuser',
    passwd='123',
    db='first_db',
    use_unicode=True,
    charset='utf8'
)

c = db.cursor()

c.execute("INSERT INTO team (name, description) VALUES (%s, %s);", ('Зенит', 'Российский футбольный клуб'))
db.commit()

c.execute("SELECT * FROM team;")
teams = c.fetchall()
for team in teams:
    print(team)

c.execute("DELETE FROM team;")
db.commit()

c.execute("SELECT * FROM team;")
teams = c.fetchall()
print('БД после удаления:')
for team in teams:
    print(team)

c.close()
db.close()
