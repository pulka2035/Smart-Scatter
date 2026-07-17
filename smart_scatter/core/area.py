import mathutils


def get_object_bounds(obj):

    corners = [
        obj.matrix_world @ mathutils.Vector(corner)
        for corner in obj.bound_box
    ]

    min_x = min(v.x for v in corners)
    max_x = max(v.x for v in corners)

    min_y = min(v.y for v in corners)
    max_y = max(v.y for v in corners)

    min_z = min(v.z for v in corners)
    max_z = max(v.z for v in corners)

    return (
        max_x - min_x,
        max_y - min_y,
        max_z - min_z
    )