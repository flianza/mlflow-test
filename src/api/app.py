import os

from dotenv import load_dotenv
from mlflow.pyfunc import load_model, scoring_server

from src.api.middleware.authentication import BasicAuthetication

load_dotenv()

model = load_model(os.environ["MODEL_PATH"])
app = scoring_server.init(model)
app.wsgi_app = BasicAuthetication(app.wsgi_app)
