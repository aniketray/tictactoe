import random

class Player(object):
  def __init__(self):
    self._scores = {}  # map from state, action, score tuples
    self._actions = [] # list of (state, action tuples) 
    self._game_count = 0
    self._non_optimal_count = 0

  def PrintState(self):
    print self._scores

  def PrintCounts(self):
    print 'Non optimal count = %d' % self._non_optimal_count

  def Inform(self, player_id, winner):
    self._game_count+=1
    if player_id == (3 - winner):
      delta = -20.0
    elif winner == 0:
      delta = 0.1
    else:
      delta = 1.9
    assert len(self._actions) <= 5
    for state_action in reversed(self._actions):
      state = state_action[0]
      action = state_action[1]
      if state in self._scores:
        action_map = self._scores[state]
        if action in action_map:
          self._scores[state][action] += delta
        else:
          self._scores[state][action] = delta
      else:
        self._scores[state] = {}
        self._scores[state][action] = delta
      delta = 0.6 * delta
    self._actions = []

  def GetMove(self, positions, size):
    state = 0
    for rows in positions:
      for j in rows:
        state = state*3 + j

    if state not in self._scores:
      action = self._ChooseRandom(positions)
      self._actions.append((state, action))
      return action

    bucket = random.randint(0, 1010)
    # 0-10 => random player
    # 11-1010 => choose best move

    optimal_move = True
    bucket_limit = 10
    # if self._game_count > 1000000:
    #   bucket_limit = 5000000 / self._game_count
    if self._game_count > 1100000:
      bucket_limit = -1
    if bucket >=0 and bucket <= bucket_limit:
      optimal_move = False

    if not optimal_move:
      self._non_optimal_count+=1
      action = self._ChooseRandom(positions)
      self._actions.append((state, action))
      return action

    action_map = self._scores[state]
    best_score = None
    best_action = None
    for action, score in action_map.iteritems():
      if not best_score or score > best_score:
        best_score = score
        best_action = action

    self._actions.append((state, best_action))
    return best_action

  def _ChooseRandom(self, positions):
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

