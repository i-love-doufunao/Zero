# -*- coding: utf-8 -*-

import pymysql
import sys
import time
from spider import Job


def createCompanyTable(createTime, ):
    db = pymysql.connect("localhost", "root", "root", "JOB_DB", use_unicode=True, charset="utf8")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    tableName = "company_info_%s" % (createTime)
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS %s (
             name VARCHAR(20) NOT NULL ,
             industry  VARCHAR(10) NOT NULL,
             org_industry  VARCHAR(10) NOT NULL,
             url VARCHAR(100) NOT NULL,
             locate VARCHAR(10),
             address VARCHAR(20),
             is_financing BIT ,
             company_size VARCHAR(10),
             publishTime DATE,createdTime DATE,updatedTime DATE)
               engine=innodb default charset=utf8 """ % (tableName)

    cursor.execute(sql)

    print("创建%s成功" % (tableName))

    # 关闭数据库连接
    db.close()


def createJobTable(createTime, ):
    db = pymysql.connect("localhost", "root", "root", "JOB_DB", use_unicode=True, charset="utf8")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    tableName = "job_info_%s" % (createTime)
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE IF NOT EXISTS %s (
             id int NOT NULL auto_increment PRIMARY KEY ,
             name  VARCHAR(20) NOT NULL,
             company  VARCHAR(20) NOT NULL FOREIGN KEY ,
             min_salary VARCHAR(20),
             max_salary VARCHAR(20),
             url VARCHAR(100) NOT NULL,
             locate VARCHAR(10),
             publish_time DATE,createdTime DATE,updatedTime DATE)
               engine=innodb default charset=utf8 """ % (tableName)

    cursor.execute(sql)

    print("创建%s成功" % (tableName))

    # 关闭数据库连接
    db.close()


def insertJobInfo(jobList):
    """
    将职位插入数据库
    :param jobList:
    :return:
    """
    nowTime = time.localtime()
    sql = """INSERT INTO %s(name,company,salary,url,locate,createdTime,updatedTime) VALUES """ \
          % ("job_info_" + time.strftime("%Y_%m_%d", nowTime))
    for job in jobList:
        insertValue = "('%s','%s','%s','%s','%s','%s','%s')," % (
            job.name, job.company, job.salary, job.url, job.locate,
            time.strftime("%Y-%m-%d %H:%M:%S", nowTime),
            time.strftime("%Y-%m-%d %H:%M:%S", nowTime))

        sql = sql + "%s" % insertValue
    sql = sql[:sql.rindex(',')]

    # 插入数据库
    db = pymysql.connect("localhost", "root", "root", "JOB_DB", use_unicode=True, charset="utf8")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # try:
    # 执行sql语句
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.err.InternalError as err:
        # 如果发生错误则回滚，记录日志
        print("写数据到数据库中发生异常:", err)
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()
