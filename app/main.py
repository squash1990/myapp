from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	message = "Hola Mundo, soy Pyton! Ahora con CloudBuild y hablando JSON. Versión 2.0. Updated "
	response = {
			"messaje": message,
			"length": len(message)
	}
	return jsonify(response)

@app.route('/bye')
def bye_world():
    return ("Adios mundo cruel")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
