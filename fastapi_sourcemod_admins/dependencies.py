
from fastapi import Depends
from ormar import NoMatch
from fastapi_sourcemod_admins.services import AdminService, GroupService, admin_not_found_exception, group_not_found_exception


async def get_admins_service() -> AdminService:
    return AdminService()


async def get_valid_admin(
        identity: str,
        admin_service: AdminService = Depends(get_admins_service)
):
    try:
        return await admin_service.get_one(
            identity=identity
        )
    except NoMatch:
        raise admin_not_found_exception
    
async def get_groups_service() -> GroupService:
    return GroupService()

async def get_valid_group(
        group_id: int,
        group_service: GroupService = Depends(get_groups_service)
):
    try:
        return await group_service.get_one(
            id=group_id
        )
    except NoMatch:
        raise group_not_found_exception
    