from random import *

class random_game :

  # 제비뽑기 함수
  def 제비뽑기(self) :
    players_num = int(input("플레이할 인원을 입력해 주세요."))
    players = []
    for i in range(players_num) :
      players.append(input(f"플레이어{i+1} 이름을 입력해 주세요."))
    choice_num = int(input("뽑기할 제비개수를 정해 주세요."))
    choice_list = []
    for i in range(choice_num) :
      choice_list.append(input("제비 내용을 입력해주세요."))
    random_choice_list = sample(choice_list,len(players))
    for i in range(players_num) :
      if i % 5 == 0 :
        print()
      print(f"{players[i]} : {random_choice_list[i]}", end = '\t')

  # 룰렛
  def 룰렛(self) :
    choice_num = int(input("룰렛 칸 개수를 입력해 주세요."))
    choice_list = []
    for i in range(choice_num) :
      choice_list.append(input("룰렛 칸 내용을 입력해 주세요."))
    print(f"{choice(choice_list)}가(이) 나왔습니다.")