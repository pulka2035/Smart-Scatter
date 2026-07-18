# pyright: reportInvalidTypeForm=false
import bpy

def update_area_size(self, context):

    from ..core.preview_manager import get_preview_manager
    manager = get_preview_manager()
    manager.update(self)

class SMART_SCATTER_Settings(bpy.types.PropertyGroup):

    surface_object: bpy.props.PointerProperty(
        name = "Surface Object",
        type = bpy.types.Object
    )

    asset_collection: bpy.props.PointerProperty(
        name = "Asset Collection",
        type = bpy.types.Collection
    )

    count: bpy.props.IntProperty(
        name = "Count",
        default = 100,
        min = 1,
        max = 100000
    )

    density: bpy.props.FloatProperty(
        name = "Density",
        default = 0.5,
        min = 0.0,
        max = 1.0
    )

    seed: bpy.props.IntProperty(
        name = "Seed",
        default = 1234
    )

    width: bpy.props.FloatProperty(
        name="Width",
        default=20.0,
        min=1.0,
        update=update_area_size
    )


    depth: bpy.props.FloatProperty(
        name="Depth",
        default=20.0,
        min=1.0,
        update=update_area_size
    )

    radius: bpy.props.FloatProperty(
        name="Radius",
        default=5.0,
        min = 1.0,
        update=update_area_size
    )

    scale_max: bpy.props.FloatProperty(
        name = "Max",
        default = 1.2,
        min = 0
    )

    scale_min: bpy.props.FloatProperty(
        name = "Min",
        default = 0.8,
        min = 0
    )

    delta_rotation_x: bpy.props.FloatProperty(
        name="X",
        default=0,
        min=-3.14159,
        max=3.14159,
        subtype="ANGLE"
    )

    delta_rotation_y: bpy.props.FloatProperty(
        name="Y",
        default=0,
        min=-3.14159,
        max=3.14159,
        subtype="ANGLE"
    )


    delta_rotation_z: bpy.props.FloatProperty(
        name="Z",
        default=0,
        min=-3.14159,
        max=3.14159,
        subtype="ANGLE"
    )

    align_to_surface: bpy.props.BoolProperty(
        name = "Align to Surface",
        default = True
    )

    offset: bpy.props.FloatProperty(
        name = "Offset",
        default = 0.1,
        min = 0
    )

    output_collection: bpy.props.PointerProperty(
        name="Output Collection",
        type=bpy.types.Collection
    )   

    minimum_distance: bpy.props.FloatProperty(
        name="Min Distance",
        default=2.0,
        min=0
    )

    area_shape: bpy.props.EnumProperty(
        name="Shape",
        items=[
            ("RECTANGLE", "Rectangle", ""),
            ("CIRCLE", "Circle", ""),
            # ("SQUARE", "Square", ""),
            # ("ELIPSE", "Elipse", ""),
            # ("POLYGON", "Polygon", "")
        ],
        default="RECTANGLE"
    )

    area_center: bpy.props.FloatVectorProperty(
        name="Area Center",
        size=3,
        subtype='XYZ',
        default=(0.0, 0.0, 0.0)
    )

    area_normal: bpy.props.FloatVectorProperty(
        size=3,
        default=(0,0,1)
    )

    area_object: bpy.props.PointerProperty(
        name="Area Object",
        type=bpy.types.Object
    )

    


classes = (
    SMART_SCATTER_Settings,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.smart_scatter = bpy.props.PointerProperty(
        type=SMART_SCATTER_Settings
        )

def unregister():
    del bpy.types.Scene.smart_scatter

    for cls in classes:
        bpy.utils.unregister_class(cls)