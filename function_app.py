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
# app.middleware.handle_async(
#         context=func.Context(),
#         req=func.HttpRequest())

# Add fastapi middleware

# async def azure_func(req: func.HttpRequest, ctx: func.Context) -> func.HttpResponse:
#     return 

# @app.route(route="azure_func", auth_level=func.AuthLevel.ANONYMOUS)
# def azure_func(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )
        
        
        
# app.add_middleware(middleware_class=fastapi_middleware, path="/api/v1")