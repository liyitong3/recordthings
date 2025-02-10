# 程序简介
记事系统,默认显示当前未完成事务，可以查看全部记录。

框架或者软件：Flask+Layui+jQuery+MySQL

1.方便每天查看当前未完成事宜。

2.随时查账以前事情的时间人物内容等。

3.期末或者年底汇总。

# 部署步骤
1.推荐Python3.8，然后pip install -r requirment.txt

2.安装MySQL数据库，推荐5.5.7版本。

3.编辑mysql_util.py文件里面的数据库链接信息，和MySQL数据库保持一致。

host = '127.0.0.1'    # 数据库所在地址

user = 'root'         # 数据库用户名

password = '123456'     # 数据库密码

database = 'memory_things_system' # 数据库名称

4.新建数据库，名称和第3步的database值保持一致。打开“mysql导入”文件夹，新建3张表和1个视图。

5.事务的分类在thingtype表中，可自定义修改。

# 后续事宜
以后再补充按条件筛选并导出分类汇总的结果。
