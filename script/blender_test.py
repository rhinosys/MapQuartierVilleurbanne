import bpy

# Clear existing objects
bpy.ops.wm.read_factory_settings(use_empty=True)

# Create a new collection for the medallion
medallion_collection = bpy.data.collections.new("MedallionCollection")
bpy.context.scene.collection.children.link(medallion_collection)

# Function to create a simple decorative border
def create_border():
    bpy.ops.mesh.primitive_torus_add(major_radius=1.2, minor_radius=0.1, location=(0, 0, 0))
    border = bpy.context.active_object
    border.name = "Border"
    return border

# Function to create the background plate
def create_background():
    bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=0.1, location=(0, 0, 0))
    background = bpy.context.active_object
    background.name = "Background"
    return background

# Function to create a brocard figure (simplified)
def create_brocard(location):
    bpy.ops.mesh.primitive_monkey_add(size=0.2, location=location)
    brocard = bpy.context.active_object
    brocard.name = "Brocard"
    return brocard

# Function to create a unicorn figure (simplified)
def create_unicorn(location):
    bpy.ops.mesh.primitive_cone_add(radius1=0.1, depth=0.5, location=location)
    unicorn = bpy.context.active_object
    unicorn.name = "Unicorn"
    return unicorn

# Create border and background
border = create_border()
background = create_background()

# Move border and background to the collection
medallion_collection.objects.link(border)
medallion_collection.objects.link(background)
bpy.context.scene.collection.objects.unlink(border)
bpy.context.scene.collection.objects.unlink(background)

# Create three brocards
brocard1 = create_brocard((0.5, 0.5, 0.1))
brocard2 = create_brocard((-0.5, 0.5, 0.1))
brocard3 = create_brocard((0, -0.5, 0.1))

# Create a unicorn
unicorn = create_unicorn((0, 0, 0.1))

# Move brocards and unicorn to the collection
medallion_collection.objects.link(brocard1)
medallion_collection.objects.link(brocard2)
medallion_collection.objects.link(brocard3)
medallion_collection.objects.link(unicorn)
bpy.context.scene.collection.objects.unlink(brocard1)
bpy.context.scene.collection.objects.unlink(brocard2)
bpy.context.scene.collection.objects.unlink(brocard3)
bpy.context.scene.collection.objects.unlink(unicorn)

# Save the Blender file
file_path = "/mnt/data/medallion_brocard_unicorn.blend"
bpy.ops.wm.save_as_mainfile(filepath=file_path)

file_path

