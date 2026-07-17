import random
import math
from mathutils import Vector

def generate_points(settings):

    points = []

    count = settings.count
    center = Vector(settings.area_center)
    normal = Vector(settings.area_normal)

    rotation = normal.to_track_quat(
        'Z',
        'Y'
    )


    if settings.area_shape == "RECTANGLE":

        for i in range(count):

            x = random.uniform(
                -settings.width / 2,
                settings.width / 2
            )
            y = random.uniform(
                -settings.depth / 2,
                settings.depth / 2
            )

            local_point = Vector(
                (x, y, 0)
            )
            world_point = (
                center
                +
                rotation @ local_point
            )

            points.append(
                {
                    "location": world_point,
                    "normal": normal
                }
            )


    elif settings.area_shape == "CIRCLE":

        for i in range(count):

            angle = random.uniform(
                0,
                math.tau
            )
            radius = math.sqrt(
                random.random()
            ) * settings.radius

            x = math.cos(angle) * radius
            y = math.sin(angle) * radius

            local_point = Vector(
                (x, y, 0)
            )
            world_point = (
                center
                +
                rotation @ local_point
            )

            points.append(
                {
                    "location": world_point,
                    "normal": normal
                }
            )


    return points