import json
from models import GoogleConfigModel


def google_config_get(s):
    
    if not s=="all":
        data = GoogleConfigModel.query.filter_by(google_path=s)
    else:
        data = GoogleConfigModel.query.all()
    all_data = [{"google_path": item.google_path, "value": json.loads(item.value)} for item in data]

    return all_data
