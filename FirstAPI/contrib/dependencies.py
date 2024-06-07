from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from firstAPI.configs.database import get_session

database_dependency = Annotated[AsyncSession, Depends(get_session)]