import pymysql.cursors
from common.system import ReadCryptoConfig

class DBHandle(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                print('connecting to mysql database...')
                dbinfo = ReadCryptoConfig('database.dat')
                connection = DBHandle._instance.connection =  pymysql.connect(
                    host = dbinfo["dbhost"],
                    user = dbinfo["dbuser"],
                    password = dbinfo["dbpass"],
                    db = dbinfo["dbname"],
                    cursorclass=pymysql.cursors.DictCursor
                )
                cursor = DBHandle._instance.cursor = connection.cursor()
                cursor.execute('SELECT VERSION()')
                db_version = cursor.fetchone()

            except Exception as error:
                print('Error: connection failed {}'.format(error))
                DBHandle._instance = None

            else:
                print("Connection established\n{}" . format(db_version))

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection

    def query(self, query):
        try:
            cursor = self.connection.cursor()
            result = cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return cursor.fetchone()

    def __del__(self):
        self.connection.close()
