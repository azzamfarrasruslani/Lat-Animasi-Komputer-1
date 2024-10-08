import bpy

#verts = [
#(-3,0,0),(-1,2,0),(1,2,0),(3,0,0),
#(-3,0,0),(-3,-2,0),(3,-2,0),(3,0,0),
#(-3,-2,0),(-1,-4,0),(1,-4,0),(3,-2,0)
#]

#faces = [(0,1,2,3),(4,5,6,7),(8,9,10,11)]

# Definisikan verteks tanpa pengulangan
verts = [
    (-3, 0, 0),   # A
    (-1, 2, 0),   # B
    (1, 2, 0),    # C
    (3, 0, 0),    # D
    (-3, -2, 0),  # E
    (3, -2, 0),   # F
    (-1, -4, 0),  # G
    (1, -4, 0)    # H
]

# Definisikan wajah (faces)
faces = [
    (0, 1, 2, 3),  # Wajah trapesium atas ABCD
    (0, 3, 5, 4),  # Wajah trapesium kiri ADFE
    (4, 5, 7, 6)   # Wajah segi empat EFHG
]


new_mesh=bpy.data.meshes.new("Bintang")
new_mesh.from_pydata(verts,[],faces)
new_mesh.update()
        
       
ob = bpy.data.objects.new("Bintang",new_mesh)

mat=bpy.data.materials.new("Red")
mat.diffuse_color=(1,0,0,0.8)

ob.active_material = mat

bpy.context.collection.objects.link(ob)


