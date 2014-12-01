__author__ = 'nakayama'

class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.bet = 1000

    def run(self):
        self.greeting()
        print "------------------GAME START------------------"

        while True:
            print "Input number."
            print "1:ROCK 2:PAPER 3:SCISSORS"

            input_data = raw_input('>>> ')

            if input_data == '1':
                print "YOU: ROCK"
                print "COM: PAPER"
                self.lose_sentence()
            elif input_data == '2':
                print "YOU: PAPER"
                print "COM: SCISSORS"
                self.lose_sentence()
            elif input_data == '3':
                print "YOU: SCISSORS"
                print "COM: ROCK"
                self.lose_sentence()
            else:
                break

        print "------------------GAME OVER------------------"

    def greeting(self):
        print "Hello rich man ! Hello " + self.player_name + " !\n"

    def lose_sentence(self):
        print "You are loser. Pay 1,000 yen to Naoki.\n"

if __name__ == '__main__':
    player_name = 'Bevis'

    good_game = Game(player_name)
    good_game.run()