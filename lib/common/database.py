import MySQLdb
import MySQLdb.cursors
from common.logger import GetFileLogger
from common.system import readconfig
from common.crypt import AESCipher


class DBHandle:

    def __init__(self):
        self.log = GetFileLogger()
        self.config = readconfig('database.json')
        self.log.info("Loaded configuration")
        self.connected = self.connect()
        self.log.info("Connected to database server")

        if not self.checkdb(self.config['dbname']):
            self._createdb()

        cursor = self.handle.cursor()
        cursor.execute("USE {}".format(self.config['dbname']))
        self.log.info("SELECTED {} database.".format(self.config['dbname']))

    def connect(self):
        crypt = AESCipher()
        try:
            self.handle = MySQLdb.connect(
                host=self.config["host"],
                port=self.config["port"],
                user=self.config["dbuser"],
                passwd=crypt.decrypt(self.config["dbpass"])
            )

            return True

        except Exception as error:
            self.log.error("Failed to connect to database: {}".format(error))
            return False


    def checkdb(self, dbname):
        result = False
        if self.connected:
            cursor = self.handle.cursor()
            cursor.execute("SHOW DATABASES")
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == dbname:
                    self.log.info("DB Name: {}".format(row[0]))
                    self.log.info("Found database {}".format(dbname))
                    result = True
            cursor.close()
        else:
            self.log.warn("Not connected")
        return result

    def _createdb(self):
        try:
            cursor = self.handle.cursor()
            cursor.execute(
                "CREATE DATABASE {} CHARACTER SET utf8 COLLATE utf8_general_ci".format(self.config['dbname'])
            )

            self.log.info("DATABASE {} CREATED.".format(self.config['dbname']))
            cursor.close()
        except Exception as error:
            self.log.error("Failed to create database: {}".format(error))

    def close(self):
        if self.connected:
            self.handle.close()

    def do(self, query):
        result = True
        if self.connected:
            try:
                cursor = self.handle.cursor()
                cursor.execute(query)
            except Exception as error:
                self.log.warn("Failed to execute query: {}".format(error))
                result = False
            finally:
                cursor.close()
        else:
            self.log.warn("Not connected")
            result = False

        return result

    def query(self, query, type=MySQLdb.cursors.Cursor):
        if self.connected:
            try:
                cursor = self.handle.cursor()
                cursor.execute(query)
                return cursor
            except Exception as error:
                self.log.warn("Failed to execute select query: {}".format(error))

    def insert_id(self):
        return self.handle.insert_id()

    def dict_query(self, query):
        return self.query(query, MySQLdb.cursors.DictCursor)

    def execute(self, query):
        result = False
        if self.connected:
            try:
                cursor = self.handle.cursor()
                cursor.execute(query)
                result = True
            except Exception as e:
                self.log.warn("Failed to execute query: {}".format(e))
                self.log.debug(query)

        return result