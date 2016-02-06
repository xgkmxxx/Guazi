# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
#from scrapy import signals
#import json
#import codecs

class GuaziPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            db = 'guazi',
            user = 'root',
            passwd = '',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True
            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item
    #将数据写入或者更新
    def _conditional_insert(self, tx, item):
        name = self._get_name(item)
        #获得数据
        tx.execute("""
                select 1 from guazi_guazicar where name = %s
        """, (name, ))
        ret = tx.fetchone()

        if ret:
            #更新
            sql_up = 'update guazi_guazicar set city = %s, time = %s, mile = %s, price = %s where name = %s'
            tx.execute(sql_up, (item['city'][0], item['time'][0], item['mile'], item['price'], item['name'][0]))
        else:
            #写入
            sql_in = 'insert into guazi_guazicar values(%s, %s, %s, %s, %s, %s)'
            tx.execute(sql_in, ('', item['name'][0], item['city'][0], item['time'][0], item['mile'], item['price']))

    def _get_name(self, item):
        return item['name'][0]

        #sql = 'insert into guazicar values(%s, %s, %s, %s, %s, %s)'
        #tx.execute(sql, ('', item['name'][0], item['city'][0], item['time'][0], item['mile'], item['price']))
#将数据保存为json格式
#class JsonGuaziPipeline(object):
#  def __init__(self):
#    self.file = codecs.open('guazi.json', 'w', encoding='utf-8')
#  def process_item(self, item, spider):
#    line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#    self.file.write(line)
#    return item
#  def spider_closed(self, spider):
#    self.file.close()