from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import *
from controllers.google_tokens import *
from flask import request


blp = Blueprint('token_mapping', __name__, description='Google token related controllers')


@blp.route("/google_data/token_mapping")
class GoogleToken(MethodView):
    def get(self):
        params_data = dict(request.args)
        return google_tokens_get(params_data)

    @blp.arguments(GoogleTokensSchemaPost)
    def post(self, body_data):
        return google_tokens_post(body_data)
