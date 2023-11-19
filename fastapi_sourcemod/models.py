from typing import Optional
import ormar

from fastapi_sourcemod.db import BaseMeta, DateFieldsMixins
from fastapi_sourcemod.enums import AuthTypeEnum


class Group(ormar.Model, DateFieldsMixins):
    class Meta(BaseMeta):
        tablename = "sm_groups"

    id: int = ormar.Integer(primary_key=True)
    flags: Optional[str] = ormar.String(max_length=30)
    name: Optional[str] = ormar.String(max_length=65)
    immunity_level: Optional[int] = ormar.Integer()


class Admin(ormar.Model, DateFieldsMixins):
    class Meta(BaseMeta):
        tablename = "sm_admins"

    id: int = ormar.Integer(primary_key=True)
    authtype: Optional[str] = ormar.String(
        max_length=5, choices=list(AuthTypeEnum), default=AuthTypeEnum.STEAM.value
    )
    identity: Optional[str] = ormar.String(max_length=65)
    password: Optional[str] = ormar.String(max_length=65, nullable=True)
    flags: Optional[str] = ormar.String(max_length=30)
    name: Optional[str] = ormar.String(max_length=65)
    immunity: Optional[str] = ormar.Integer()
    groups: Optional[Group] = ormar.ManyToMany(
        Group,
        through_relation_name="admin_id",
        through_reverse_relation_name="group_id",
    )
