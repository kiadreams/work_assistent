from dishka import make_container, Container

from src.di.providers import DatabaseProvider, ServiceProvider


def get_container() -> Container:
    return make_container(
        DatabaseProvider(),
        ServiceProvider(),
    )
