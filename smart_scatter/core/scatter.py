
import bpy

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
        print("POINT COUNT:", len(points))
        print(points[:5])
        assets = self.get_assets()

        for point in points:
            
            asset = assets[0]
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
        
        total_weight = 0
        assets_weight = {}

        for asset in assets:
            weight = 1
            assets_weight[asset] = weight
            total_weight += 1

        result = []
        
        for asset in assets:
            percentage = assets_weight[asset] / total_weight
            amount = round(percentage * count)

            result.append(
                {
                    "asset": asset,
                    "amount": amount,
                    "weight": assets_weight[asset]
                }
            )
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

        obj.rotation_quaternion = normal.to_track_quat(
            'Z',
            'Y'
        )


