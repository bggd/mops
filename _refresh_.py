from importlib import reload
import sys
import bpy

from . import mops_shift_7, mops_2_4_6_8


def reload_modules():
    if not bpy.context.preferences.view.show_developer_ui:
        return

    reload(mops_shift_7)
    reload(mops_2_4_6_8)
    reload(sys.modules[__name__])
