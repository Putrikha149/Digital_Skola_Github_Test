#Tugas 3
def jumlahkan(num_1 : int, num_2 = 10):
  result = num_1 + num_2
  return result
  
Jumlahkan(num_1) #num_1 diinput merupakan integer

#Tugas 4
class Angka : 
  def __init__(self, number: int):
    self.number = number
  def add_new(self, other_num:int):
    new_value = jumlahkan((self.number+other_num), num_2 = 10)
    return new_value
