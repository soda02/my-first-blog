import pyodbc
server = 'rdsxdtlgl0qawdnd08juo.sqlserver.rds.aliyuncs.com,3433'
database = 'db_hanguomianshui'
username = 'escodfs'
password = 'escodfs123'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT top 100 * FROM t_member")
row = cursor.fetchone()
while row:
    print str(row[0]) + " " + str(row[1])
    row = cursor.fetchone()
