from apistar.frameworks.wsgi import WSGIApp

from swipe_for_rights_api import routes, settings


app = WSGIApp(routes=routes, settings=settings)

if __name__ == '__main__':
    app.main()
