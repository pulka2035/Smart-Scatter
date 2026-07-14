bl_info = {
    "name": "Smart Scatter",
    "author": "Na_s1",
    "version": (0, 1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar",
    "description": "Procedural asset scattering tool"
}

# import bpy
from . import properties
from . import ui
from . import operators


def register():

    properties.register()
    operators.register()
    ui.register()


def unregister():

    ui.unregister()
    operators.unregister()
    properties.unregister()



if __name__ == "__main__":
    register()
