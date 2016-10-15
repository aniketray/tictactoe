import random

class Player(object):
  def __init__(self):
    self._scores = {}  # map from state, action, score tuples
    self._actions = [] # list of (state, action tuples) 
    self._lose_count = 0
    self._no_winning_move_count = 0

  def PrintState(self):
    print self._scores

  def PrintCounts(self):
    print 'Lose count = %d' % self._lose_count
    print 'No winning count = %d' % self._no_winning_move_count

  def Inform(self, player_id, winner):
    if player_id == (3 - winner):
      delta = -10.0
    elif winner == 0:
      delta = 0.0
      # self._actions = []
      # return
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
      delta = 0.9 * delta
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
    # 0 => choose lossy
    # 1-10 => choose neutral
    # 11-510 => choose winning

    action_map = self._scores[state]
    losers = []
    neutral = []
    winners = []
    for action, score in action_map.iteritems():
      if score > 0:
        winners.append(action)
      elif score < 0:
        losers.append(action)
      else:
        neutral.append(action)

    chosen_one = []
    if bucket == 0:
      chosen_one = losers
      self._lose_count+=1
    elif bucket >=1 and bucket <= 10:
      chosen_one = neutral
    else:
      chosen_one = winners

    if not chosen_one:
      if winners:
        chosen_one = winners
      else:
        self._no_winning_move_count+=1
        action = self._ChooseRandom(positions)
        self._actions.append((state, action))
        return action

    chosen_idx = random.randint(0, len(chosen_one) - 1)
    action = chosen_one[chosen_idx]
    self._actions.append((state, action))
    return action

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

