# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, new_data):
        if new_data is None:
            return
        print(new_data['summary'])
        self.datas.append(new_data)

    def into_mysql(self):
        i = 0
        for data in self.datas:
            conn = pymysql.Connect(
                host='127.0.0.1',
                user='root',
                password='2414605975',
                db='wikiurl',
                port=3306,
                charset='utf8mb4'
            )
            try:
                cursor = conn.cursor()
                i += 1
                sql = 'insert into `urls`(`id`,`urlname`,`urlhref`,`urlcontent`)values(%s,%s,%s,%s)'
                cursor.execute(sql, (i, data['title'],data['url'],data['summary']))
                conn.commit()
            finally:

                conn.close()

