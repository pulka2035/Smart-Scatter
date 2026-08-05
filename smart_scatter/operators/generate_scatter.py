import bpy

from ..core.scatter import ScatterGenerator
from ..core.preview_manager import get_preview_manager



class SMART_SCATTER_OT_generate(bpy.types.Operator):

    bl_idname = "smart_scatter.generate"
    bl_label = "Generate Scatter"

    def execute(self, context):

        generator = ScatterGenerator(context)
        generator.generate()

        manager = get_preview_manager()

        if manager.preview:
            preview_collection = bpy.data.collections.get("Smart_Scatter_Preview")
            manager.preview.remove()
            bpy.data.collections.remove(preview_collection)
            manager.stop()

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