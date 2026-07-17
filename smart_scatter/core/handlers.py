# import bpy

from .preview_manager import get_preview_manager


def preview_update_handler(scene):

    settings = scene.smart_scatter
    manager = get_preview_manager()
    manager.update(settings)


# def register():

#     bpy.app.handlers.depsgraph_update_post.append(
#         preview_update_handler
#     )


# def unregister():

#     bpy.app.handlers.depsgraph_update_post.remove(
#         preview_update_handler
#     )