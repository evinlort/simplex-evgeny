from flask import Flask

from quote.quote import quote

app = Flask(__name__)
app.register_blueprint(quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, load_dotenv=True, threaded=False, processes=10)
