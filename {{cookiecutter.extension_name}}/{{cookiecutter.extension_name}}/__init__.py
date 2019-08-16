from {{ cookiecutter.extension_name }}.handlers import setup_handlers


def _jupyter_server_extension_paths():
    return [{
        'module': '{{ cookiecutter.extension_name }}'
    }]


def load_jupyter_server_extension(nb_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.
    Parameters
    ----------
    nb_app: notebook.notebookapp.NotebookApp
        Notebook application instance
    """
    setup_handlers(nb_app.web_app)
    nb_app.log.info(f'Registered HelloWorld extension at URL path /{{ cookiecutter.api_endpoint }}')