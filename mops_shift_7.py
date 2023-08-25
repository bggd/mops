import bpy


class MOPS_OT_shift7(bpy.types.Operator):
    """View Align
    Scroll - Roll Left/Right"""

    bl_idname = "mops.shift_7"
    bl_label = "Modal Shift Numpad 7"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.object.type == "MESH" and context.mode == "EDIT_MESH"

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        bpy.ops.view3d.view_axis(type="TOP", align_active=True)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
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

        if event.type in keymap_confirm:
            return {"FINISHED"}
        elif event.type in keymap_cancel:
            return {"CANCELLED"}

        if event.type == "WHEELUPMOUSE":
            bpy.ops.view3d.view_roll(type="RIGHT")
        elif event.type == "WHEELDOWNMOUSE":
            bpy.ops.view3d.view_roll(type="LEFT")

        return {"RUNNING_MODAL"}
