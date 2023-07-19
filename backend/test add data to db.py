import sqlite3

with sqlite3.connect('racing.db') as db:
    cursor = db.cursor()
    # cursor.execute('''
    # INSERT INTO tblQuestion(questionTitle,questionDescription)
    # VALUES ("this is a test title", "lorum ipsum")''')
