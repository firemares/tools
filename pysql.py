import pymysql

db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='spiders')

id='1'
test='1'

cursor = db.cursor()
sql = 'CREATE TABLE if not exists test (`id`  int NOT NULL ,`test`  varchar(255) not NULL ,PRIMARY KEY (`id`));'
sql_add = 'alter table `student` add column `name` varchar(255) not null after `age`'
sql_insert='insert into test(id, test) values(%s,%s)'

sql_version='select version()'
sql_db='select database()'
sql_sel='select * from student where id = %s'


cursor.execute(sql)
cursor.execute(sql_sel,(id))
if  cursor.fetchone() ==None :
    cursor.execute(sql_insert,(id,test))
    print('1')
else:
    print(cursor.fetchone())








# cursor.execute('select version()')
# cursor.execute(sql_add)

# try :
#     for id in range(100):
#         cursor.execute(sql_insert,(id,age,name))
#         db.commit()
#     # cursor.execute(sql_insert,(id,age,name))
#     # db.commit()
# except:
#     db.rollback()
# # cursor.execute(sql_sel)
# data = cursor.fetchall()
# print(list(data))
# db.close()
# data = cursor.fetchone()
# print(data)
# cursor.execute(("create database spiders default character  set utf8"))
# db.close()