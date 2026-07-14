from . import generate_scatter
from . import clear_scatter

def register():
    generate_scatter.register()
    clear_scatter.register()

def unregister():
    generate_scatter.unregister()
    clear_scatter.unregister()