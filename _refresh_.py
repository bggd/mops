from importlib import reload
import sys
import bpy

from . import mops_shift7


def reload_modules():
    if not bpy.context.preferences.view.show_developer_ui:
        return

    reload(mops_shift7)
    reload(sys.modules[__name__])
