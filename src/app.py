from wsgiref.simple_server import make_server
from pyramid.config import Configurator

def main():
    config = Configurator()
    config.add_route('spacebar', '/games/{game_name}/spacebar')
    config.add_route('openbet', '/games/{game_name}/openbet')
    config.add_route('nyx', '/games/{game_name}/nyx')

    config.add_static_view(name='games', path='games/')

    config.scan('views')
    app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    server = make_server('0.0.0.0', 8080, app)
    print ('Starting up server on http://localhost:8080')
    server.serve_forever()
