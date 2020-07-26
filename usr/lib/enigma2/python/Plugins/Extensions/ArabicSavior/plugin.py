# -*- coding: utf-8 -*-

currversion = '1.2'
from Components.ConfigList import ConfigList, ConfigListScreen
from Components.config import config, ConfigDirectory, ConfigSubsection, ConfigSubList, ConfigEnableDisable, ConfigNumber, ConfigText, ConfigSelection, ConfigYesNo, ConfigPassword, getConfigListEntry, configfile
from Components.Label import Label
from Components.MenuList import MenuList
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from enigma import getDesktop,addFont
from Components.Sources.StaticText import StaticText
from Components.ActionMap import ActionMap

config.ArabicSavior = ConfigSubsection()
config.ArabicSavior.active = ConfigEnableDisable(default=True)

skin_hd='''<screen
    position = "center,center"
    size = "533,266"
    title = "  منقذ اللغه العربيه الاصدار الاول د محمود فرج   ">
    <widget
        name = "config"
        position = "7,40"
        size = "519,133"
        scrollbarMode = "showOnDemand"/>
    <ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_red.png"
        position = "200,160"
        zPosition = "0"
        size = "93,27"
        transparent = "1"
        alphatest = "on"/>
    <ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_green.png"
        position = "326,160"
        zPosition = "0"
        size = "93,27"
        transparent = "1"
        alphatest = "on"/>
    <ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_yellow.png"
        position = "266,213"
        zPosition = "0"
        size = "93,27"
        transparent = "1"
        alphatest = "on"/>
    <widget
        render = "Label"
        source = "key_yellow"
        position = "220,233"
        size = "160,27"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;20"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        text = "Activate Arabic"
        shadowOffset = "-1,-1"/>
    <widget
        render = "Label"
        source = "key_red"
        position = "220,153"
        size = "93,27"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;20"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        shadowOffset = "-1,-1"/>
    <widget
        render = "Label"
        source = "key_green"
        position = "346,153"
        size = "93,27"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;20"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        shadowOffset = "-1,-1"/>
</screen>
'''
skin_fhd='''<screen
        position = "center,center"
        size = "800,400" title="  منقذ اللغه العربيه الاصدار الاول د محمود فرج   " >
<widget
name = "config"
position = "10,60"
size = "780,200"
scrollbarMode = "showOnDemand"/>
<ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_red.png"
        position = "300,240"
        zPosition = "0"
        size = "140,40"
        transparent = "1"
        alphatest = "on"/>
    <ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_green.png"
        position = "490,240"
        zPosition = "0"
        size = "140,40"
        transparent = "1"
        alphatest = "on"/>

    <ePixmap
        pixmap = "/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior/images/button_yellow.png"
        position = "400,320"
        zPosition = "0"
        size = "140,40"
        transparent = "1"
        alphatest = "on"/>
<widget
        render = "Label"
        source = "key_yellow"
        position = "330,350"
        size = "240,40"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;28"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        text = "Activate Arabic"
        shadowOffset = "-1,-1"/>        
<widget
        render = "Label"
        source = "key_red"
        position = "330,230"
        size = "140,40"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;28"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        
        shadowOffset = "-1,-1"/>
    <widget
        render = "Label"
        source = "key_green"
        position = "520,230"
        size = "140,40"
        zPosition = "5"
        valign = "center"
        halign = "left"
        backgroundColor = "red"
        font = "Regular;28"
        transparent = "1"
        foregroundColor = "white"
        shadowColor = "black"
        shadowOffset = "-1,-1"/>   
    </screen>'''

class ArabicSaviorSetup(Screen, ConfigListScreen):
    sz_w = getDesktop(0).size().width()
    if sz_w == 1280:
      skin=skin_hd
    else:
      skin=skin_fhd
    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = []
        self.list.append(getConfigListEntry(_('Arabic Savior:'), config.ArabicSavior.active))
        self['config'] = MenuList(self.list)
        self['key_red'] = StaticText(_('الغاء'))
        self['key_green'] = StaticText(_('حفظ'))
        self['key_yellow'] = StaticText(_('Activate Arabic'))
        ConfigListScreen.__init__(self, self.list, session)        
        self['actions'] = ActionMap(['OkCancelActions', 'ColorActions'], {'cancel': self.keyClose,
         'green': self.keySave,'yellow': self.activate}, -1)
  
    def activate(self):
            try:
                fontpath='/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior'
                addFont('%s/font_default.otf' % fontpath, 'ArabicFont', 100, 1)
                print "arabic font added successfully"
            except:
                print "arabic font not added"
            self['key_red'].setText(_('الغاء'))
            self['key_green'].setText(_('حفظ'))
            self.setTitle= "  منقذ اللغه العربيه الاصدار الاول د محمود فرج   "
        
    def keySave(self):
            for x in self['config'].list:
                x[1].save()        
            configfile.save()
            try:
                fontpath='/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior'
                addFont('%s/font_default.otf' % fontpath, 'ArabicFont', 100, 1)
                print "arabic font added successfully"
            except:
                print "arabic font not added"
            self.close()

    def keyClose(self):
        for x in self['config'].list:
            x[1].cancel()
        self.close()

def main(session, **kwargs):
    session.open(ArabicSaviorSetup)

def sessionstart(reason, **kwargs):
    if reason == 0:
        if config.ArabicSavior.active.value == False:
            pass
        else:
            try:
                fontpath='/usr/lib/enigma2/python/Plugins/Extensions/ArabicSavior'
                addFont('%s/font_default.otf' % fontpath, 'ArabicFont', 100, 1)
                print "arabic font added successfully"
            except:
                print "arabic font not added"

def Plugins(**kwargs):
    list = []
    list.append(PluginDescriptor(where=[PluginDescriptor.WHERE_SESSIONSTART], fnc=sessionstart))
    list.append(PluginDescriptor(icon='icon.png', name='Arabic Savior', description='Arabic Savior', where=PluginDescriptor.WHERE_PLUGINMENU, fnc=main))
    return list
