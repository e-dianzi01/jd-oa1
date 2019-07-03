#
__author__ = 'bob'
__date__ = '2019/6/29 15:35'
import pymysql


conn = pymysql.Connect(host='localhost',
                       port=3306,
                       user='root',
                       db='jd',
                       password='buzhidao',
                       charset='utf8')
cursor = conn.cursor()


def mysql_save(table, zd, text, id, num):
    print(table, zd, text, id, num)
    try:
        sql = "update {} set {}={} where {}={};".format(table, zd, text, id, num)
        print('_------------------------=======>')
        print(sql)
        cursor.execute(sql)
        print('执行成功')
    except Exception as e:
        print('执行错误：', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
