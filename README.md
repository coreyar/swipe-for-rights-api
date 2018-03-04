# Swipe For Rights API
A platform to express your opinion on congressional legislation.  This is the backend to the [Swipe For Rights Mobile App](github.com/CoreyAR/swipe-for-rights-mobile).

## Running
Make sure you

* Have 🐳 [Docker ](https://docs.docker.com/) installed
* Fill out the short [OpenStates API Key Registration Form](https://openstates.org/api/register/).  You should receive an email with your API key shortly. Hold onto it somewhere, as you'll need to set it in the environment each time you run the application.

In the root directory run:

```
export OPEN_STATES_API_KEY="<your API key>"
docker-compose up
```

to build and run the app.  The following resources should now be available:

* Interactive API Documentation - http://localhost:8080/docs/


## Testing
Test are run inside of the `api` docker container (make sure your `OPEN_STATES_API_KEY` is set) using API Star's built-in testing framework [py<span style="color: deepskyblue">test</span>](https://docs.pytest.org/en/latest/).

```
docker-compose run api test
```

*Note*: All commands after `docker-compose run api` are passed as arguments to the `apistar` command

## Architecture
This project is built using [API Star](https://github.com/encode/apistar), an API library specifically tailored to leverage types and asynchrony in Python3.  Legislative information is copied from the [OpenStates API](http://docs.openstates.org/).

This also prefers [`setup.cfg` to store package information](http://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files), including install (`install_requires`) and dev (`extra_requires['dev']`) dependencies.

## License
[MIT](LICENSE) © 2018 Corey Rice
