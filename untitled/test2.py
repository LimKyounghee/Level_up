from pywinauto.application import Application
from pywinauto.timings import timestamp
from pywinauto import keyboard

app = Application(backend="uia").start(r'C:/Program Files (x86)/Kakao/KakaoTalk/KakaoTalk.exe')
app.window(title_re='카카오톡').wait('ready',timeout=20)
# print(app.window(title_re='카카오톡').dump_tree)
print(app.window(title_re='카카오톡').dump_tree())
app.window(title_re='카카오톡').child_window(auto_id="1061", control_type="Edit").type_keys("ghkdth123")
dlg = app.window(title_re='카카오톡')
keyboard.send_keys('{ENTER}')
# app.window(title_re='카카오톡').child_window(auto_id="132").wait('ready',timeout=10)
# #TAB 8 , 아래
# for i in range(0,8):
#     keyboard.send_keys('{TAB}')
# keyboard.send_keys('{DOWN}')
# keyboard.send_keys('{TAB}')
# for i in range(0,1):
#     keyboard.send_keys('{DOWN}')
# keyboard.send_keys('{ENTER}')
# keyboard.send_keys('임경희 바보')
# keyboard.send_keys('{ENTER}')