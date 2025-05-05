from fastapi import FastAPI
from repository.impl.configuration import ConfigurationRepository
from repository.impl.global_config import GlobalConfigRepository
from service.scheduler import schedule
from fastapi import Depends
from repository.impl.configuration import Time

# this creates repo beans
# 1 for global config
# 1 for configuration


async def get_global_repository() -> GlobalConfigRepository:
    yield GlobalConfigRepository()


async def get_configuration_repository() -> ConfigurationRepository:
    yield ConfigurationRepository()


app = FastAPI()


# Schedule endpoint
@app.get(
    "/schedule",
    dependencies=[
        Depends(get_configuration_repository),
        Depends(get_global_repository),
    ],
    response_model=None
)
def schedule(
    customer_id: str,
    start_time: Time,
    configuration: ConfigurationRepository,
    global_config: GlobalConfigRepository,
):
    schedule(customer_id, start_time, configuration, global_config)


# CRUD on customer configuration
@app.post("/configuration", dependencies=[Depends(get_configuration_repository)])
def create_configuration(customer_id: str, configuration: ConfigurationRepository):
    return configuration.create(customer_id, configuration)


@app.get("/configuration", dependencies=[Depends(get_configuration_repository)])
def get_configuration(customer_id: str, configuration: ConfigurationRepository):
    return configuration.read(customer_id)


@app.put("/configuration", dependencies=[Depends(get_configuration_repository)])
def update_configuration(customer_id: str, configuration: ConfigurationRepository):
    return configuration.update(customer_id, configuration)


@app.delete("/configuration", dependencies=[Depends(get_configuration_repository)])
def delete_configuration(customer_id: str, configuration: ConfigurationRepository):
    return configuration.delete(customer_id)


# CRUD on global config
@app.post("/global_config", dependencies=[Depends(get_global_repository)])
def create_global_config(global_config: GlobalConfigRepository):
    return global_config.create(global_config)


@app.get("/global_config", dependencies=[Depends(get_global_repository)])
def get_global_config(global_config: GlobalConfigRepository):
    return global_config.read()


@app.put("/global_config", dependencies=[Depends(get_global_repository)])
def update_global_config(global_config: GlobalConfigRepository):
    return global_config.update(global_config)


@app.delete("/global_config", dependencies=[Depends(get_global_repository)])
def delete_global_config(global_config: GlobalConfigRepository):
    return global_config.delete()
