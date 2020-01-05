# ----------------------------------------------------------------------------------------
# menu.py
# Version: 1.0.1
# Last Updated: January 4th. 2020
#-----------------------------------------------------------------------------------------

import nuke
import platform
import nukescripts

# Define where .nuke directory is on each OS's network.
Win_Dir = 'C:\Users\michael.bogen\.nuke'
MacOSX_Dir = '/Users/michael/.nuke'
Linux_Dir = '/home/benm/.nuke'

# Automatically set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None


#-----------------------------------------------------------------------------------------
# KNOB DEFAULTS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------

# Set shutter offset to "centered".
nuke.knobDefault('Tracker4.shutteroffset', "centered")
# Set dynamic label on Tracker to display the value of the "transform" and "reference_frame" knobs.
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")

#FrameHold set current frame
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')



#-----------------------------------------------------------------------------------------
# CUSTOM MENUS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------


utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Autocrop', 'nukescripts.autocrop()')


oldNodesMenu = nuke.menu('Nodes').addMenu('oldNodes', icon="oldNodes_icon.png")
oldNodesMenu.addCommand('Blocky', "nuke.createNode('Blocky')")

#-----------------------------------------------------------------------------------------
# MERGE SHORT CUTS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------

mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Add.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="From.png", shortcutContext=2)




#-----------------------------------------------------------------------------------------
# KEYBOARD SHORTCUTS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#-----------------------------------------------------------------------------------------


nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)



# ----- MOTION BLUR SHUTTER CENTERED ---------------------------
nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")


##Hagbarth Tools
toolbar = nuke.toolbar("Nodes")
m = toolbar.addMenu("Higx Tools", icon="higx_tools.png")
m_general = m.addMenu("General",icon="h_pointRender.png")
m_generator = m.addMenu("Generator",icon="h_pointGenerator.png")
m_modifier = m.addMenu("Modifier",icon="h_pointModifier.png")
m_shader = m.addMenu("Shader",icon="h_pointShader.png")

m_general.addCommand("Point_Render", "nuke.createNode(\"Point_Render\")", icon="h_pointRender.png")
m_general.addCommand("Point_3DPreview", "nuke.createNode(\"Point_3DPreview\")", icon="h_pointRender.png")

m_generator.addCommand("Point_Plane", "nuke.createNode(\"Point_Plane\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_Sphere", "nuke.createNode(\"Point_Sphere\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_Torus", "nuke.createNode(\"Point_Torus\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_Cylinder", "nuke.createNode(\"Point_Cylinder\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_UnitSphere_NU", "nuke.createNode(\"Point_UnitSphere\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_Grid_NU", "nuke.createNode(\"Point_Grid\")", icon="h_pointGenerator.png")
m_generator.addCommand("Point_GeoSource_NU", "nuke.createNode(\"Point_GeoSource\")", icon="h_pointGenerator.png")


m_modifier.addCommand("Point_Expression", "nuke.createNode(\"Point_Expression\")", icon="h_pointModifier.png")
m_modifier.addCommand("Point_Fractal_Evolve", "nuke.createNode(\"Point_Fractal_Evolve\")", icon="h_pointModifier.png")
m_modifier.addCommand("Point_Fractal", "nuke.createNode(\"Point_Fractal\")", icon="h_pointModifier.png")
m_modifier.addCommand("Point_RadialForce", "nuke.createNode(\"Point_RadialForce\")", icon="h_pointModifier.png")
m_modifier.addCommand("Point_Transform", "nuke.createNode(\"Point_Transform\")", icon="h_pointModifier.png")
m_modifier.addCommand("Point_Twist", "nuke.createNode(\"Point_Twist\")", icon="h_pointModifier.png")



m_shader.addCommand("Point_Distance", "nuke.createNode(\"Point_Distance\")", icon="h_pointShader.png")
m_shader.addCommand("Point_FractalMask", "nuke.createNode(\"Point_FractalMask\")", icon="h_pointShader.png")
m_shader.addCommand("Point_Light", "nuke.createNode(\"Point_Light\")", icon="h_pointShader.png")
m_shader.addCommand("Point_MotionShader", "nuke.createNode(\"Point_MotionShader\")", icon="h_pointShader.png")
m_shader.addCommand("Point_Normal", "nuke.createNode(\"Point_Normal\")", icon="h_pointShader.png")
m_shader.addCommand("Point_Proximity", "nuke.createNode(\"Point_Proximity\")", icon="h_pointShader.png")
m_shader.addCommand("Point_ReflectionShader", "nuke.createNode(\"Point_ReflectionShader\")", icon="h_pointShader.png")
m_shader.addCommand("Point_Texture", "nuke.createNode(\"Point_Texture\")", icon="h_pointShader.png")
m_shader.addCommand("Point_VectorMathOps", "nuke.createNode(\"Point_Vector_Math_Ops\")", icon="h_pointShader.png")











