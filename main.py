from flask import Flask, render_template, request
import pymysql

import picalcs.derivada

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
    lista_vendas = cursor.fetchall()

    p = picalcs.derivada.Financeiro()
    lucro_max = p.calc_max()

    soma_vendas = 0

    for venda in lista_vendas:
        soma_vendas += venda.get('QTD')

    valor_para_lucro_max = round(lucro_max[0] - soma_vendas, 2)

    return render_template('resultado.html', lista_vendas=lista_vendas, qtd=qtd, valor_para_lucro_max= valor_para_lucro_max)

app.run(debug=True)

db.close()
