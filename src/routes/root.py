from fastapi import APIRouter, Depends
from helpers.config import get_settings, Settings

root_router = APIRouter(
    tags=["Root"]
)

@root_router.get("/")
async def get_app_info(app_settings: Settings = Depends(get_settings)):

    return {"app_name": app_settings.APP_NAME,
            "app_version": app_settings.APP_VERSION,
    }
