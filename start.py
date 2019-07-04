import os
import __builtin__
import sys
import _winreg as wreg

token = raw_input("Username: ")
if not token:
    token = "faketoken"

try:
    key = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Disney\\Disney Online\\Toontown", 0, wreg.KEY_ALL_ACCESS)
except:
    key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Disney\\Disney Online\\Toontown")

wreg.SetValueEx(key, 'TOONTOWN_PLAYTOKEN', 0, wreg.REG_SZ, str(token))
print wreg.QueryValueEx(key, 'TOONTOWN_PLAYTOKEN')
wreg.SetValueEx(key, 'PROXY_DIRECT_HOSTS', 0, wreg.REG_SZ, "")
wreg.SetValueEx(key, 'PROXY_SERVER', 0, wreg.REG_SZ, "")
wreg.SetValueEx(key, 'TOONTOWN_BLUE', 0, wreg.REG_SZ, str(token))
wreg.SetValueEx(key, 'GAME2_DONE', 0, wreg.REG_DWORD, 1)
wreg.SetValueEx(key, 'INSTALL_DIR', 0, wreg.REG_SZ, "C:\Program Files\Disney\Disney Online\Toontown")
#print wreg.QueryValueEx(key, 'PROXY_SERVER')

os.system('Toontown.exe null http://127.0.0.1/toontown http://127.0.0.1/ http://127.0.0.1/ 0 "-OGL -windowed -allow_hw_midi -show_fps"')
