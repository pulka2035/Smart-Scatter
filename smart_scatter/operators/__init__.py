from . import generate_scatter
from . import clear_scatter
from . import pick_area


def register():
    generate_scatter.register()
    clear_scatter.register()
    pick_area.register()

def unregister():
    generate_scatter.unregister()
    clear_scatter.unregister()
    pick_area.unregister()