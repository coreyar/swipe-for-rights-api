from apistar import typesystem

class Login(typesystem.Object):
    properties = {
        'email': typesystem.string(max_length=100),  # Use lowercase functions for inline declarations.
        'password': typesystem.string(max_length=100),
    }

class Address(typesystem.Object):
    properties = {
        'street_address': typesystem.string(max_length=100),
        'locality': typesystem.string(max_length=100),
        'region': typesystem.string(max_length=2),
        'postal_code': typesystem.string(max_length=5),
    }

