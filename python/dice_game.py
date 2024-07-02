from game_class import *
from tkinter import *
import time 

# Variables
items = {1:"", 2:"", 3:"", 4:""}
items_dic = [{'A': [9, 9, 9]}, {'b': [9, 9, 9]}, {'c': [9, 9, 9]}, {'a': [9, 9, 9]}]
experience = 0
coin = 0
stats = ['체력', '공격력', '방어력', '민첩', '명중률', '행운']
stats_values = []
status = {}

# Status Functions
def setLabel(alret):
  label = Label(win, text=alret)
  label.pack(pady = 8)

def setEntry():
  entry = Entry(win)
  entry.pack()
  return entry

def status_input():
  input_values = [entry.get() for entry in entries]
  
  if all(value.isdigit() for value in input_values):
    input_values = list(map(int, input_values))
    # input_values의 값을 int형으로 매핑(객체로 리턴) 후 리스트로 변환
    if sum(input_values) > 30 or any(value > 8 for value in input_values):
      # sum() => 값을 합산 시켜 리턴해줌
      # any() => 요소 중 하나라도 True이면 True, 모두 False이면 False 반환
      Status_msg.config(text="규칙에 맞게 다시 입력해 주세요.")
    else:
      stats_values.extend(input_values)
      # extent() => a.extend(b)일때 a에 b를 확장시킴 (a에 없는 b의 요소를 a에 추가)
      time.sleep(1)
      Status_msg.config(text="다음으로 넘어갑니다.")
      win.destroy()
  else:
    Status_msg.config(text="규칙에 맞게 다시 입력해 주세요.")

# Tkinter Status
win = Tk()
win.geometry("800x600")
win.title("Status")
win.option_add("*Font","맑은고딕 15")
label = Label(win, text="\n스테이터스 초기치는 '8'을 넘길 수 없습니다.\n스테이터스 합은 '30'을 넘길 수 없습니다.")
label.pack()

entries = []
for stat in stats:
  setLabel(f"{stat}을 정해 주세요.")
  entries.append(setEntry())

button = Button(win, text="확인", command=status_input)
button.pack(pady= 8)

Status_msg = Label(win)
Status_msg.pack()
win.mainloop()

status = dict(zip(stats, stats_values))


if __name__ == "__main__" :
  stage1 = game(1, 5, 10, "파란 달팽이", "마노", status, experience, items, items_dic, coin, "img\파란달팽이.png", "img\마노.png")
  status, experience, items, items_dic, coin = stage1.stage_start()
  stage2 = game(2, 5, 11, "주황 버섯", "좀비 머쉬맘", status, experience, items, items_dic, coin, "img\주황버섯.png", "img\좀비머쉬맘.png")
  status, experience, items, items_dic, coin = stage2.stage_start()
  stage3 = game(3, 6, 12, "리본 돼지", "식신", status, experience, items, items_dic, coin, "img\리본돼지.png", "img\식신.png")
  status, experience, items, items_dic, coin = stage3.stage_start()
  stage4 = game(4, 6, 13, "스템프", "스템피", status, experience, items, items_dic, coin, "img\스템프.png" ,"img\스템피.png")
  status, experience, items, items_dic, coin = stage4.stage_start()
  stage5 = game(5, 7, 14, "루나 픽시", "파파 픽시", status, experience, items, items_dic, coin, "img\루나픽시.png" ,"img\파파픽시.png")
  status, experience, items, items_dic, coin = stage5.stage_start()
  stage6 = game(6, 7, 15, "페페", "페페 킹", status, experience, items, items_dic, coin, "img\페페.png" ,"img\페페킹.png")
  status, experience, items, items_dic, coin = stage6.stage_start()
  stage7 = game(7, 8, 17, "스톤 골렘", "에이션트 믹스골렘", status, experience, items, items_dic, coin, "img\스톤골렘.png" ,"img\에이션트_믹스골렘.png")
  status, experience, items, items_dic, coin = stage7.stage_start()
  stage8 = game(8, 8, 19, "주니어 발록", "마왕 발록", status, experience, items, items_dic, coin, "img\주니어발록.png" ,"img\마왕발록.png")
  status, experience, items, items_dic, coin = stage8.stage_start()
  stage9 = game(9, 9, 21, "리치", "자쿰", status, experience, items, items_dic, coin, "img\리치.png" ,"img\자쿰.png")
  status, experience, items, items_dic, coin = stage9.stage_start()
  stage10 = game(10, 9, 23, "레드 와이번", "혼테일", status, experience, items, items_dic, coin, "img\레드와이번.png" ,"img\혼테일.png")
  status, experience, items, items_dic, coin = stage10.stage_start()
  print("GAME CLEAR")