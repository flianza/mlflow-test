import os

from dotenv import load_dotenv
from mlflow.pyfunc import load_model, scoring_server

from api.middleware.authentication import BasicAuthetication

load_dotenv()

model = load_model(os.environ["API_MODEL_PATH"])
app = scoring_server.init(model)
app.wsgi_app = BasicAuthetication(app.wsgi_app)
