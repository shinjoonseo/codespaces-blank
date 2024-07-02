from random import *
from tkinter import *
from PIL import ImageTk, Image


#스테이지 설정 클레스
class game :
  #처음 스테이지 설정(스테이지, 스테이지개수, 주사위최대값)으로 받는 값
  def __init__(self, stage, scount, limit, monster, bossmonster, status, experience, items, items_dic, coin, monster_img, bossmonster_img) :
    #리턴 받아야 하는 값{
    self.status = status
    self.experience = experience
    self.items = items
    self.items_dic = items_dic
    self.coin = coin   #}
    self.item = {11:["(일반)체력이 1 증가합니다.",1,1], 12:["(일반)공격력이 1 증가합니다.",1,2], 13:["(일반)방어력이 1 증가합니다.",1,3], 14:["(일반)민첩이 1 증가합니다.",1,4], 15:["(일반)명중률이 1 증가합니다.",1,5], 16:["(일반)행운이 1 증가합니다.",1,6],
                  21:["(희귀)체력이 2 증가합니다.",2,1], 22:["(희귀)공격력이 2 증가합니다.",2,2], 23:["(희귀)방어력이 2 증가합니다.",2,3], 24:["(희귀)민첩이 2 증가합니다.",2,4], 25:["(희귀)명중률이 2 증가합니다.",2,5], 26:["(희귀)행운이 2 증가합니다.",2,6],
                  31:["(영웅)체력이 3 증가합니다.",3,1], 32:["(영웅)공격력이 3 증가합니다.",2,2], 33:["(영웅)방어력이 3 증가합니다.",3,3], 34:["(영웅)민첩이 3 증가합니다.",3,4], 35:["(영웅)명중률이 3 증가합니다.",3,5], 36:["(영웅)행운이 3 증가합니다.",3,6],
                  41:["(전설)체력이 4 증가합니다.",4,1], 42:["(전설)공격력이 4 증가합니다.",2,2], 43:["(전설)방어력이 4 증가합니다.",4,3], 44:["(전설)민첩이 4 증가합니다.",4,4], 45:["(전설)명중률이 4 증가합니다.",4,5], 46:["(전설)행운이 4 증가합니다.",4,6]}
    #일반몬스터, 보스몬스터 이미지 상대경로 문자열{
    self.monster_img = monster_img
    self.bossmonster_img = bossmonster_img #}
    self.stage = stage
    self.scount = scount
    self.limit = limit
    self.monster = monster
    self.bossmonster = bossmonster
    self.monster_hp = int(100 + (100 * (stage*0.14)))
    self.monster_atk =  int(22 + (15 * (stage*0.15)))
    self.Hp = self.status['체력'] * 80
    print(self.status)
    print(f"\n{self.stage}스테이지로 진입합니다.")
  
  #레벨업 함수
  def LvUp(self) :
    while 1 > 0 :
      lvup = input("레벨이 올랐습니다. 올리고 싶은 스테이터스를 고르세요.\n1. 체력\n2. 공격력\n3. 방어력\n4. 민첩\n5. 명중률\n6. 행운\n")
      if lvup.isdigit() == False :   
        print("메뉴에서 골라주세요.")
        continue
      lvup = int(lvup)
      if lvup == 1 :
        self.status['체력'] += 1
        self.Hp += 80
        print("\n체력이 1 올랐습니다.")
      elif lvup == 2 :
        self.status['공격력'] += 1
        print("\n공격력이 1 올랐습니다.")          
      elif lvup == 3 :
        self.status['방어력'] += 1
        print("\n방어력이 1 올랐습니다.")         
      elif lvup == 4 :
        self.status['민첩'] += 1
        print("\n민첩이 1 올랐습니다.")         
      elif lvup == 5 :
        self.status['명중률'] += 1
        print("\n명중률이 1 올랐습니다.")         
      elif lvup == 6 :
        self.status['행운'] += 1
        print("\n행운이 1 올랐습니다.")
      else :
        print("메뉴에서 골라주세요.")
        continue
      print(f"최대HP:{self.status['체력'] * 80}/현재HP:{self.Hp}")         
      print(f"\n현재 능력치\n체력: {self.status['체력']}\n공격력: {self.status['공격력']}\n방어력: {self.status['방어력']}\n민첩: {self.status['민첩']}\n명중률: {self.status['명중률']}\n행운: {self.status['행운']}")
      input("다음 스테이지로 넘어갑니다.")
      break
    

  #플레이어 회피 함수
  def evasion(self) :
    num = choice(range(self.limit-9, self.limit+1))
    print(f"\n주사위 숫자: \'{num}\'\n")
    if num <= self.status['민첩'] :
      input(f"{self.monster}의 공격을 피했습니다.")
    elif num > self.status['민첩'] :
      print(f"{self.monster}의 공격을 맞았습니다.")
      self.Hp = self.Hp - (self.monster_atk - (self.status['방어력']*2))
      input(f"나의 HP가 \'{self.Hp}\'남았습니다.")

  #공격 함수
  def attack(self, monster_hp) :
    num = choice(range(1, self.limit+1))
    print(f"\n주사위 숫자: \'{num}\'\n")
    #공격 성공
    if num <= self.status['명중률'] :
      print("공격을 성공했습니다.")
      monster_hp = monster_hp - (self.status['공격력']*5)
      if monster_hp > 0 :
        print(f"{self.monster}의 HP가 \'{monster_hp}\'남았습니다.\n")
      else :
        print(f"{self.monster}이(가) 죽었습니다.\n")
        return monster_hp
      #몬스터 공격회피
      input(f"이번에는 {self.monster}이(가) 공격합니다.")
      game.evasion(self)
      return monster_hp
    #공격 실패
    elif num > self.status['명중률'] :
      print("공격을 실패했습니다.")
      input(f"이번에는 {self.monster}이(가) 공격합니다.")
      #몬스터 공격회피
      game.evasion(self)
      return monster_hp

  #도망 함수
  def run(self) : 
    num = choice(range(self.limit-9, self.limit+1))
    print(f"\n주사위 숫자: \'{num}\'\n")
    if num <= self.status['민첩'] :
      print("도망을 성공했습니다.\n경험치를 1얻습니다.")
      self.experience += 1
      if self.experience >= 4 :
        game.LvUp(self)
        self.experience -= 4
      else :
        input("다음 스테이지로 넘어갑니다.")
      return 1
    else :
      print("도망을 실패해 공격에 맞습니다.")
      self.Hp = self.Hp - (self.monster_atk - (self.status['방어력']*2))
      input(f"나의 HP가 \'{self.Hp}\'남았습니다.\n")
      return 2

  #체력회복 함수
  def Healing(self) :
    Probability = choice(range(self.status['행운'] , 41))
    #일반등급일때 Hp 50 회복
    if Probability <= 20 :
      self.Hp = self.Hp + 50
      print(f"\n\'일반\'등급이 나왔습니다. HP를 50회복 시켜 현재 HP는 \'{self.Hp}\'입니다.\n")
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80 
        print(f"\n\'일반\'등급이 나왔습니다. HP를 50회복 시켜 현재 HP는 \'{self.Hp}\'입니다.\n")
    elif Probability <= 32 :
      self.Hp = self.Hp + 80
      print(f"\n\'희귀\'등급이 나왔습니다. HP를 80회복 시켜 현재 HP는 \'{self.Hp}\'입니다.\n")
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80 
        print(f"\n\'희귀\'등급이 나왔습니다. HP를 80회복 시켜 현재 HP는 \'{self.Hp}\'입니다.\n")
    elif Probability <= 38 :
      self.Hp = self.Hp + 150
      print(f"\n\'영웅\'등급이 나왔습니다. HP를 150회복 시켜 현재 HP는 \'{self.Hp}\'입니다.\n")
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80 
        print(f"\n\'영웅\'등급이 나왔습니다. HP를 150회복 시켜 현재 HP \'{self.Hp}\'입니다.\n")
    else :
      self.Hp = self.status['체력'] * 80
      print(f"\n\'전설\'등급이 나왔습니다. HP를 전부회복 시켜 현재 HP \'{self.Hp}\'입니다.\n")
    print(f"최대HP:{self.status['체력'] * 80}/현재HP:{self.Hp}")

  #아이템뽑기 함수
  def Picking_items(self) :   
    Probability = choice(range(self.status['행운'] , 41))
    if Probability <= 20 :
      rarity10 = 1
    elif Probability <= 32 :
      rarity10 = 2
    elif Probability <= 38 :
      rarity10 = 3
    else :
      rarity10 = 4
    rarity1 = choice(range(1,7))
    rarity = int((rarity10*10) + (rarity1))
    item = {rarity:self.item[rarity]}
    while 0<1 :
      print(f"나온 아이템은 \"{self.item[rarity][0]}\"")
      print(self.items)
      slot = input("1, 2, 3, 4번중 어디다가 장착할지 입력해 주세요.\n나온 아이템을 버리실거면 5를 입력해주세요.")
      if slot.isdigit() == False :
        print("메뉴에서 골라주세요.")
        continue
      slot = int(slot)
      if slot > 5 :
        continue
      elif slot == 5 :
        break
      items_dic_key = list(self.items_dic[slot-1].keys())
      #능력치 다운
      if self.items_dic[slot-1][items_dic_key[0]][2] == 1 :
        self.status['체력'] -= self.items_dic[slot-1][items_dic_key[0]][1]
        if self.status['체력'] * 80 < self.Hp :
          self.Hp = self.status['체력'] * 80
      if self.items_dic[slot-1][items_dic_key[0]][2] == 2 :
        self.status['공격력'] -= self.items_dic[slot-1][items_dic_key[0]][1]
      if self.items_dic[slot-1][items_dic_key[0]][2] == 3 :
        self.status['방어력'] -= self.items_dic[slot-1][items_dic_key[0]][1]
      if self.items_dic[slot-1][items_dic_key[0]][2] == 4 :
        self.status['민첩'] -= self.items_dic[slot-1][items_dic_key[0]][1]
      if self.items_dic[slot-1][items_dic_key[0]][2] == 5 :
        self.status['명중률'] -= self.items_dic[slot-1][items_dic_key[0]][1]
      if self.items_dic[slot-1][items_dic_key[0]][2] == 6 :
        self.status['행운']  -= self.items_dic[slot-1][items_dic_key[0]][1]
      #능력치 업
      if self.item[rarity][2] == 1 :
        self.status['체력'] += self.item[rarity][1]
        self.Hp += self.item[rarity][1]*80
      if self.item[rarity][2] == 2 :
        self.status['공격력'] += self.item[rarity][1]
      if self.item[rarity][2] == 3 :
        self.status['방어력'] += self.item[rarity][1]
      if self.item[rarity][2] == 4 :
        self.status['민첩'] += self.item[rarity][1]
      if self.item[rarity][2] == 5 :
        self.status['명중률'] += self.item[rarity][1]
      if self.item[rarity][2] == 6 :
        self.status['행운']  += self.item[rarity][1]
      self.items[slot] = self.item[rarity][0]
      self.items_dic[slot-1] = item
      print(f"장착 아이템 {self.items}")
      print(f"최대HP:{self.status['체력'] * 80}/현재HP:{self.Hp}")
      input(f"\n현재 능력치\n체력: {self.status['체력']}\n공격력: {self.status['공격력']}\n방어력: {self.status['방어력']}\n민첩: {self.status['민첩']}\n명중률: {self.status['명중률']}\n행운: {self.status['행운'] }")
      break

  #보너스(랜덤뽑기) 함수
  def bonus(self) :
    input("\n이번 스테이지는 보스를 만나기 전 보너스 스테이지입니다.\n\'행운\'에 따라 보너스가 달라집니다.")
    Probability = choice(range(self.status['행운'] , 41))
    #일반등급일때 Hp 30 회복
    if Probability <= 20 :
      self.Hp = self.Hp + 30
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80
      print(f"\n\'일반\'등급이 나왔습니다. Hp를 30회복 시켜 현재 HP은 \'{self.Hp}\'입니다.\n")
    #희귀등급일때 능력치 1 증가
    elif Probability <= 32 :
      print("\n\'희귀\'등급이 나왔습니다.")
      up = choice(range(1,7))
      if up == 1 :
        self.status['체력'] += 1
        self.Hp = self.Hp + 80
        input("체력이 1 올랐습니다. 최대HP와 현재HP가 100 올랐습니다.\n")
      if up == 2 :
        self.status['공격력'] += 1
        input("공격력이 1 올랐습니다.\n")
      if up == 3 :
        self.status['방어력'] += 1
        input("방어력이 1 올랐습니다.\n")
      if up == 4 :
        self.status['민첩'] += 1
        input("민첩이 1 올랐습니다.\n")
      if up == 5 :
        self.status['명중률'] += 1
        input("명중률이 1 올랐습니다.\n")
      if up == 6 :
        self.status['행운']  += 1
        input("행운이 1 올랐습니다.\n")
    #영웅등급일때 Hp 50 회복 능력치 1 증가
    elif Probability <= 38 :
      self.Hp = self.Hp + 50
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80
      print(f"\n\'영웅\'등급이 나왔습니다. Hp를 50회복 시켜 현재 체력은 \'{self.Hp}\'입니다.")
      up = choice(range(1,7))
      if up == 1 :
        self.status['체력'] += 1
        self.Hp = self.Hp + 80
        input("체력이 1 올랐습니다. 최대HP와 현재HP가 100 올랐습니다.\n")
      if up == 2 :
        self.status['공격력'] += 1
        input("공격력이 1 올랐습니다.\n")
      if up == 3 :
        self.status['방어력'] += 1
        input("방어력이 1 올랐습니다.\n")
      if up == 4 :
        self.status['민첩'] += 1
        input("민첩이 1 올랐습니다.\n")
      if up == 5 :
        self.status['명중률'] += 1
        input("명중률이 1 올랐습니다.\n")
      if up == 6 :
        self.status['행운']  += 1
        input("행운이 1 올랐습니다.\n")
    #전설등급일때 Hp 50 회복 능력치 2 증가
    else :
      self.Hp = self.Hp + 50
      if self.Hp > self.status['체력'] * 80 :
        self.Hp = self.status['체력'] * 80
      print(f"\n\'전설\'등급이 나왔습니다. Hp를 50회복 시켜 현재 체력은 \'{self.Hp}\'입니다.")
      up = choice(range(1,7))
      if up == 1 :
        self.status['체력'] += 2
        self.Hp = self.Hp + 160
        input("체력이 2 올랐습니다. 최대HP와 현재HP가 200 올랐습니다.\n")
      if up == 2 :
        self.status['공격력'] += 2
        input("공격력이 2 올랐습니다.\n")
      if up == 3 :
        self.status['방어력'] += 2
        input("방어력이 2 올랐습니다.\n")
      if up == 4 :
        self.status['민첩'] += 2
        input("민첩이 2 올랐습니다.\n")
      if up == 5 :
        self.status['명중률'] += 2
        input("명중률이 2 올랐습니다.\n")
      if up == 6 :
        self.status['행운']  += 2
        input("행운이 2 올랐습니다.\n")
    print(f"최대HP:{self.status['체력'] * 80}/현재HP:{self.Hp}")
    input(f"\n현재 능력치\n체력: {self.status['체력']}\n공격력: {self.status['공격력']}\n방어력: {self.status['방어력']}\n민첩: {self.status['민첩']}\n명중률: {self.status['명중률']}\n행운: {self.status['행운'] }")

  # MyPage Functions
  def set_title_lable(self, text, color):
      label = Label(self.win,
                    text=text,
                    bg=color,
                    width=15,
                    height=1)
      label.pack(anchor="w", padx=10, pady=8)

  def set_lable(self, text, color):
      label = Label(self.win,
                    text=text,
                    bg=color,
                    width=12,
                    height=1)
      label.pack(anchor="w", padx=10, pady=5)

  def show_stats(self, dic, coin):
      self.set_title_lable("나의 능력치", "yellow")
      self.set_lable(f"최대 HP : {self.status['체력'] * 80}", "lightblue")
      self.set_lable(f"현재 HP : {self.Hp}", "lightblue")

      for key, value in dic.items():
          self.set_lable(f"{key} : {value}", "lightblue")

      self.set_title_lable("보유 코인", "yellow")
      self.set_lable(f"코인 : {coin}", "lightblue")

  def myPage_main(self):
      self.win = Tk()
      self.win.geometry("800x600")
      self.win.title("My Page")
      self.win.option_add("*Font", "맑은고딕 20")

      path = Image.open("img\배경3.png")
      resize_img = path.resize((800, 600))
      img = ImageTk.PhotoImage(resize_img)
      bg_image = Label(self.win, image=img)
      bg_image.place(x=0, y=0, anchor="nw")

      label = Label(self.win, text="My Page", bg="beige")
      label.pack(ipadx=15, ipady=15)

      self.show_stats(self.status, self.coin)
      self.win.mainloop()


  #스테이지 시작함수
  def stage_start(self) :

    # 마이페이지 GUI 호출
    self.myPage_main()

    for i in range(1, self.scount + 1) :
      print(f"\n스테이지{self.stage} - {i}")
      monster_hp = self.monster_hp 

      #보스 몬스터와 전투
      if i == self.scount :
        bossmonster_hp = monster_hp * 5
        self.monster = self.bossmonster
        self.monster_atk = int(self.monster_atk * 1.4)
        print(f"이번 몬스터는 강력한 {self.bossmonster}입니다.\n이 스테이지는 도망이 불가능합니다.")
        while True :
          if self.Hp < 0 :
            input(f"당신은 스테이지{self.stage} - {i} 에서 죽었습니다.")
            print("GAEM OVER")
            exit()
          if bossmonster_hp <= 0 :
            print(f"{self.bossmonster}를(을) 처치했습니다.\n경험치6과 코인200원을 얻었습니다.")
            self.coin += 200
            game.LvUp(self)
            break
          select = input("\n행동을 골라주세요.\n1. 공격\n")
          if select.isdigit() == False : 
            print("메뉴에서 골라주세요.")
            continue
          select = int(select)          
          if select > 1 :
            print("메뉴에서 골라주세요.")
            continue
          bossmonster_hp = game.attack(self, bossmonster_hp)
          continue

      #일반 몬스터와 전투
      elif i < self.scount - 1 :
        print(f"{self.monster}이(가) 나타났습니다.")
        while True :
          if self.Hp < 0 :
            input(f"당신은 스테이지{self.stage} - {i} 에서 죽었습니다.")
            print("GAEM OVER")
            exit()
          if monster_hp <= 0 :
            print(f"{self.monster}를(을) 처치했습니다.\n경험치2와 코인100원을 얻었습니다.")
            print(f"최대HP:{self.status['체력'] * 80}/현재HP:{self.Hp}")
            self.coin += 100
            self.experience += 2
            if self.experience >= 6 :
              game.LvUp(self)
              self.experience -= 6
            else :
              input("다음 스테이지로 넘어갑니다.")
            break
          select = input("\n행동을 골라주세요.\n1. 공격\n2. 도망\n")
          if select.isdigit() == False :
            print("메뉴에서 골라주세요.")
            continue
          select = int(select)
          if select == 1 :
            monster_hp = game.attack(self, monster_hp)
            continue
          elif select == 2 :
            run = game.run(self)
            if run == 1 :
              break
            continue
          print("메뉴에서 골라주세요.")
          continue

      #상점
      else :
        print("보스를 잡기전 상점 스테이지 입니다.")
        x = 0
        while True :
          print(f"\n보유코인 {self.coin}원")
          market_choice = input("뽑기 등급은 (일반, 희귀, 영웅, 전설)이 있습니다.n\'행운\'에 따라 확률이 달라집니다.)\n1. 체력회복뽑기 100원\n2. 아이템뽑기 300원\n3. 랜덤뽑기 0원(처음 1번만가능, 선택시 뽑기 후 다음스테이지로 넘어갑니다.)\n4. 상점 나가기\n")
          if market_choice.isdigit() == False :
            print("메뉴에서 골라주세요.")
            continue
          market_choice = int(market_choice)
          if market_choice == 1 :
            if self.coin >= 100 :
              game.Healing(self)
              self.coin -= 100
              x += 1
            else :
              input("코인이 부족합니다.")
          elif market_choice == 2 :
            if self.coin >= 300 :
              game.Picking_items(self)
              self.coin -= 300
              x += 1
            else :
              input("코인이 부족합니다.")
          elif market_choice == 3 :
            if x == 0 :
              game.bonus(self)
              break
            else :
              input("랜덤뽑기는 상점입장한 처음만 가능합니다.")
          elif market_choice == 4 :
            break
    return self.status, self.experience, self.items, self.items_dic, self.coin
