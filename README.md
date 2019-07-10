# Swipe For Rights API
A platform to express your opinion on congressional legislation.  This is the backend to the [Swipe For Rights Mobile App](github.com/CoreyAR/swipe-for-rights-mobile).

## Running
Make sure you

* Have 🐳 [Docker ](https://docs.docker.com/) installed
* Fill out the short [OpenStates API Key Registration Form](https://openstates.org/api/register/).  You should receive an email with your API key shortly. Hold onto it somewhere, as you'll need to set it in the environment each time you run the application.

In the root directory run:

```
export OPENSTATES_API_KEY="<your API key>"
docker-compose up
```

to build and run the app.  The following resources should now be available:

* Interactive API Documentation - http://localhost:8080/docs/

*Note*: For most endpoints you'll have to manually `login` and use the generated JWT token in the **Authentication** section of the interactive API documentation.

## Testing
Test can be run using the django cli.

```
./manage.py test <optional app name or test path>
```

*Note*: All commands after `docker-compose run api` are passed as arguments to the `apistar` command

## Architecture
This project is built using [Django Rest Framework](https://www.django-rest-framework.org/) and leverages Python3 types.
The python uses [Djongo](https://github.com/nesdis/djongo/) to extend Django's ORM to work with MongoDB.
Legislative information is copied from the [OpenStates API](http://docs.openstates.org/).

This also prefers [`setup.cfg` to store package information](http://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files), including install (`install_requires`) and dev (`extra_requires['dev']`) dependencies.

## License
[MIT](LICENSE) © 2018 Corey Rice