from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api
from api.controllers.login import api as login_ns
from api.controllers.test import api as test_ns


def create_app(*, config_module_class):
	"""creates the flask application and register the namespace"""
	app = Flask(__name__, instance_relative_config=True)
	jwt = JWTManager(app)
	app.config.from_object(config_module_class)

	authorizations = {
		'Authorize': {
			'type': 'apiKey',
			'in': 'header',
			'name': 'jwt-token'
		}
	}
	api = Api(app, authorizations=authorizations)

	api.add_namespace(login_ns, path='/api/v1/login')
	api.add_namespace(test_ns, path='/api/v1/test')

	return app

