#-*- coding: utf-8 -*-
import MySQLdb
import json
import collections

if __name__ == "__main__":

       connector = MySQLdb.connect(host="localhost", db="sangi",user="root", 
       passwd="root", charset="utf8")       
       cursor = connector.cursor()
           
       f = open('data.json','r')
       jsonData = json.load(f, object_pairs_hook=collections.OrderedDict)
       f.close()
      
       for num in jsonData:
           print jsonData[num]
           sql = "insert into sensors(sensor) values(" + str(jsonData[num])+ ")"
           cursor.execute(sql)
           
       connector.commit()
       cursor.close()
       connector.close()
       
       
