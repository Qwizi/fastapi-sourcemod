
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params

from fastapi_sourcemod_admins.dependencies import get_admins_service, get_valid_admin
from fastapi_sourcemod_admins.models import Admin
from fastapi_sourcemod_admins.schemas import AdminOut, CreateAdminSchema
from fastapi_sourcemod_admins.services import AdminService


router = APIRouter()


@router.get("/")
async def get_admins(
    params: Params = Depends(),
    admin_service: AdminService = Depends(get_admins_service)
) -> Page[AdminOut]:
    admins = await admin_service.get_all(params=params)
    return admins


@router.get("/{identity}")
async def get_admin(
    admin: Admin = Depends(get_valid_admin)
) -> AdminOut:
    return admin

@router.post("/")
async def create_admin(
    data: CreateAdminSchema,
    admins_service: AdminService = Depends(get_admins_service)
):
    new_admin = await admins_service.create(**data.dict())
    return new_admin

@router.delete("/{identity}")
async def delete_admin(
    admin: Admin = Depends(get_valid_admin)
):
    await admin.delete()
    return admin