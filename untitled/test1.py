from pywinauto import application
from pywinauto import timings
from pywinauto import findwindows
import time
import os

# app = application.Application()
# app.start("notepad")
# # timings.wait_until_passes(20, 0.5, lambda: app.window(title=title))
# app.UntitleNotepad.menu_select("도움말(&H)->메모장 정보(&A)")
#
# app.메모장_정보.확인.click()
#
# app.UntitleNotepad.Edit.type_keys("pywinauto Works!", with_spaces=True)

# dlg = app.window(title=title)
#
# dlg.wrapper_object()

# pass_ctrl = dlg.Edit2
# pass_ctrl.SetFocus()
# pass_ctrl.TypeKeys('xxxx') # 로그인 비밀 번호 입력
#
# cert_ctrl = dlg.Edit3
# cert_ctrl.SetFocus()
# cert_ctrl.TypeKeys('yyyy!')
#
# btn_ctrl = dlg.Button0
# btn_ctrl.Click()
# title = "제목없음 - Windows 메모장"
# dlg = t

# -*- coding: utf-8 -*-
from pywinauto.application import Application

# 메모장를 띄운다.
app = Application().start("notepad.exe")

# 메모장에 code를 적는다.
app.UntitledNotepad.Edit.type_keys("print ('test')", with_spaces=True)

# '파일' > '저장' 메뉴 실행
app.UntitledNotepad.menu_select("파일(&F)->저장(&S)")

# 파일 full 경로 입력
app.다른_이름으로_저장.Edit1.set_edit_text("c:\Download\samplecode.py")

# '파일이름' 콤보박스에서 파일 종류 선택
app.다른_이름으로_저장.ComboBox2.select("모든 파일 (*.*)")

# '파일형식' 콤보박스에서 인코딩 선택
app.다른_이름으로_저장.ComboBox3.select("UTF-8")

# 바로 저장 버튼을 누르면 미처 콤보 박스가 안 바뀌어 에러가 나서 1초 시간 줌
import time

time.sleep(1.0)

# 저장 버튼 누름
app.다른_이름으로_저장.Button1.click()