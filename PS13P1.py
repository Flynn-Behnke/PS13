class employee:
  def __init__(self, first, last, pay, brate):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = (first + '.' + last + '@company.com')
    self.brate = brate

  def bonus(self):
    bonus = float(self.pay)*float(self.brate)
    return bonus
  def fullname(self):
    return '{} {}'.format(self.first, self.last)


emp_1 = employee('John', 'Smith', 75000, 0.1)
emp_2 = employee('Steven', 'Johnson', 65000, 0.07)

print(emp_1.fullname(), 'bonus:', emp_1.bonus())
