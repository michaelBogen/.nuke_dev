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
mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="MergeOut.png", shortcutContext=2)



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




