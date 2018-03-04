import os

from mongoengine import connect


connect(host=os.environ['SWIPE_FOR_RIGHTS_MONGO_URL'])
