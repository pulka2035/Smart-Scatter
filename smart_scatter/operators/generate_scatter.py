import bpy

class SMART_SCATTER_OT_generate(bpy.types.Operator):

    bl_idname = "smart_scatter.generate"
    bl_label = "Generate Scatter"

    def execute(self, context):
        return {'FINISHED'}

classes = (
    SMART_SCATTER_OT_generate,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)