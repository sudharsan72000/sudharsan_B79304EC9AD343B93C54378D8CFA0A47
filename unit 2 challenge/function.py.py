
 # Define the base class Player
class Player:
     def play(self):
        print("The player is playing cricket.")

 # Defi (class) Batsman Lass Batsman.
class Batsman (Player):
    def play (self):
         print("The batsman is batting.")

class Bowler(Player):
    def play (self):
         print("The bowler is bowling.")

 # Create objects of Batsman and Bowler classes
batsman= Batsman()
bowler=Bowler ()

batsman.play()
bowler.play()