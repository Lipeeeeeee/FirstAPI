from fastapi import APIRouter
from firstAPI.controllers.atleta import atleta_router
from firstAPI.controllers.categoria import categoria_router
from firstAPI.controllers.centro_treinamento import centro_treinamento_router

api_router = APIRouter()
api_router.include_router(atleta_router, prefix="/atletas", tags=["atletas/"])
api_router.include_router(categoria_router, prefix="/categorias", tags=["categorias/"])
api_router.include_router(centro_treinamento_router, prefix="/CTs", tags=["CTs/"])