from locale import currency
from flask import Flask,redirect,url_for,render_template,request
import requests

API_KEY = "dc1697bb16f80f74f2ef67e2384bc084"

url = "http://data.fixer.io/api/latest?access_key="+API_KEY


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        firstCurrency = request.form.get("firstCurrency")
        #id'mize göre verimizi POST ettik.
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")

        response = requests.get(url)
        #response içerinse get request alabilmek için url'imizi gönderdik.(Requests methodu ile
        
        infos = response.json()
        #Json fonksiyonunun kullanımı, Verimiz JSON verisi haline gelir
        app.logger.info(infos)
        #JSON verisi üzerinden verilerimiz görmemizi sağlar.
        firstValue = infos["rates"][firstCurrency]
        #Json verileri bir sözlük olduğu için sözlük gibi çağırabilir ve içerisinden verileri alabiliriz.

        secondValue = infos["rates"][secondCurrency]

        result = (secondValue/firstValue) * float(amount)
        #Değerimiz string geldiği için float kullanarak işimizi kesine alıyoruz ve sayısal olarak gösterebiliyoruz.
        
        currencyInfo = dict()
        #Değerlerimiz taşıyacak sözlük yapısı oluşturuyoruz.dict fonskiyonunu hatırlamış olalım Sözlük oluşturmamıza yarıyordu.
        #dict() fonksiyonu,currenyInfo = {}'ya eşittir.
        currencyInfo["firstCurrency"] = firstCurrency
        #sözlüğümüzü yukarıdaki gibi doldurabiliriz.
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result


        return render_template('index.html',info = currencyInfo)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)