from fastapi import HTTPException
from utils.date import get_day
from repository.impl.configuration import ConfigurationRepository
from repository.impl.global_config import GlobalConfigRepository
from data_model import Time


days_to_ordinals = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}


def schedule(
    customer_id: str,
    start_time: Time,
    configuration: ConfigurationRepository,
    global_config: GlobalConfigRepository,
):
    if configuration.read(customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    elif global_config.read() is None:
        raise HTTPException(status_code=404, detail="Global config not found")

    day = get_day(start_time)
    if day not in days_to_ordinals:
        raise HTTPException(status_code=404, detail="Day not found")
    customer_configuration = configuration.read(customer_id)
    start_day = day
    while start_day != day:
        for configuration in customer_configuration.configurations.values():
            for time_slot in configuration.available_time_slots:
                if time_slot.start_time <= start_time <= time_slot.end_time:
                    return True
        start_day = (start_day + 1) % 7
    return False
