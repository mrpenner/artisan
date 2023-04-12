import prettytable
import re
try:
    from PyQt6.QtWidgets import QApplication # @Reimport @UnresolvedImport @UnusedImport # pylint: disable=import-error
except Exception: # pylint: disable=broad-except
    from PyQt5.QtWidgets import QApplication # type: ignore # @Reimport @UnresolvedImport @UnusedImport

def content():
    strlist = []
    helpstr = ''  # noqa: F841 #@UnusedVariable # pylint: disable=unused-variable
    newline = '\n'  # noqa: F841 #@UnusedVariable  # pylint: disable=unused-variable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append('<b>')
    strlist.append(QApplication.translate('HelpDlg','KEYBOARD SHORTCUTS'))
    strlist.append('</b>')
    tbl_KeyboardShortcuts = prettytable.PrettyTable()
    tbl_KeyboardShortcuts.field_names = [QApplication.translate('HelpDlg','Keys'),QApplication.translate('HelpDlg','Description')]
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','ENTER'),QApplication.translate('HelpDlg','Turns ON/OFF Keyboard Shortcuts')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','SPACE'),QApplication.translate('HelpDlg','When Keyboard Shortcuts are ON chooses the current button\nWhen Keyboard Shortcuts are OFF adds a custom event')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','LEFT,RIGHT,UP,DOWN'),QApplication.translate('HelpDlg','Move background or key focus')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','A'),QApplication.translate('HelpDlg','Autosave')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','⌘-N [Mac]\nCRTL+N [Win]'),QApplication.translate('HelpDlg','Autosave + RESET + START')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','T [Mac]\nCTRL+SHIFT+T [Win]'),QApplication.translate('HelpDlg','Toggle mouse cross lines')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','G'),QApplication.translate('HelpDlg','Toggle auto axis mode between Roast, BBP+Roast and BBP')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','D'),QApplication.translate('HelpDlg','Toggle xy cursor mode (off/temp/delta)')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','Z'),QApplication.translate('HelpDlg','Toggle xy cursor clamp mode (off/BT/ET/BTB/ETB)')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','U'),QApplication.translate('HelpDlg','Toggle LCD cursor (off/profile/background)')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','C'),QApplication.translate('HelpDlg','Shows/Hides Controls')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','X'),QApplication.translate('HelpDlg','Shows/Hides LCD Readings')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','Y'),QApplication.translate('HelpDlg','Shows/Hides Mini Event editor (on recording)')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','M'),QApplication.translate('HelpDlg','Shows/Hides Event Buttons')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','B'),QApplication.translate('HelpDlg','Shows/Hides Extra Event Buttons')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','S'),QApplication.translate('HelpDlg','Shows/Hides Event Sliders')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','P'),QApplication.translate('HelpDlg','Toggle PID mode')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','J'),QApplication.translate('HelpDlg','Toggle Playback Events')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','H\nCTRL+H [Win]'),QApplication.translate('HelpDlg','Load background profile')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','OPTION+H [Mac]\nCTRL+SHIFT+H [Win]'),QApplication.translate('HelpDlg','Remove background profile')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','I'),QApplication.translate('HelpDlg','Toggle foreground curves “show full”')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','OPTION+H [Mac]\nCTRL+SHIFT+H [Win]'),QApplication.translate('HelpDlg','Toggle background curves “show full”')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','L'),QApplication.translate('HelpDlg','Load alarms')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','+,-'),QApplication.translate('HelpDlg','Inc/dec PID lookahead')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','⌘ +,- [Mac]\nCRTL +,- [Win]'),QApplication.translate('HelpDlg','Inc/dec graph resolution')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','⌘ 0-9 [Mac]\nCRTL 0-9 [Win]'),QApplication.translate('HelpDlg','Changes Event Button Palettes')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg',';'),QApplication.translate('HelpDlg','Application ScreenShot')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg',':'),QApplication.translate('HelpDlg','Desktop ScreenShot')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','Q,W,E,R + <value>'),QApplication.translate('HelpDlg','Quick Special Event Entry.  The keys q,w,e, and r correspond to special events 1,2,3 and 4.  A two digit numeric value must follow the shortcut letter, e.g. &#39;q75&#39;, when the correspoding event slider max value is 100 or less (default setting).   When the slider max value is greater than 100, three digits must be entered and for values less that 100 a leading zero is required, e.g. &#39;q075&#39;.  ')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','V +  <value>'),QApplication.translate('HelpDlg','Quick PID SV Entry.  Value is a three digit number.  For values less than 100 must be entered with a leading zero, e.g. &#39;v075&#39;.')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','OPTION+B + <value> [Mac]\nCTRL+SHIFT+B + <value> [Win]'),QApplication.translate('HelpDlg','Fire custom event button action. Value is a two digit number indicating the button number.')])
    tbl_KeyboardShortcuts.add_row([QApplication.translate('HelpDlg','F\nCTRL+SHIFT+F [Win]'),QApplication.translate('HelpDlg','Full Screen Mode')])
    strlist.append(tbl_KeyboardShortcuts.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','ADDITIONAL SHORTCUTS'))
    strlist.append('</b>')
    tbl_AddlShortcuts = prettytable.PrettyTable()
    tbl_AddlShortcuts.field_names = [QApplication.translate('HelpDlg','Key/mouse stroke(s)'),QApplication.translate('HelpDlg','Where'),QApplication.translate('HelpDlg','Action'),QApplication.translate('HelpDlg','Additional Information')]
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Double click on Roast Title'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Open the roast in artisan.plus'),QApplication.translate('HelpDlg','Requires an artisan.plus account')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on Background Profile Title'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle Show/Hide Background Profile'),QApplication.translate('HelpDlg','Only when a Background profile is loaded')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Right click on BT curve'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Place or re-place events'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Right click on timer'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle super mode'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Right click on characteristics line below graph'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle set of characteristics displayed'),QApplication.translate('HelpDlg','Characteristics must be enabled in Config>> Statistics')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on plus icon (when not red)'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle connect/disconnect to plus'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on plus icon (when it is red)'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Sync the roast with artisan.plus'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘ click on plus icon [Mac]\nCTRL click on plus icon [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','When connected to plus, disconnect and clear credentials'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION click on plus icon [Mac]\nALT click on plus icon [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Generate email message with Artisan Logs'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+OPTION click on plus icon [Mac]\nCTRL+ALT click on plus icon [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle debug logging mode'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on timer'),QApplication.translate('HelpDlg','Simulator'),QApplication.translate('HelpDlg','Toggle Pause/Continue Simulation'),QApplication.translate('HelpDlg','Simulator speed may be changd while paused.  See next two shortcuts.')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION Tools>>Simulator [Mac]\nALT Tools>>Simulator [Win]'),QApplication.translate('HelpDlg','Graph/Simulator'),QApplication.translate('HelpDlg','Start or change Simulator speed to 2x mode'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘ Tools>>Simulator [Mac]\nCTRL Tools>>Simulator [Win]'),QApplication.translate('HelpDlg','Graph/Simulator'),QApplication.translate('HelpDlg','Start or change Simulator speed to 4x mode'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on LCD'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Hide or Show corresponding Curve'),QApplication.translate('HelpDlg','In  OFF state this changes the Artisan Settings, in ON/START states the change is temporary until OFF state')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on label in the Legend'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Hide or Show corresponding Curve'),QApplication.translate('HelpDlg','Only in OFF state when the Legend is displayed')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION click &#39;RESET&#39; Button [Mac]\nALT click &#39;RESET&#39; Button [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Detach IO Phidgets'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘ click &#39;Control&#39; Button [Mac]\nCTRL click &#39;Control&#39; Button [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle PID Standby on and off'),QApplication.translate('HelpDlg','Device = Fuji or Delta')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘ click &#39;Control&#39; Button [Mac]\nCTRL click &#39;Control&#39; Button [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Opens PID dialog'),QApplication.translate('HelpDlg','Device = Hottop')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘ click &#39;Control&#39; Button [Mac]\nCTRL click &#39;Control&#39; Button [Win]'),QApplication.translate('HelpDlg','Graph'),QApplication.translate('HelpDlg','Toggle PID'),QApplication.translate('HelpDlg','Device = <all others>, Control enabled in Config>> Device')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+C [Mac]\nCTRL+C [Win]'),QApplication.translate('HelpDlg','Roast Properties Data tab'),QApplication.translate('HelpDlg','Copy table'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+L [Mac]\nCTRL+L [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Open volume calculator'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Enter'),QApplication.translate('HelpDlg','Roast Properties Roast Tab\nVolume Calculator Unit, Green Unit  Weight or Roasted Unit Weight field'),QApplication.translate('HelpDlg','Overwrite with current scale weight (same action as &#39;unit&#39;, &#39;in&#39;, &#39;out&#39; buttons)'),QApplication.translate('HelpDlg','Requires a connected scale')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Enter'),QApplication.translate('HelpDlg','Roast Properties Roast tab\nGreen Weight  or Roasted Weight field'),QApplication.translate('HelpDlg','Overwrite with current scale weight'),QApplication.translate('HelpDlg','Requires a connected scale')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+I [Mac]\nCTRL+I [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Adds scale weight to Green Weight field (same action as &#39;in&#39; button)'),QApplication.translate('HelpDlg','Requires a connected scale')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+O [Mac]\nCTRL+O [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Adds scale weight to Roasted Weight field (same action as &#39;out&#39; button)'),QApplication.translate('HelpDlg','Requires a connected scale')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','⌘+P [Mac]\nCTRL+P [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Clear accumulated scale weight preview display (same as clicking on the preview display)'),QApplication.translate('HelpDlg','Requires a connected scale')])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION click  &#39;+&#39;  button [Mac]\nALT click  &#39;+&#39;  button [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Adds Weight Roasted, Volume Roasted, Moisture Roasted, ColorWhole, and Color Ground to the recent roast'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION File>> New>> <recent-roast> [Mac]\nALT File>> New>> <recent-roast> [Win]'),QApplication.translate('HelpDlg','Roast Properties Roast tab'),QApplication.translate('HelpDlg','Sets roast properties to <recent-roast> without starting a new roast'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','OPTION click &#39;Copy Table&#39; Button [Mac]\nALT click &#39;Copy Table&#39; Button [Win]'),QApplication.translate('HelpDlg','Various'),QApplication.translate('HelpDlg','For various tables this copies the table in tabular form'),'&#160;'])
    tbl_AddlShortcuts.add_row([QApplication.translate('HelpDlg','Click on Home Icon\nWhile recording only'),QApplication.translate('HelpDlg','Navigation Toolbar'),QApplication.translate('HelpDlg','Toggle Zoom Follow (automatic panning)'),QApplication.translate('HelpDlg','Zoom action while recording sets Follow ON')])
    strlist.append(tbl_AddlShortcuts.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('<br/><br/><b>')
    strlist.append(QApplication.translate('HelpDlg','MENU SHORTCUTS'))
    strlist.append('</b>')
    tbl_MenuShortcuts = prettytable.PrettyTable()
    tbl_MenuShortcuts.field_names = [QApplication.translate('HelpDlg','Keys'),QApplication.translate('HelpDlg','Menu'),QApplication.translate('HelpDlg','Action')]
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+O [Mac]\nCTRL+O [Win]'),QApplication.translate('HelpDlg','File'),QApplication.translate('HelpDlg','Open')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+S [Mac]\nCTRL+S [Win]'),QApplication.translate('HelpDlg','File'),QApplication.translate('HelpDlg','Save')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+P [Mac]\nCTRL+P [Win]'),QApplication.translate('HelpDlg','File'),QApplication.translate('HelpDlg','Print')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+X [Mac]\nCTRL+X [Win]'),QApplication.translate('HelpDlg','Edit'),QApplication.translate('HelpDlg','Cut')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+C [Mac]\nCTRL+C [Win]'),QApplication.translate('HelpDlg','Edit'),QApplication.translate('HelpDlg','Copy')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+V [Mac]\nCTRL+V [Win]'),QApplication.translate('HelpDlg','Edit'),QApplication.translate('HelpDlg','Paste')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+T [Mac]\nCTRL+T [Win]'),QApplication.translate('HelpDlg','Roast'),QApplication.translate('HelpDlg','Open Roast Properties dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+B [Mac]\nCTRL+B [Win]'),QApplication.translate('HelpDlg','Roast'),QApplication.translate('HelpDlg','Open Profile Background dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+F4 [Mac]\nCTRL+F4 [Win]'),QApplication.translate('HelpDlg','Roast'),QApplication.translate('HelpDlg','Switch Profiles (Foreground<=>Background)')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+D [Mac]\nCTRL+D [Win]'),QApplication.translate('HelpDlg','Config'),QApplication.translate('HelpDlg','Open Devices dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+U [Mac]\nCTRL+U [Win]'),QApplication.translate('HelpDlg','Config'),QApplication.translate('HelpDlg','Open Curves dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+E [Mac]\nCTRL+E [Win]'),QApplication.translate('HelpDlg','Config'),QApplication.translate('HelpDlg','Open Events dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+A [Mac]\nCTRL+A [Win]'),QApplication.translate('HelpDlg','Config'),QApplication.translate('HelpDlg','Open Alarms dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+SHIFT+A [Mac]\nCTRL+SHIFT+A [Win]'),QApplication.translate('HelpDlg','Config'),QApplication.translate('HelpDlg','Open Axes dialog')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+K [Mac]\nCTRL+K [Win]'),QApplication.translate('HelpDlg','Tools'),QApplication.translate('HelpDlg','Analyzer Auto All')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+OPTION+A [Mac]\nCTRL+ALT+K [Win]'),QApplication.translate('HelpDlg','Tools'),QApplication.translate('HelpDlg','Analyzer Clear Results')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+L [Mac]\nCTRL+L [Win]'),QApplication.translate('HelpDlg','View'),QApplication.translate('HelpDlg','Show/Hide Large Main LCDs')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','⌘+F [Mac]\nCTRL+SHIFT+F [Win]'),QApplication.translate('HelpDlg','View'),QApplication.translate('HelpDlg','Toggle Full Screen Mode \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 \u00A0\u00A0\u00A0\u00A0\u00A0 ')])
    tbl_MenuShortcuts.add_row([QApplication.translate('HelpDlg','F1'),QApplication.translate('HelpDlg','Help'),QApplication.translate('HelpDlg','Open QuickStart Guide in the system browser')])
    strlist.append(tbl_MenuShortcuts.get_html_string(attributes={'width':'100%','border':'1','padding':'1','border-collapse':'collapse'}))
    strlist.append('</body>')
    helpstr = ''.join(strlist)
    return re.sub(r'&amp;', r'&',helpstr)
