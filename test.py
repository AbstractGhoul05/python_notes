import mysql.connector
from difflib import SequenceMatcher, get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()
query = cursor.execute('SELECT Expression FROM Dictionary')
results = cursor.fetchall()
print(results[0][0])
# print(results)
