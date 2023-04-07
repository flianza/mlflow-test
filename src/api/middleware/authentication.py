import json
import os
from typing import Any, Callable

from werkzeug.wrappers import Response


class BasicAuthetication:
    def __init__(self, app) -> None:
        self.app = app

    def __call__(self, environ: dict, start_response: Callable) -> Any:
        secret_key = environ.get("HTTP_X_APP_KEY", None)

        if secret_key is None:
            return Response(
                json.dumps({"error": "Missing token"}),
                status=401,
                mimetype="application/json",
            )(environ, start_response)

        if secret_key != os.environ["API_APP_KEY"]:
            return Response(
                json.dumps({"error": "Invalid token"}),
                status=403,
                mimetype="application/json",
            )(environ, start_response)

        return self.app(environ, start_response)
