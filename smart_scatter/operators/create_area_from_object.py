import bpy

from ..core.area import get_object_bounds


class SMART_SCATTER_OT_create_area_from_object(
        bpy.types.Operator):

    bl_idname = "smart_scatter.area_from_object"
    bl_label = "Create Area From Object"


    def execute(self, context):

        settings = context.scene.smart_scatter
        obj = context.active_object
        if obj is None:
            self.report(
                {'WARNING'},
                "Select object first"
            )
            return {'CANCELLED'}


        width, depth, height = get_object_bounds(obj)
        settings.width = width + 2
        settings.depth = depth + 2
        settings.area_center = obj.location


        return {'FINISHED'}