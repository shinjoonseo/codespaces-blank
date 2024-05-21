from random import * 

class Calculation :

  #시작할때 숫자 두개를 받는다.
  def __init__(self, num1, num2) -> int :
    self.num1 = num1
    self.num2 = num2

  #공약수 함수
  def CD(self) :
    if self.num1 > self.num2 :
      num2_CD = [i for i in range(1,self.num2+1) if self.num2 % i == 0]
      num_CD = [i for i in num2_CD if self.num1 % i == 0]
      return num_CD
    if self.num2 > self.num1 :
      num1_CD = [i for i in range(1,self.num1+1) if self.num1 % i == 0]
      num_CD = [i for i in num1_CD if self.num2 % i == 0]
      return num_CD
  #최대공약수 함수
  def GCD(self) :
    GCD_ = Calculation.CD(self)
    return GCD_[len(GCD_) - 1]
  #공배수 함수
  def CM(self) :
    limit = choice(range(4,11))
    LCM_ = Calculation.LCM(self)
    CM_ = [i * LCM_ for i in range(1, limit +1)]
    return CM_
  #최소공배수 함수
  def LCM(self) :
    GCD_ = Calculation.GCD(self)
    return int(GCD_ * (self.num1 / GCD_) * (self.num2 / GCD_))
a = Calculation(12,6)
print(f"공약수는 {a.CD()}입니다.")
print(f"최대공약수는 {a.GCD()}입니다.")
print(f"공배수는 {a.CM()}입니다.")
print(f"최소공배수는 {a.LCM()}입니다.")

b = Calculation(7,9)
print(f"공약수는 {b.CD()}입니다.")
print(f"최대공약수는 {b.GCD()}입니다.")
print(f"공배수는 {b.CM()}입니다.")
print(f"최소공배수는 {b.LCM()}입니다.")