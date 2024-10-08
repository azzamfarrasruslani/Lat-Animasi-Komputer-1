import bpy

verts = [
(0,-3,0),(0,4,0),(3,-5,0),
(0,-3,0),(0,4,0),(-3,-5,0),
(-5,0,0),(5,0,0),(0,-3,0)
]

faces = [(0,1,2),(3,4,5),(6,7,8)]

new_mesh=bpy.data.meshes.new("Bintang")
new_mesh.from_pydata(verts,[],faces)
new_mesh.update()
        
       
ob = bpy.data.objects.new("Bintang",new_mesh)

mat=bpy.data.materials.new("Red")
mat.diffuse_color=(1,0,0,0.8)

ob.active_material = mat

bpy.context.collection.objects.link(ob)


