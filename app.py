import os
import json
from flask import Flask, request, render_template

app = Flask(__name__)

# Imposta il percorso del file di domande e risposte
QA_FILE = "domande_risposte.json"

# Crea o apre il file di domande e risposte
if os.path.exists(QA_FILE):
    with open(QA_FILE, "r") as f:
        qa_dict = json.load(f)
else:
    qa_dict = {}

# Funzione per porre una domanda e cercare la risposta nella lista di coppie domanda-risposta
def ask_question(question):
    for q, a in qa_dict.items():
        if q in question:
            return a
    
    return "Mi dispiace, non ho trovato la risposta alla tua domanda."

# Pagina di benvenuto
@app.route("/")
def welcome():
    return render_template("index.html")

# Pagina di risposta alla domanda
@app.route("/answer", methods=["POST"])
def answer():
    question = request.form["question"]
    answer = ask_question(question)
    return render_template("index.html", question=question, answer=answer)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
