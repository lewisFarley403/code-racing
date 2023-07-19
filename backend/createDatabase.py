import sqlite3
with sqlite3.connect('racing.db') as db:
    cursor = db.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS tblQuestion(    
questionID INTEGER PRIMARY KEY autoincrement,
questionTitle title text NOT NULL,
questionDescription text);
        '''
                   )
    cursor.execute('''
CREATE TABLE IF NOT EXISTS tblTestInput(
testID INTEGER PRIMARY KEY autoincrement,
input text NOT NULL,
output text NOT NULL,
questionID INTEGER,
FOREIGN KEY (questionID) REFERENCES tblQuestion(questionID));'''
                   )
    cursor.execute('''
CREATE TABLE IF NOT EXISTS tblPlayingGroup(
groupID INTEGER PRIMARY KEY autoincrement,
timestampStarted real,
finished INTEGER,
joinCode text,
questionID INTEGER,
FOREIGN KEY (questionID) REFERENCES tblQuestion(questionID));'''
                   )
    cursor.execute('''CREATE TABLE IF NOT EXISTS tblPlayer(
        playerID INTEGER PRIMARY KEY autoincrement,
        displayName text NOT NULL,
        groupID INTEGER,
        FOREIGN KEY(groupID) REFERENCES tblPlayingGroup(groupID));''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tblControls(
        playerID INTEGER,
        groupID INTEGER,
        FOREIGN KEY(groupID) REFERENCES tblPlayingGroup(groupID),
        FOREIGN KEY (playerID) REFERENCES tblPlayer(playerID),
        
        PRIMARY KEY (playerID,groupID));''')
    #cursor.execute('DROP TABLE tblTestInput')
