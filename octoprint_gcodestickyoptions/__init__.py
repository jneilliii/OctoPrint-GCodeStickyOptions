# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin


class GcodestickyoptionsPlugin(octoprint.plugin.SettingsPlugin,
                               octoprint.plugin.AssetPlugin,
                               octoprint.plugin.TemplatePlugin
                               ):

    # ~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return {
            "checkboxes": []
        }

    # ~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/gcodestickyoptions.js"]
        }

    # ~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "gcodestickyoptions": {
                "displayName": "Gcodestickyoptions Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "jneilliii",
                "repo": "OctoPrint-GCodeStickyOptions",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/jneilliii/OctoPrint-GCodeStickyOptions/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "Gcodestickyoptions Plugin"
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = GcodestickyoptionsPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
