# Copy and Paste vertex of a mesh in world space
### These two script will help you copy and paste vertex position of one mesh to another so as to move them locally or in World Space
 
This acts like a blendshape set to 1 but without any connector nodes in between and you are free to delete history.
Just select the mesh you want to copy from and use the copy vert script, then select the mesh you want to paste the position of the vertex on and use paste vert script.


# Use case example

Say you have a face or an object with multiple blendshapes to it. You take the master mesh to zbrush, do some sculpting and you bring it in (without changing topo) maya. You want this change to appear on all the blendshape. You can always set this inside maya with a delta blendshape node network but if you want to export it can be a hassle. 
You can use this script to transfer the sculpted mesh detail on to the original head then use "bake topology to blendshape" in maya to transfer the changes to all connected blendshape.

# Note:
Use move topology before baking.
