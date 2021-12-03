from flask import Flask, render_template, request
import pymysql

import piCalcs.diferencial

db = pymysql.connect(host="b96az1avpnrw5cohpooj-mysql.services.clever-cloud.com",
                     user="upj2vrn16ahshjxl",
                     password="eWbGa35vinZoU7mPj43h",
                     database="b96az1avpnrw5cohpooj")

cursor = db.cursor(pymysql.cursors.DictCursor)
app = Flask(__name__)

@app.route('/')
def renderizar_pag():
    return render_template('index.html')


@app.route('/registrar', methods=["POST"])
def registrar_venda():
    qtd = request.form.get("qtd")
    cursor.execute("INSERT INTO VENDAS (QTD) VALUES ({})".format(qtd))
    db.commit()

    cursor.execute("SELECT QTD FROM VENDAS")
    listaVendas = cursor.fetchall()

    p = piCalcs.diferencial.Financeiro()
    lucroMax = p.calcMax()

    somaVendas = 0

    for venda in listaVendas:
        somaVendas += venda.get('QTD')

    valorParaLucroMax = lucroMax[0] - somaVendas

    return render_template('resultado.html', listaVendas=listaVendas, qtd=qtd, valorParaLucroMax= valorParaLucroMax)

app.run(debug=True)

db.close()
