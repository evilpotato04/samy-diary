from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('Index.html', msg=None)

if __name__ == '__main__':
    app.run(debug=True)