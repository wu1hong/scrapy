import mysql.connector
from novel1.novel import settings

MYSQL_HOST = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user='root', password='password', database='dd_name')
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert_dd_name(cls, xs_name, xs_author, category, name_id, serial_status, serial_number):
        sql = 'INSERT INTO dd_name (`xs_name`, `xs_author`, `category`, `name_id`, `serial_status`, `serial_number`) VALUES (%(xs_name)s, %(xs_author)s, %(category)s, %(name_id)s, %(serial_status)s, %(serial_number)s)'
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'category': category,
            'name_id': name_id,
            'serial_status': serial_status,
            'serial_number': serial_number
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = "SELECT EXISIS(SELECT 1 FROM dd_name WHERE name_id=%(name_id)s"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()[0]
