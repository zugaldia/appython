from code.blueprint_webapp import blueprint_webapp
from shared.bootstrap import create_app
from shared.config import Config

# import logging

app = create_app(config_flask=Config.FLASK)

'''
Flask blueprints
'''

app.register_blueprint(blueprint_webapp)
