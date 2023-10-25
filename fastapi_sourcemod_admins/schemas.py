
from typing import Optional
from pydantic import BaseModel
from fastapi_sourcemod_admins.enums import AuthTypeEnum
from fastapi_sourcemod_admins.models import Admin, Group


admin_out =  Admin.get_pydantic()
group_out = Group.get_pydantic()

class AdminOut(admin_out):
    pass

class GroupOut(group_out):
    pass

class CreateAdminSchema(BaseModel):
    authtype: Optional[AuthTypeEnum]
    identity: str
    password: Optional[str]
    flags: str
    name: str
    immunity: int

class CreateGroupSchema(BaseModel):
    name: str
    immunity_level: int
    flags: str