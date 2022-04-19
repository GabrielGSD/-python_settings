from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
   return 'Olá, estou com a aplicação setada'

@app.route('/teste')
def teste():
   return 'ISSO É UM TESTE'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)