

from pydantic import BaseModel


class GlobalConfig(BaseModel):
    permissible_start_time: str
    permissible_end_time: str
    tz: str
    country: str


class GlobalConfigRepository(BaseRepository[GlobalConfig]):
    def __init__(self):
        super().__init__()
        
    