from flask.views import MethodView
from routes.blueprints import google_config_blp as blp
from schemas import *
from controllers.google_config import *


@blp.route("/google_data/data")
class GoogleConfig(MethodView):
    @blp.arguments(GoogleConfigSchemaGet)
    def get(self, body_data):
        return google_config_get(body_data)

    @blp.arguments(GoogleConfigSchemaPost)
    def post(self, body_data):
        return google_config_post(body_data)

    @blp.arguments(GoogleConfigSchemaPut)
    def put(self, body_data):
        return google_config_put(body_data)

    @blp.arguments(GoogleConfigSchemaDelete)
    def delete(self, body_data):
        return google_config_delete(body_data)
