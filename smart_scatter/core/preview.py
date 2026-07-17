import bpy
import math


class ScatterPreview:

    GRID_SIZE = 1.0
    MIN_RESOLUTION = 5
    MAX_RESOLUTION = 100


    def __init__(self):

        self.collection = None
        self.center = None
        self.area = None

        self.last_shape = None
        self.last_radius = None
        self.last_width = None
        self.last_depth = None


    def update(self, location, normal, settings):

        if self.center is not None:
            self.center.location = location


        if self.area is not None:
            self.area.location = location + normal*0.05
            self.area.rotation_mode = 'QUATERNION'
            self.area.rotation_quaternion = normal.to_track_quat(
                'Z',
                'Y'
            )

            self.update_area(settings)

    def update_area(self, settings):

        if self.area is None:
            return

        verts, faces = self.build_area(settings)
        mesh = self.area.data
        mesh.clear_geometry()
        mesh.from_pydata(
            verts,
            [],
            faces
        )
        mesh.validate()
        mesh.update()
        self.area.data.update()

        mesh.update()
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()


        self.last_shape = settings.area_shape
        self.last_radius = settings.radius
        self.last_width = settings.width
        self.last_depth = settings.depth




    def remove(self):

        if self.center is not None:
            bpy.data.objects.remove(
                self.center,
                do_unlink=True
            )
            self.center = None


        if self.area is not None:
            bpy.data.objects.remove(
                self.area,
                do_unlink=True
            )
            self.area = None



    def create(self, location, normal, settings):
        self.create_collection()
        self.create_center(location)
        self.create_area(
            location,
            normal,
            settings
        )



    def create_collection(self):

        self.collection = self.get_or_create_collection(
            "Smart_Scatter_Preview"
        )


    def get_or_create_collection(self, name):
        collection = bpy.data.collections.get(name)
        if collection is None:
            collection = bpy.data.collections.new(name)
            bpy.context.scene.collection.children.link(
                collection
            )
        return collection

    def create_center(self, location):

        obj = bpy.data.objects.new(
            "Scatter Center",
            None
        )
        obj.empty_display_type = 'SPHERE'
        obj.empty_display_size = 0.5
        obj.location = location
        self.collection.objects.link(obj)

        for selected in bpy.context.selected_objects:
            selected.select_set(False)

        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        self.center = obj

    def create_area(self, location, normal, settings):

        if settings.area_shape == "CIRCLE":

            verts, faces = self.build_grid(
                settings.radius * 2,
                settings.radius * 2,
                shape="CIRCLE",
                radius=settings.radius
            )

        elif settings.area_shape == "RECTANGLE":

            verts, faces = self.build_grid(
                settings.width,
                settings.depth,
                shape="RECTANGLE"
            )
        else:
            return

        self.area = self.create_mesh_object(
            "Scatter Area",
            verts,
            faces,
            location,
            normal
        )

        self.last_shape = settings.area_shape
        self.last_radius = settings.radius
        self.last_width = settings.width
        self.last_depth = settings.depth
        self.area.rotation_mode = 'QUATERNION'
        self.area.rotation_quaternion = normal.to_track_quat(
            'Z',
            'Y'
        )
    def create_mesh_object(self, name, verts, faces, location, normal):
        mesh = bpy.data.meshes.new(name)
        mesh.from_pydata(
            verts,
            [],
            faces
        )
        mesh.validate()
        mesh.update()
        obj = bpy.data.objects.new(
            name,
            mesh
        )
        obj.location = location + normal * 0.05
        self.collection.objects.link(obj)
        return obj



    def calculate_resolution(self, size):
        resolution = int(size / self.GRID_SIZE)
        resolution = max(
            self.MIN_RESOLUTION,
            min(
                resolution,
                self.MAX_RESOLUTION
            )
        )
        return resolution

    def build_grid(
            self,
            width,
            depth,
            shape="RECTANGLE",
            radius=None):

        resolution_x = self.calculate_resolution(width)
        resolution_y = self.calculate_resolution(depth)

        verts = []
        faces = []

        vertex_map = {}

        for y in range(resolution_y + 1):
            py = (
                -depth / 2
                +
                depth / resolution_y * y
            )
            for x in range(resolution_x + 1):
                px = (
                    -width / 2
                    +
                    width / resolution_x * x
                )

                if shape == "CIRCLE":
                    distance = math.sqrt(
                        px * px +
                        py * py
                    )
                    if distance > radius:
                        continue
                index = len(verts)
                vertex_map[(x, y)] = index
                verts.append(
                    (
                        px,
                        py,
                        0
                    )
                )

        for y in range(resolution_y):

            for x in range(resolution_x):


                v1 = vertex_map.get((x, y))
                v2 = vertex_map.get((x + 1, y))
                v3 = vertex_map.get((x + 1, y + 1))
                v4 = vertex_map.get((x, y + 1))


                if None not in (
                    v1,
                    v2,
                    v3,
                    v4
                ):

                    faces.append(
                        (
                            v1,
                            v2,
                            v3,
                            v4
                        )
                    )

        return verts, faces
    def build_area(self, settings):

        if settings.area_shape == "CIRCLE":

            return self.build_grid(
                settings.radius * 2,
                settings.radius * 2,
                shape="CIRCLE",
                radius=settings.radius
            )


        elif settings.area_shape == "RECTANGLE":

            return self.build_grid(
                settings.width,
                settings.depth,
                shape="RECTANGLE"
            )
        


    def clear_existing(self):
        collection = bpy.data.collections.get(
            "Smart_Scatter_Preview"
        )
        if collection:
            for obj in list(collection.objects):
                bpy.data.objects.remove(
                    obj,
                    do_unlink=True
                )
            bpy.data.collections.remove(
                collection,
                do_unlink=True
            )

        self.collection = None