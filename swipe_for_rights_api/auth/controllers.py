from apistar import http, Response, typesystem, annotate
from apistar.interfaces import Auth
from apistar.types import Settings
from apistar_jwt.token import JWT
from passlib.hash import pbkdf2_sha256

from swipe_for_rights_api.database.models.user import UserModel as User
from swipe_for_rights_api.annotations import public

from .types import Login, Address, UserType


def create_token(secret, payload):
    token = JWT.encode(payload, secret=secret)
    return token

@public()
def login(login: Login, settings: Settings):
    email = login['email']
    user = User.objects(email=email.lower()).first()
    if user:
        valid = pbkdf2_sha256.verify(login['password'], user['password'])
        if valid:
            secret = settings['JWT'].get('SECRET')
            payload = {'email': email, 'id': user.id.__str__()}
            token = create_token(secret, payload)
            return Response({'token': token, 'user': user.to_json()}, status=201)
        return Response('Incorrect username or password.', status=401)
    return Response('User does not exist.', status=401)

@public()
def signup(user: UserType, settings: Settings):
    email = user['email'].lower()
    exists = User.objects(email=email).first()
    if not exists:
        hash = pbkdf2_sha256.hash(user['password'])
        createdUser = User(
            email=email,
            password=hash,
            locality=user['locality'],
            street_address=user['street_address'],
            region=user['region'],
            postal_code=user['postal_code']
        ).save()
        secret = settings['JWT'].get('SECRET')
        payload = {'email': email, 'id': createdUser.id.__str__()}
        token = create_token(secret, payload)
        return Response(token, status=201)
    return Response('User exists.', status=401)

def me(request: http.Request, auth: Auth,  address: Address,):
    # TODO - Write a decorator for acceptable HTTP Methods
    if request.method == 'GET':
        return Response(auth.user, status=201)
    # TODO: Quick switch to PATCH
    if request.method == 'POST':
        user = User.objects(id=auth.user['id']).first()
        user.street_address = address['street_address']
        user.locality = address['locality']
        user.region = address['region']
        user.postal_code = address['postal_code']
        user.save()
        return Response(auth.user, status=204)
    return Response('Method not allowed',status=405)
