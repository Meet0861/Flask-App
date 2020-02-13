from api.controllers import create_app
from config import LocalConfig

application = create_app(config_module_class=LocalConfig)

""" to run the application"""
if __name__ == '__main__':
    application.run(debug=True)


