# from pyuac import isUserAdmin, runAsAdmin

# if not isUserAdmin():
#        runAsAdmin()

from pywinauto import Desktop, Application

app = Application(backend="win32").start(r'C:\\WINDOWS\\system32\\SnippingTool.exe')
app.UntitledNotepad.type_keys("%FX")

# app = Application(backend="win32").start('SnippingTool.exe')
# dlg = Desktop(backend="uia").Snipping_Tool
# dlg.print_control_identifiers()
# Application().start('explorer.exe "C:\\Program Files"')

# # connect to another process spawned by explorer.exe
# # Note: make sure the script is running as Administrator!
# app = Application(backend="uia").connect(path="explorer.exe", title="Program Files")

# app.ProgramFiles.set_focus()
# common_files = app.ProgramFiles.ItemsView.get_item('Common Files')
# common_files.right_click_input()
# app.ContextMenu.Properties.invoke()

# # this dialog is open in another process (Desktop object doesn't rely on any process id)
# Properties = Desktop(backend='uia').Common_Files_Properties
# Properties.print_control_identifiers()
# Properties.Cancel.click()
# Properties.wait_not('visible') # make sure the dialog is closed