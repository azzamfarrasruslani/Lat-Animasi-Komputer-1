import bpy

# Menghapus objek teks yang ada
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='FONT')
bpy.ops.object.delete()

# Mengatur rentang untuk X dan Y
x_range = range(-5, 6)  # Dari -10 hingga 10
y_range = range(-5,6)  # Dari -10 hingga 10

# Membuat objek teks untuk setiap kombinasi (x, y)
for x in x_range:
    for y in y_range:
        # Membuat objek teks
        bpy.ops.object.text_add(location=(x, y, 0))
        text_object = bpy.context.object
        
        # Mengatur isi teks
        text_object.data.body = f"({x}, {y})"

        # Mengatur skala dan rotasi (jika perlu)
        text_object.scale = (0.2, 0.2, 0.2)
        text_object.rotation_euler = (0, 0, 0)
