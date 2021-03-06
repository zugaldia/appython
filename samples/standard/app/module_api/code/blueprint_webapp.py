'''
See http://flask.pocoo.org/docs/blueprints/
'''

from code.views.web.web_landing import WebLandingView
from flask import Blueprint

blueprint_webapp = Blueprint('webapp', __name__)


'''
Landing
'''

blueprint_webapp.add_url_rule(
    '/',
    view_func=WebLandingView.as_view('web_landing'))
