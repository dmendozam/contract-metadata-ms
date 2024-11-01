import azure.functions as func
import datetime
import json
import logging
# from fastapi.middleware.wsgi import WSGIMiddleware

from app import app as fastapi_app

app = func.AsgiFunctionApp(
    app=fastapi_app, 
    http_auth_level=func.AuthLevel.ANONYMOUS
    )
