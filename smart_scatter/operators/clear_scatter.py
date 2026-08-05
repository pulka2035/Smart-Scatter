import bpy

class SMART_SCATTER_OT_clear(bpy.types.Operator):

    bl_idname = "smart_scatter.clear"
    bl_label = "Clear"

    def execute(self, context):
        output_collection = bpy.data.collections.get("Scatter_Output")
        output_objects = output_collection.objects

        if output_collection is None:
            return {'CANCELLED'}

        for obj in list(output_collection.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(output_collection)
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

