from flask import Flask, render_template, request
import pymysql

db = pymysql.connect(host="b96az1avpnrw5cohpooj-mysql.services.clever-cloud.com",
                     user="upj2vrn16ahshjxl",
                     password="eWbGa35vinZoU7mPj43h",
                     database="b96az1avpnrw5cohpooj")

cursor = db.cursor()
app = Flask(__name__)

@app.route('/')
def teste():
    listaVendas = cursor.execute("SELECT QTD FROM VENDAS")
    print(listaVendas)
    if listaVendas == 0:
        return render_template('index.html')
    else:
        return render_template('index.html', listaVendas=listaVendas)


@app.route('/registrar', methods=["POST"])
def teste2():
    cursor.execute("INSERT INTO VENDAS (QTD) VALUES (1)")
    db.commit()
    return "oi"

app.run(debug=True)

db.close()
