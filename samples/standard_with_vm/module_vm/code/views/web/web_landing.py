from flask.views import MethodView
import shapely

# import logging


class WebLandingView(MethodView):
    def get(self):
        return 'Sample VM with Shapely version {}.'.format(
            shapely.__version__)
