import math

import bpy

MODAL_PIXEL = 32.0
move_x = 0.0
move_y = 0.0


class MOPS_OT_2_4_6_8(bpy.types.Operator):
    """Modal Orbit and Roll
    Move Horizontal - Orbit Left/Right
    Move Vertical - Orbit Up/Down
    Shift + Move Horizontal - Roll Left/Right"""

    bl_idname = "mops.2_4_6_8"
    bl_label = "Modal Numpad 2/4/6/8"
    bl_options = {"GRAB_CURSOR", "BLOCKING"}

    def invoke(self, context, event):
        global move_x, move_y
        move_x = 0.0
        move_y = 0.0
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        global move_x, move_y
        keymap_cancel = []
        keymap_confirm = []
        for i, km in enumerate(context.window_manager.keyconfigs.user.keymaps):
            if km.name == "Transform Modal Map":
                modalmap = context.window_manager.keyconfigs.user.keymaps[i]
                for item in modalmap.keymap_items:
                    if item.propvalue == "CANCEL":
                        keymap_cancel.append(item.type)
                    elif item.propvalue == "CONFIRM":
                        keymap_confirm.append(item.type)

        if (
            event.type in keymap_confirm
            and not event.is_repeat
            and event.value == "PRESS"
        ):
            return {"FINISHED"}
        elif event.type in keymap_cancel:
            return {"CANCELLED"}

        if event.type == "MOUSEMOVE":
            if math.fabs(event.mouse_x - event.mouse_prev_x) > math.fabs(
                event.mouse_y - event.mouse_prev_y
            ):
                delta = event.mouse_x - event.mouse_prev_x
                if move_x < 0.0 and delta > 0.0:
                    move_x = delta
                elif move_x > 0.0 and delta < 0.0:
                    move_x = delta
                else:
                    move_x += delta
                if math.fabs(move_x) > MODAL_PIXEL:
                    orbit_type = "ORBITLEFT"
                    roll_type = "RIGHT"
                    if move_x < 0.0:
                        orbit_type = "ORBITRIGHT"
                        roll_type = "LEFT"
                    for i in range(math.floor(math.fabs(move_x) / MODAL_PIXEL)):
                        if event.shift:
                            bpy.ops.view3d.view_roll(type=roll_type)
                        else:
                            bpy.ops.view3d.view_orbit(type=orbit_type)
                    move_x = 0.0
            else:
                if event.shift:
                    return {"RUNNING_MODAL"}
                delta = event.mouse_y - event.mouse_prev_y
                if move_y < 0.0 and delta > 0.0:
                    move_y = delta
                elif move_y > 0.0 and delta < 0.0:
                    move_y = delta
                else:
                    move_y += delta
                if math.fabs(move_y) > MODAL_PIXEL:
                    orbit_type = "ORBITDOWN"
                    if move_y < 0.0:
                        orbit_type = "ORBITUP"
                    for i in range(math.floor(math.fabs(move_y) / MODAL_PIXEL)):
                        bpy.ops.view3d.view_orbit(type=orbit_type)
                    move_y = 0.0

        return {"RUNNING_MODAL"}
