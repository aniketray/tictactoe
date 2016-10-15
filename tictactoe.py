# Board itself, keeps track of the board state.
import copy

class TicTacToe(object):
  def __init__(self, w, h):
    self.h = h
    self.w = w
    self._positions = [[0 for x in range(w)] for y in range(h)]
    self._terminated = False
    self._place_count = 0
    self._winner = 0
    self._progress = []

  def PrintBoard(self):
    self.PrintBoardState(self._positions)

  def PrintBoardState(self, positions):
    for idx, positions in enumerate(positions):
      formatted_positions = []
      for x in positions:
        if x == 1:
          formatted_positions.append('x')
        elif x == 2:
          formatted_positions.append('o')
        else:
          formatted_positions.append(' ')
      print '|'.join(formatted_positions)
      if idx != self.h - 1:
        print '- - -'
    print '___________________'

  def PrintGame(self):
    for positions in self._progress:
      self.PrintBoardState(positions)
      print ''

  def Terminated(self):
    return self._terminated

  def Winner(self):
    return self._winner
    
  def CurrentBoard(self):
    return copy.deepcopy(self._positions)

  def PlaceTurn(self, player_id, position):
    if self._positions[position[0]][position[1]] != 0:
      return False
    self._positions[position[0]][position[1]] = player_id
    win_state = self._CheckWinState()
    assert win_state is not None
    if win_state != 0:
      self._terminated = True
      self._winner = win_state
    self._place_count+=1
    if self._place_count == 9:
      self._terminated = True
    self._progress.append(copy.deepcopy(self._positions))
    return True

  def _CheckWinState(self):
    for row in self._positions:
      t = set(row)
      if len(t) == 1 and row[0] != 0:
        return row[0]
    for i in range(self.w):
      col = []
      for row in self._positions:
        col.append(row[i])
      t = set(col)
      if len(t) == 1 and col[0] != 0:
        return col[0]
    if (self._positions[0][0] ==
       self._positions[1][1] and
       self._positions[1][1] ==
       self._positions[2][2] and
       self._positions[1][1] != 0):
      return self._positions[1][1]
    if (self._positions[2][0] ==
       self._positions[1][1] and
       self._positions[1][1] ==
       self._positions[0][2] and
       self._positions[1][1] != 0):
      return self._positions[1][1]
    return 0

