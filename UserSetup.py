
import pymel.core as pmc
import maya.cmds as cmds
import qbMayaQueMenu
pmc.evalDeferred('qbMayaQueMenu.setupQueMenu()')


cmds.setAttr ( 'defaultResolution.w' , 1920 )
cmds.setAttr ( 'defaultResolution.h' , 1080 )
cmds.loadPlugin("MayaScanner", quiet=True)
cmds.pluginInfo("MayaScanner", edit=True, autoload=True)
cmds.loadPlugin("MayaScannerCB", quiet=True)
cmds.pluginInfo("MayaScannerCB", edit=True, autoload=True)
cmds.evalDeferred('cmds.loadPlugin("mtoa")')
pmc.optionVar(stringValue=('workingUnitLinear', 'cm'))
pmc.optionVar(stringValue=('workingUnitLinearDefault', 'cm'))
pmc.optionVar(stringValue=('workingUnitAngular', 'deg'))
pmc.optionVar(stringValue=('workingUnitAngularDefault', 'deg'))

def delayedStartup(*args, **kwargs):
    # cmds.colorManagementPrefs(e=True, renderingSpaceName="ACEScg")
    # cmds.colorManagementPrefs(e=True, displayName="sRGB")
    # cmds.colorManagementPrefs(e=True, viewName="Un-tone-mapped")
    cmds.currentUnit(time = '23.976fps')

maya.utils.executeDeferred('delayedStartup()') 
import maya.OpenMaya as om
om.MSceneMessage.addCallback(om.MSceneMessage.kAfterNew, delayedStartup)

