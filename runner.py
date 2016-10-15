
import tictactoe
import randplayer
import learningplayer
import optimalplayer

_RUN_COUNT = 3000000

def Play(run_count):
  players = {}
  players[1] = randplayer.Player()
  players[2] = optimalplayer.Player()
  wins = {}
  last_wins = {}
  wins[0] = 0
  wins[1] = 0
  wins[2] = 0
  last_wins[0] = 0
  last_wins[1] = 0
  last_wins[2] = 0
  current_turn = 2
  once = False
  for i in range(run_count):
    game = tictactoe.TicTacToe(3, 3)
    while not game.Terminated():
      current_turn = 3 - current_turn
      current_turn_player = players[current_turn]
      while not game.PlaceTurn(current_turn,
          current_turn_player.GetMove(game.CurrentBoard(), (3,3))):
        # keep trying if illegal move
        pass
    for id, player in players.iteritems():
      player.Inform(id, game.Winner()) 

    if i > 2000000 and not once and game.Winner() == 1:
      game.PrintGame()
      once = True

    wins[game.Winner()]+=1
    if i % 100000 == 0:
      print 'After %d games' % (i + 1)
      print 'Draws = %d (d=%d)' % (wins[0], wins[0] - last_wins[0])
      print 'Player 1 wins = %d (d=%d)' % (wins[1], wins[1] - last_wins[1])
      print 'Player 2 wins = %d (d=%d)' % (wins[2], (wins[2] - last_wins[2]))
      players[2].PrintCounts()
      last_wins[0] = wins[0]
      last_wins[1] = wins[1]
      last_wins[2] = wins[2]

  print 'Final Tally:'
  print 'Draws= %d' % wins[0]
  print 'Player 1 wins = %d' % wins[1]
  print 'Player 2 wins = %d' % wins[2]


def main():
  Play(_RUN_COUNT)

if __name__ == "__main__":
  main()
