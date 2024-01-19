from fastapi import APIRouter

routes = APIRouter()

@routes.get('/my_route')
async def route_api():
    return {"ok": "true"}