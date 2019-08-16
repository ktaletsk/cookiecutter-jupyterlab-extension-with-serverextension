from notebook.base.handlers import APIHandler
from notebook.utils import url_path_join
import json


class HandlerClass(APIHandler):
    def get(self):
        self.finish(json.dumps({
            'data': 'This is /{{ cookiecutter.api_endpoint }} endpoint!'
        }))


def setup_handlers(web_app):
    host_pattern = '.*$'
    
    base_url = web_app.settings['base_url']
    route_pattern = url_path_join(base_url, '/{{ cookiecutter.api_endpoint }}')
    handlers = [(route_pattern, HandlerClass)]
    web_app.add_handlers(host_pattern, handlers)