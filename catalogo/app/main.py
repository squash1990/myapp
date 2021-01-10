from flask import jsonify, request, Flask
from catalog import get_products, create_product
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/product', methods=['GET', 'POST'])
def list_all_products():
	'''This view manages the CRUD of products'''
	print("Hola mundo")
	if request.method == 'GET':
		response = get_products()
		return jsonify(response)

	if request.method == 'POST':
		data = request.get_json()
		new_sku = create_product(
			None,
			data['title'],
			data['long_description'],
			data['price_euro'])
		return jsonify({"status": "ok", "sku": new_sku})


@app.route('/hello')
def hello_world():
	message = "Hola Mundo, soy Pyton! Ahora con CloudBuild y hablando JSON."
	response = {
			"messaje": message,
			"length": len(message)
	}
	return jsonify(response)


@app.route('/bye')
def bye_world():
    return ("Adios mundo cruel")

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)
