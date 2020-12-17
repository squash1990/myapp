import uuid
def get_products():
	fake_response = [{
		"sku": uuid.uuid4(),
		"title": "Vanilla icecream",
		"long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultricies eleifend tortor at tempor. Nullam iaculis nulla quis ipsum bibendum, sit amet elementum tellus malesuada. Nam porttitor sapien nec sapien placerat, at auctor nisl feugiat. Praesent et faucibus nisi. Sed sit amet malesuada odio, vel lacinia erat. Donec maximus ipsum leo, quis eleifend sapien euismod sed. Aliquam nec molestie nunc, et auctor lacus. Cras scelerisque mauris tellus, aliquam luctus enim laoreet nec. Duis ullamcorper vitae eros ut condimentum.",
		"price": 1.5
	}, {
		
		"sku": uuid.uuid4(), '''sku = codigo univoco de referencia que lo hacemos con la libreria uuid'''
		"title": "Cola icecream",
		"long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultricies eleifend tortor at tempor. Nullam iaculis nulla quis ipsum bibendum, sit amet elementum tellus malesuada. Nam porttitor sapien nec sapien placerat, at auctor nisl feugiat. Praesent et faucibus nisi. Sed sit amet malesuada odio, vel lacinia erat. Donec maximus ipsum leo, quis eleifend sapien euismod sed. Aliquam nec molestie nunc, et auctor lacus. Cras scelerisque mauris tellus, aliquam luctus enim laoreet nec. Duis ullamcorper vitae eros ut condimentum.",
		"price": 1.5
	}, {
		"sku": uuid.uuid4(), '''sku = codigo univoco de referencia que lo hacemos con la libreria uuid'''
		"title": "Choco icecream",
		"long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultricies eleifend tortor at tempor. Nullam iaculis nulla quis ipsum bibendum, sit amet elementum tellus malesuada. Nam porttitor sapien nec sapien placerat, at auctor nisl feugiat. Praesent et faucibus nisi. Sed sit amet malesuada odio, vel lacinia erat. Donec maximus ipsum leo, quis eleifend sapien euismod sed. Aliquam nec molestie nunc, et auctor lacus. Cras scelerisque mauris tellus, aliquam luctus enim laoreet nec. Duis ullamcorper vitae eros ut condimentum.",
		"price": 1.5
	}, {
		"sku": uuid.uuid4(), '''sku = codigo univoco de referencia que lo hacemos con la libreria uuid'''
		"title": "Lemon icecream",
		"long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In ultricies eleifend tortor at tempor. Nullam iaculis nulla quis ipsum bibendum, sit amet elementum tellus malesuada. Nam porttitor sapien nec sapien placerat, at auctor nisl feugiat. Praesent et faucibus nisi. Sed sit amet malesuada odio, vel lacinia erat. Donec maximus ipsum leo, quis eleifend sapien euismod sed. Aliquam nec molestie nunc, et auctor lacus. Cras scelerisque mauris tellus, aliquam luctus enim laoreet nec. Duis ullamcorper vitae eros ut condimentum.",
		"price": 1.5
	}]
	return fake_response

def create_product(sku, title, long_description, price_euro):
	''' Insertar todo esto en una bbdd '''
	print(f"Crear sku={sku} y title={title}")
