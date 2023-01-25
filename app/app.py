import os
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from loguru import logger

from models import ResponseModel
from utils import get_homebridge_config

app = FastAPI(
    title="Jablotron config helper for Homebridge",
    description="Simple API that helps you get the config for Jablotron in Homebridge.",
    version=os.environ.get("API_VERSION", "dev"),
    redoc_url=None,
    swagger_ui_parameters={"docExpansion": "full", "defaultModelsExpandDepth": -1}
)


@app.post("/config/homebridge", response_model=ResponseModel, tags=["Config helper"])
async def generate_config(username, password):
    _uuid = str(uuid.uuid4())
    try:
        config = get_homebridge_config(username=username, password=password)
        response = {"status": "OK", "configs": []}
        for i in config:
            response["configs"].append(i)
        return response
    except KeyError:
        raise HTTPException(status_code=404, detail="User not found, probably incorrect credentials")
    except Exception as E:
        logger.error(f"{_uuid}, error: {str(E)}")
        raise HTTPException(status_code=500, detail=f"Something went wrong")


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')
