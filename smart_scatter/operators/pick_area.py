import bpy

from ..core import placement
from ..core.preview import ScatterPreview
from ..core.preview_manager import get_preview_manager

class SMART_SCATTER_OT_pick_area(bpy.types.Operator):
    bl_idname = "smart_scatter.pick_area"
    bl_label = "Pick Area Center"

    def execute(self, context):

        settings = context.scene.smart_scatter

        self.settings = settings
        self.point = None
        self.preview = None
        self.normal = None


        if settings.surface_object is None:
            self.report(
                {'WARNING'},
                "Please select a Surface Object first"
            )
            return {'CANCELLED'}
        self.surface = settings.surface_object
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


    def modal(self, context, event):

        if event.type == 'MOUSEMOVE':
            result = placement.raycast_surface(
                context,
                event,
                self.surface
            )
            if result is not None:
                point, normal = result
                self.point = point
                self.normal = normal
                self.settings.area_center = point

                if self.preview is None:
                    self.preview = ScatterPreview()
                    self.preview.clear_existing()
                    self.preview.create(
                        point,
                        normal,
                        self.settings
                    )
                    get_preview_manager().start(
                        self.preview
                    )

                else:
                    self.preview.update(
                        point,
                        normal,
                        self.settings
                    )


        if event.type == 'LEFTMOUSE':
            if self.point is not None:
                self.settings.area_center = self.point
                self.settings.area_normal = self.normal
            return {'FINISHED'}


        if event.type in {'RIGHTMOUSE', 'ESC'}:
            if self.preview:
                self.preview.remove()
            return {'CANCELLED'}


        return {'RUNNING_MODAL'}


classes = (
    SMART_SCATTER_OT_pick_area,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)