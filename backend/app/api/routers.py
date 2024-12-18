import fastapi

import app.api.auth.routers
import app.api.utils.routers

api_router = fastapi.APIRouter()

api_router.include_router(app.api.auth.routers.auth_router, prefix='/auth')
api_router.include_router(app.api.utils.routers.utils_router, prefix='/utils')
