

# this creates repo beans 
# 1 for global config
# 1 for configuration

async def get_global_repository() -> GlobalConfigRepository:
    return GlobalConfigRepository()

async def get_configuration_repository() -> ConfigurationRepository:
    return ConfigurationRepository()