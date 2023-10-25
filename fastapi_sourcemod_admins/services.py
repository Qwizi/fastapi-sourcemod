
from fastapi import HTTPException
from fastapi_sourcemod_admins.db import BaseService
from fastapi_sourcemod_admins.models import Admin, Group


admin_not_found_exception = HTTPException(
    status_code=404,
    detail="Admin not found",
)

group_not_found_exception = HTTPException(
    status_code=404,
    detail="Group not found",
)

class AdminService(BaseService):
    
    class Meta:
        model = Admin
        not_found_exception = admin_not_found_exception


class GroupService(BaseService):
    
    class Meta:
        model = Group
        not_found_exception = group_not_found_exception