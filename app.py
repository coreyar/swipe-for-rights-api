from apistar.frameworks.wsgi import WSGIApp
from api import routes, settings

app = WSGIApp(routes=routes, settings=settings)


if __name__ == '__main__':
    app.main()
