import bpy

class SMART_SCATTER_OT_clear(bpy.types.Operator):

    bl_idname = "smart_scatter.clear"
    bl_label = "Clear"

    def execute(self, context):
        return {'FINISHED'}
    
classes = (
    SMART_SCATTER_OT_clear,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

