from dishka import Container, make_container

from .providers import (
    CoordinatorsProvider,
    DatabaseProvider,
    InjectionsProvider,
    ServiceProvider,
    UIWindowsProvider,
    ViewmodelProvider,
)


def get_container() -> Container:
    return make_container(
        DatabaseProvider(),
        ServiceProvider(),
        ViewmodelProvider(),
        UIWindowsProvider(),
        CoordinatorsProvider(),
        InjectionsProvider(),
    )
