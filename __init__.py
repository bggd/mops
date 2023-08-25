# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "mops",
    "author": "birthggd",
    "description": "modal operations",
    "blender": (3, 6, 0),
    "version": (0, 0, 0),
    "location": "",
    "warning": "",
    "category": "3D View",
}

import bpy

from . import _refresh_
from .mops_shift7 import *

_refresh_.reload_modules()

classes = (MOPS_OT_shift7,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
