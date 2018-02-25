from apistar import http, Response, typesystem, annotate
from apistar.interfaces import Auth
from apistar.types import Settings
from apistar_jwt.token import JWT
from apistar_jwt.authentication import JWTAuthentication
from passlib.hash import pbkdf2_sha256
from .types import Login, Address
from database.models.user import User

def create_token(secret, payload):
    token = JWT.encode(payload, secret=secret)
    return token


def login(login: Login, settings: Settings):
    email = login['email']
    user = User.model.objects(email=email.lower()).first()
    if user:
        valid = pbkdf2_sha256.verify(login['password'], user['password'])
        if valid:
            secret = settings['JWT'].get('SECRET')
            payload = {'email': email, 'id': user.id.__str__()}
            token = create_token(secret, payload)
            return Response({'token': token, 'user': user}, status=201)
        return Response('Incorrect username or password.', status=401)
    return Response('User does not exist.', status=401)

def signup(login: Login, settings: Settings):
    email = login['email'].lower()
    user = User.objects(email=email).first()
    if not user:
        hash = pbkdf2_sha256.hash(login['password'])
        user = User.model(email=email, password=hash).save()
        secret = settings['JWT'].get('SECRET')
        payload = {'email': email, 'id': user.id.__str__()}
        token = create_token(secret, payload)
        return Response(token, status=201)
    return Response('User exists.', status=401)

@annotate(authentication=[JWTAuthentication()])
def me(request: http.Request, auth: Auth,  address: Address,):
    # TODO - Write a decorator for acceptable HTTP Methods
    if request.method == 'GET':
        return Response(auth.user, status=201)
    if request.method == 'POST':
        user = User.objects(id=auth.user['id']).first()
        user.street_address = address['street_address']
        user.locality = address['locality']
        user.region = address['region']
        user.postal_code = address['postal_code']
        user.save()
        return Response(auth.user, status=204)
    return Response('Method not allowed',status=405)
