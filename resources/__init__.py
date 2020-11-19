from flask_restful import Api

from resources.token import TokenResource, RefreshResource, RevokeResource
from resources.user import UserListResource, UserResource, MeResource


def init_app(app):

    api = Api(app)

    api.add_resource(UserListResource, "/users")
    api.add_resource(UserResource, "/users/<string:name>")
    api.add_resource(MeResource, "/me")

    api.add_resource(TokenResource, "/token")
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')
