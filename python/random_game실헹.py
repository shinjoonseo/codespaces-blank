from random_game import *

play = random_game()
print("어떤 복불복 게임을 할까요?")
while 1 < 2 : 
  play_choice = input("1. 제비뽑기\n2. 룰렛\n")
  if play_choice.isdigit() == False :
    print("메뉴에서 선택해 주세요.")
    continue
  if int(play_choice) == 1 :
    play.제비뽑기()
    break
  elif int(play_choice) == 2 :
    play.룰렛()
    break
  else :
    print("메뉴에서 선택해 주세요.")
    continue