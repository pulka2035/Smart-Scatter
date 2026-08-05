import bpy

class SMART_SCATTER_PT_mainPanel(bpy.types.Panel):

    bl_idname = "SMART_SCATTER_PT_mainPanel"
    bl_label = "Smart Scatter"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Smart Scatter"

    def draw_header(self, context):
        self.layout.label(text="🌲")

    def draw(self, context):
        layout = self.layout
        settings = context.scene.smart_scatter

        layout.label(text="  Smart Scatter Tool")


        # Surface
        surface_box = layout.box()
        surface_box.label(text="  Surface")

        surface_box.prop(settings, "surface_object", text = "")


        # Assets
        assets_box = layout.box()
        assets_box.label(text="  Assets")

        assets_box.prop(settings, "asset_collection", text = "")


        # Scatter Settings
        settings_box = layout.box()
        settings_box.label(text="  Scatter Settings")

        column_settings_box = settings_box.column(align=True)
        column_settings_box.use_property_split = True
        column_settings_box.use_property_decorate = False

        # column_settings_box.prop(settings, "density")
        column_settings_box.prop(settings, "count")
        # column_settings_box.prop(settings, "minimum_distance")
        # column_settings_box.prop(settings, "seed")




        # Area
        area_box = layout.box()
        area_box.label(text="  Area")

        row = area_box.row()
        row.enabled = settings.surface_object is not None
        row.operator("smart_scatter.pick_area", text="Pick Area Center")

        area_box.prop(settings, "area_center")
        area_box.prop(settings, "area_shape")
        

        column_area_box = area_box.column(align=True)
        column_area_box.use_property_split = True
        column_area_box.use_property_decorate = False

        if settings.area_shape == "RECTANGLE":
            column_area_box.prop(settings, "width")
            column_area_box.prop(settings, "depth")
        
        elif settings.area_shape == "CIRCLE":
            column_area_box.prop(settings, "radius")




        # Transform
        transform_box = layout.box()
        transform_box.label(text="  Transform")
        transform_box.label(text="Scale")

        column_transform_box_1 = transform_box.column(align=True)
        column_transform_box_1.use_property_decorate = False

        column_transform_box_1.prop(settings, "scale_min")
        column_transform_box_1.prop(settings, "scale_max")

        transform_box.label(text="Rotation")

        column_transform_box_2 = transform_box.column(align=True)
        column_transform_box_2.use_property_decorate = False

        column_transform_box_2.prop(settings, "delta_rotation_x")
        column_transform_box_2.prop(settings, "delta_rotation_y")
        column_transform_box_2.prop(settings, "delta_rotation_z")

        # Alignment
        # alignment_box = layout.box()
        # alignment_box.label(text="  Alignment")

        # alignment_box.prop(settings, "align_to_surface")
        # alignment_box.prop(settings, "offset")

        #Generate Scatter
        layout.separator()
        layout.operator("smart_scatter.generate", text = "<< Generate Scatter >>")

        #Clear
        layout.operator("smart_scatter.clear", text = "<< Clear >>")






classes = (
    SMART_SCATTER_PT_mainPanel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)