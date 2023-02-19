import sqlite3

DB_FILE = "database.db"
stories_header = "(date TEXT, newText TEXT, Contributor TEXT)"
users_header = "(username TEXT, password TEXT)"


def query(sql, extra = None):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    if extra is None:
        res = c.execute(sql)
    else:
        res = c.execute(sql, extra)
    db.commit()
    db.close()
    return res

def create_table(name, header):
    query(f"CREATE TABLE IF NOT EXISTS {name} {header}")

create_table("emotionInfo", stories_header)
create_table("userInfo", users_header)

def add_account(username, password):
    if not(check_username(username)):
        query("INSERT INTO userInfo VALUES (?, ?)", (username, password))
    else:
        return -1

def check_username(username):
    accounts = get_table_contents("userInfo")
    for account in accounts:
        if account[0] == username:
            return True
    return False
#return true if username and password are in db, false if one isn't
def verify_account(username, password):
    accounts = get_table_contents("userInfo")
    for account in accounts:
        if account[0] == username and account[1] == password:
            return True
    return False

def get_table_contents(tableName):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT * from {tableName}")
    out = res.fetchall()
    db.commit()
    db.close()
    return out

print(get_table_contents("emotionInfo"))
def get_user_stories(username):
    viewable_stories = []
    stories = get_table_contents("emotionInfo")
    for story in stories:
        print(username)
        print(story[2])
        if username == story[2]:
            viewable_stories.append(story[1] + " at " + story[0])
    return viewable_stories

def setup():
    user_header = ("(username TEXT, password TEXT)")
    create_table("userInfo",user_header)

def add_entry(date, newText, contributor):
    query("INSERT INTO emotionInfo VALUES (?, ?, ?)", (date, newText, contributor))

def get_story_contents(storyName):
    storyInfo = get_table_contents("emotionInfo")
    for row in storyInfo:
        if row[0] == storyName:
            return row[1]
    return -1

    


