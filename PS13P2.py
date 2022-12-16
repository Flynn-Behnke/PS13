class stu:
  def __init__(self, first, last, dcode, credits):
    self.first = first
    self.last = last
    self.dcode = dcode
    self.credits = credits

  def tuition(self):
    if self.dcode == "I":
      rate = 250.00
    else:
      rate = 500.00
  
    tuit = int(self.credits)*float(rate)
    return tuit

stu1 = stu('John', 'Smith', 'I', 18)

print(stu.tuition(stu1))
