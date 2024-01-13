import pyautogui 

Btn_1=pyautogui.alert("경고","Title","clear")
# print(Btn_1)
# print(type(Btn_1))

# Btn_2=pyautogui.confirm("Test")
# print(Btn_2)
# print(type(Btn_2))

# if Btn_2 =='ok':

#     print("ok입니다.")

Btn_2=pyautogui.prompt(title="Test", default='여기에 쓰세요',test='텍스트')