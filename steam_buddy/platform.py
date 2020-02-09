from typing import List
from steam_buddy.app import App


class Platform:
    def __init__(self, platform_id: str, name: str):
        self.__name = name
        self.__platform_id = platform_id

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__platform_id

    def get_installed_apps(self) -> List[App]:
        raise NotImplementedError('Function get_installed_apps has not been implemented yet')

    def add_app(self, app: App) -> (bool, str):
        raise NotImplementedError('Function add_app has not been implemented yet')

    def remove_app(self, app: App) -> (bool, str):
        raise NotImplementedError('Function remove_app has not been implemented yet')

    def get_new_template(self) -> List:
        raise NotImplementedError('Function get_name has not been implemented yet')

    def get_edit_template(self) -> List:
        raise NotImplementedError('Function get_name has not been implemented yet')

    def get_launch_command(self):
        raise NotImplementedError('Function get_launch_command has not been implemented yet')

    def get_banner(self) -> str:
        raise NotImplementedError('Function get_banner has not been implemented yet')


class PlatformWithLocalContent(Platform):
    def get_content_dir(self) -> str:
        raise NotImplementedError('Function get_available_apps has not been implemented yet')


class PlatformWithRemoteContent(Platform):
    def get_available_apps(self) -> List[App]:
        raise NotImplementedError('Function get_available_apps has not been implemented yet')
