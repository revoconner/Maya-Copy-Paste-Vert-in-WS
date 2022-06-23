from maya import cmds
import maya.api.OpenMaya as om
sel = cmds.ls(sl=True)
selection_list = om.MSelectionList ()
selection_list.add(sel[0])
dag_path = selection_list.getDagPath (0)
mfn_mesh = om.MFnMesh(dag_path)
points = mfn_mesh.getPoints()
