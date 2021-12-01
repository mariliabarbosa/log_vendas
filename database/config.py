import export as export
import pymysql

db = pymysql.connect(host="b96az1avpnrw5cohpooj-mysql.services.clever-cloud.com",
                     user="upj2vrn16ahshjxl",
                     password="eWbGa35vinZoU7mPj43h",
                     database="b96az1avpnrw5cohpooj")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS VENDAS")

create = """
    CREATE TABLE VENDAS (
        QTD INT
    )
"""

cursor.execute(create)

db.close()
