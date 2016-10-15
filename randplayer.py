import random

class Player(object):
  def Inform(self, player_id, winner):
    pass

  def GetMove(self, positions, size):
    count = 0
    for rows in positions:
      for j in rows:
        if j == 0:
          count+=1
    chosen = random.randint(0, count - 1)
    for i, rows in enumerate(positions):
      for j, val in enumerate(rows):
        if val == 0:
          if chosen == 0:
            return (i, j)
          chosen -= 1
    assert False
    return (0, 0)

 




