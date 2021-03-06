import pymysql as msql
import json

with open("./envars.json", "r") as e_file:
    env_file = json.load(e_file)
    e_file.close()

msql_db = msql.connect(
    env_file['db_data']['host_uri'],
    env_file['db_data']['db_uname'],
    env_file['db_data']['db_pword'],
    env_file['db_data']['db_sname']
)

m_cursor = msql_db.cursor()

__fakeUsers__ = (
    "Banksy",
    "Guy Fawkes",
    "Dudebro",
    "Brodude",
    "Anonymous",
    "Ugandan Knuckles Tribe",
    "PickleJho9000"
)

#m_cursor.execute("DROP TABLE messages")

create_table_messages = """
    CREATE TABLE messages (
            m_id INTEGER PRIMARY KEY AUTO_INCREMENT, 
            sender VARCHAR(40), 
            recipient VARCHAR(40),
            message NVARCHAR(255)
        );
    """
try:
    m_cursor.execute(create_table_messages)
except:
    print("table already exists. Skipping creation.")


def create_messages(user="Anonymous"):

    insert_new_message = f"""
        INSERT INTO messages (m_id, sender, recipient, message)
        VALUES (NULL, "{user}", "Guy Fawkes", "yo dude nice pics!");
        """
    m_cursor.execute(insert_new_message)


for u in __fakeUsers__:
    create_messages(u)

# Always keep these two when using cursor, in order to save changes.
msql_db.commit()

find_by_id = 36
m_cursor.execute(
    f'SELECT * '
    f'FROM messages '
    f'ORDER BY m_id DESC;'
)
messages = m_cursor.fetchall()

for m in messages:
    print(m)
# cursor.execute("SELECT * FROM messages;")

msql_db.close()
