from bpy_extras import view3d_utils
from mathutils import Vector

def raycast_surface(context, event, surface):

    region = context.region
    rv3d = context.region_data

    if rv3d is None:
        return None


    mouse_coord = (
        event.mouse_region_x,
        event.mouse_region_y
        )


    ray_origin = view3d_utils.region_2d_to_origin_3d(
        region,
        rv3d,
        mouse_coord
    )


    ray_direction = view3d_utils.region_2d_to_vector_3d(
        region,
        rv3d,
        mouse_coord
    )


    hit, location, normal, index = surface.ray_cast(
        ray_origin,
        ray_direction
    )


    if hit:
        return location, normal


    return None


def project_point_to_surface(point, surface):

    origin = point + Vector((0,0,10))
    direction = Vector((0,0,-1))

    hit, location, normal, index = surface.ray_cast(
        origin,
        direction
    )

    if hit:
        return location, normal

    return None, None