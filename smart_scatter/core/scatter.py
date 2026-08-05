
import bpy
import random
from mathutils import Quaternion
from mathutils import Euler


from .scatter_points import generate_points
from .placement import project_point_to_surface

class ScatterGenerator:

    def __init__(self, context):

        self.context = context
        self.settings = context.scene.smart_scatter

    def generate(self):

        if not self.validator():
            return

        self.prepare_output_collection()
        points = generate_points(
            self.settings
        )

        assets = self.get_assets()
        distribution = self.choose_assets(assets)

        if len(distribution) < len(points):
            print("Not enough assets in distribution")
            return
        for point, asset in zip(points, distribution):

            self.spawn_object(
                asset,
                point["location"],
                point["normal"]
            )
        


    def validator(self):

        if self.settings.surface_object is None:
            print("No surface selected")
            return False
        
        if self.settings.asset_collection is None:
            print("No asset collection selection")
            return False
        
        if len(self.settings.asset_collection.objects) == 0:
            print("No objects in asset collection")
            return False
        
        return True
    

    def prepare_output_collection(self):

        collection_name = "Scatter_Output"
        collection = bpy.data.collections.get(collection_name)


        if collection is None:

            collection = bpy.data.collections.new(collection_name)
            self.context.scene.collection.children.link(collection)


        self.output_collection = collection

    def get_assets(self):
        return list(self.settings.asset_collection.objects)


    def choose_assets(self, assets):

        count = self.settings.count
        if not assets:
            return []

        result = []
        amount_per_asset = count // len(assets)
        remainder = count % len(assets)


        for asset in assets:

            amount = amount_per_asset

            if remainder > 0:
                amount += 1
                remainder -= 1


            for i in range(amount):
                result.append(asset)


        random.shuffle(result)
        return result



    def spawn_object(
            self,
            asset,
            location,
            normal
    ):

        obj = asset.copy()
        obj.data = asset.data.copy()

        self.output_collection.objects.link(obj)

        obj.location = location

        obj.rotation_mode = 'QUATERNION'


        surface_rotation = normal.to_track_quat(
            'Z',
            'Y'
        )


        random_angle = random.uniform(
            -self.settings.delta_rotation_z,
            self.settings.delta_rotation_z
        )

        random_rotation = Quaternion(
            normal,
            random_angle
        )



        delta_x = random.uniform(
            -self.settings.delta_rotation_x,
            self.settings.delta_rotation_x
        )

        delta_y = random.uniform(
            -self.settings.delta_rotation_y,
            self.settings.delta_rotation_y
        )


        delta_rotation = Euler(
            (
                delta_x,
                delta_y,
                0
            ),
            'XYZ'
        ).to_quaternion()


        obj.rotation_quaternion = (
            surface_rotation
            @ random_rotation
            @ delta_rotation
        )


        scale = random.uniform(
            self.settings.scale_min,
            self.settings.scale_max
        )

        obj.scale = (
            scale,
            scale,
            scale
        )


