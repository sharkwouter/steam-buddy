from typing import List
from steam_buddy.platform import PlatformWithLocalContent
from steam_buddy.app import App
from steam_buddy.shortcuts import get_shortcuts


class Emulator(PlatformWithLocalContent):
    def add_app(self, app: App) -> None:
        pass

    def get_installed_apps(self) -> List[App]:
        print("this is getting called")
        apps = []
        shortcuts = get_shortcuts(self)
        for shortcut in shortcuts:
            apps.append(
                App(shortcut['name'], shortcut['params'], shortcut['hidden'], shortcut['banner'])
            )
        return apps


