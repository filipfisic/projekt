from flask import Flask
import funkcija_grupe
import funkcija_korisnici
import urllib.request
import re
import urllib.parse

app = Flask(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/index")
def home():
    # print(str(get("http://127.0.0.1:5000/podaci")))
    podaci = get("http://127.0.0.1:5000/podaci")
    podaci = podaci[1:len(podaci) + 1]
    x = re.split("Group", podaci)
    # print("radi")

    html = funkcija_grupe.fun_grupe(x)

    return html


def get(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr


@app.route("/grupa/<ime>")
def grupa(ime):
    ime = ime.split("'")
    ime[1] = ime[1].replace(" ", "%20")
    link = "http://127.0.0.1:5000/grupe/" + str(ime[1])
    # print(link)
    podaci = get(link)

    #print("jel ovo istina:")
    # print(podaci)
    podaci = podaci[1:len(podaci) - 1]
    podaci = podaci.split("Member")

    string = funkcija_korisnici.fun_korisnici(podaci)
    return string


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005)
