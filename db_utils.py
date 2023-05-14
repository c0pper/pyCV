import sqlite3
from classes import Experience


conn = sqlite3.connect("sqlite_resume.sqlite3")
cursor = conn.cursor()

cursor.execute("""SELECT name FROM sqlite_master  
  WHERE type='table';""")
print(cursor.fetchall())


def get_experience_by_type(type: str):  # 'w' or 'e'
    exp_list = cursor.execute("""SELECT * FROM website_experience WHERE exp_type='W';""")
    print(exp_list)
    exp_objects = [Experience()]


cursor.execute("""SELECT * FROM website_institution;""")
print(cursor.fetchall())
cursor.execute("""SELECT Institution FROM website_experience;""")
print(cursor.fetchall())