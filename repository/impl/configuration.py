from pydantic import BaseModel
from repository.base import BaseRepository


class Time(BaseModel):
    date: str
    hour: str
    minute: str
    second: str
    unit: str


class TimeSlot(BaseModel):
    start_time: Time
    end_time: Time


class CustomerConfiguration(BaseModel):
    available_time_slots: list[TimeSlot]


class Configuration(BaseModel):
    customer_id: str
    configurations: dict[str, CustomerConfiguration]


class ConfigurationRepository(BaseRepository[Configuration]):
    def __init__(self):
        super().__init__()
