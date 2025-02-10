import pymysql   # 引入pymysql模块
import traceback # 引入python中的traceback模块，跟踪错误
import sys       # 引入sys模块

class MysqlUtil():
    def __init__(self):
        '''
            初始化方法，连接数据库
        '''
        host = '127.0.0.1'      # 主机名
        user = 'root'           # 数据库用户名
        password = '123456'     # 数据库密码
        database = 'memory_things_system' # 数据库名称
        self.db = pymysql.connect(host=host,user=user,password=password,db=database) # 建立连接
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor) # 设置游标，并将游标设置为字典类型
    
    def insert(self, sql):
        '''
            插入数据库
            sql:插入数据库的sql语句
        '''
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception:  # 方法一：捕获所有异常
            # 如果发生异常，则回滚
            print("发生异常", Exception)
            self.db.rollback()
        finally:
            # 最终关闭数据库连接
            self.db.close()

    def fetchone(self, sql):
        '''
            查询数据库：单个结果集
            fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
        '''
        result="没有返回值"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            print(sql)
            result = self.cursor.fetchone()
        except:  # 方法二：采用traceback模块查看异常
            # 输出异常信息
            traceback.print_exc()
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 最终关闭数据库连接
            self.db.close()
        return result

    def fetchall(self, sql):
        '''
            查询数据库：多个结果集
            fetchall(): 接收全部的返回结果行.
        '''
        results="没有返回值"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:  # 方法三：采用sys模块回溯最后的异常
            # 输出异常信息
            info = sys.exc_info()
            print(info[0], ":", info[1])
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 最终关闭数据库连接
            self.db.close()
        return results

    def delete(self, sql):
        '''
            删除结果集
        '''
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.db.commit()
        except:  # 把这些异常保存到一个日志文件中，来分析这些异常
            # 将错误日志输入到目录文件中
            f = open("\log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 最终关闭数据库连接
            self.db.close()

    def update(self, sql):
        '''
            更新结果集
        '''
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 如果发生异常，则回滚
            self.db.rollback()
        finally:
            # 最终关闭数据库连接
            self.db.close()
