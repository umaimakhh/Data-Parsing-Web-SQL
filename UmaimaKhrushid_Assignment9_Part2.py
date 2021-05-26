import sqlite3
conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

createIndex = "CREATE INDEX userID_indx ON TweetTablee(user_id)"
cursor.execute(createIndex)

createComposite = "CREATE INDEX COMPOSITE_INDx ON user_Dictionaryy(friends_count, screen_name);"
cursor.execute(createComposite)


createComposite = "CREATE TABLE id_strx AS SELECT id_str FROM TweetTablee;"
cursor.execute(createComposite)

query1="SELECT * FROM id_strx where id_str like '%777%' or id_str like '%88%';"
cursor.execute(query1).fetchall()

conn.commit()
conn.close()