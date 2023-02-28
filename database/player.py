import mysql.connector
import mysql.connector.cursor

class __Database:
    def __init__(self, dict=False) -> None:
        self.__dict = dict
        self.__conn = mysql.connector.connect(
            host='localhost',
            database='pongas',
            user='root',
            password='admin'
        )
    
    def __enter__(self):
        self.__cur = self.__conn.cursor(dictionary=self.__dict)
        return self.__cur
    
    def __exit__(self):
        self.__conn.commit()
        self.__cur.close()
        self.__conn.close()


def create_player(name: str, icon: str = None):
    with __Database() as cur:
        cur.execute(
            'INSERT INTO player(name, icon, wins, defeat) VALUES (%s, %s, 0, 0) as val '
            'ON DUPLICATE KEY UPDATE name = val.name, icon = val.icon',
            [name, icon]
        )