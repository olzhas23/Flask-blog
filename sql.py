import sqlite3
with sqlite3.connect ("blog.db") as connection:

	c=connection.cursor()
	c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")
	
	c.execute ("""INSERT INTO posts VALUES( 'hi', 'its a great morning')"""),
	c.execute ("""INSERT INTO posts VALUES( 'Good', ' its a great morning')"""),
	c.execute ("""INSERT INTO posts VALUES( 'Awesome', ' its a great nigh')"""),
	c.execute ("""INSERT INTO posts VALUES( 'Hi dear', ' its a great day')""")
	
	