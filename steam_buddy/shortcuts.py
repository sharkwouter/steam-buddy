import os
import yaml
from steam_buddy.config import SHORTCUT_DIR


def add_shortcut(platform, app) -> (bool, str):
    # Make sure the shortcut directory exists
    if not os.path.exists(SHORTCUT_DIR):
        os.makedirs(SHORTCUT_DIR)

    shortcuts_file = os.path.join(SHORTCUT_DIR, "steam-buddy.{}.yaml".format(platform.get_id()))
    shortcuts = get_shortcuts(platform)

    matches = [e for e in shortcuts if e['name'] == app.name and e['cmd'] == platform.get_id()]
    if len(matches) != 0:
        shortcuts.remove(matches[0])

    # Collect the information for the new shortcut
    shortcut_data = {
        'name': app.name,
        'cmd': platform.get_launch_command(),
        'hidden': app.hidden,
        'tags': [platform.get_id()],
        'params': app.params,
        'banner': app.banner
    }

    # A banner image is optional
    if shortcut_data['banner']:
        shortcut_data['banner'] = platform.get_banner()
    try:
        shortcut_data['dir'] = platform.get_content_dir()
    except:
        pass

    # Add the shortcut
    shortcuts.append(shortcut_data)
    yaml.dump(shortcuts, open(shortcuts_file, 'w'), default_flow_style=False)


def get_shortcuts(platform):
    shortcuts = []
    shortcuts_file = os.path.join(SHORTCUT_DIR, "steam-buddy.{}.yaml".format(platform.get_id()))
    if os.path.isfile(shortcuts_file):
        shortcuts = yaml.load(open(shortcuts_file), Loader=yaml.Loader)
    return shortcuts


def remove_shortcut(platform, app):
    shortcuts_file = os.path.join(SHORTCUT_DIR, "steam-buddy.{}.yaml".format(platform.get_id()))
    shortcuts = get_shortcuts(platform)

    matches = [e for e in shortcuts if e['name'] == app.name and e['cmd'] == platform.get_id()]
    shortcut = matches[0]

    shortcuts.remove(shortcut)
    yaml.dump(shortcuts, open(shortcuts_file, 'w'), default_flow_style=False)
