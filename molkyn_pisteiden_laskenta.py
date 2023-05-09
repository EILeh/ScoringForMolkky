"""
Scoring for Mölkky

Mölkky is a traditional Finnish game where players aim to score exactly 50
points. If a player ends up having more than 50 points, his/her score will be
decreased to 25 points. The program will help us with scoring a game of Mölkky
when there are two players playing. The main program is defined with two Player
type objects and calls the methods get_name, get_points, has_won, and add_points
to them. In the main function the variables player1 ja player2 are the names
given to these two objects. Those names persistently refer to the same objects.
Variable in_turn, on the other hand, switches referring between these two
objects depending on whose turn it is (i.e. whether the value of the variable
throw is even or odd). The class Player contains all the data used to represent
one player. The class has an interface the main program uses to manipulate
Player objects. A warning message is printed immediately after the new points
are entered if the total score of the player is 40 ≤ total score ≤ 49. NAME
has been replaced by the name of the player whose turn it is and X has been
replaced by the point amount the player is missing from winning score of 50
points. A supporting feedback printout "Cheers NAME!" in the program. It will be
printed immediately after the new points are entered if the entered point score
is larger than the average of the all the points entered for that player. Name
will again be replaced by the name of the player for whom the points belong.

For example, if on the first round Matti scored 10 points and on the second
round he scores 11 points, then the cheer will be printed after the second score
(11) is entered. At the end of the line of the scoreboard printout a success
percentage for the player. The success percentage in this context means the
amount of scores entered which resulted at least one point (i.e. the player
didn't fail his/her turn completely). The percentage should be printed with the
accuracy of one decimal.

Writer of the program: EILeh

"""

class Player:
    """
    Class Player: Implements a player and his/hers name, points, penalties,
    hit percentage and if they are a winner or not.
    """

    def __init__(self, player_name, points = 0, points_added = 0,
                 count_throws = 0, hit = 0):
        """
        Constructor, initializes the newly created object.
        :param player_name: str, player's name
        :param points: int, player's points at the moment
        :param points_added: int, player's points at current round
        :param count_throws: int, the amount of times player has thrown
        :param hit: float, counts points so the percentage can be taken
        """

        # player's name
        self.__name = player_name

        # adds points for player
        self.__points_atm = points

        # counts the amount of throws
        self.__throws = []

        # the points that players throw
        self.__add_points = points_added

        # the percentage of player's hits and misses
        self.__percentage = hit

        # point list to check if player hit or missed
        self.__hits = []

        # checks if player gets penalty or not
        self.__penalty = False



    def get_name(self):
        """
        Player's name.
        :return: str, player's name
        """
        return self.__name


    def get_points(self):
        """
        Player's total point at the moment.
        :return: int, player's total points at the moment
        """
        return self.__points_atm


    def add_points(self, points_added):
        """
        Updates player's score after a throw.
        :param points_added: int, the points that are added to the total
        points
        :return: int, updated value of player's points after current throw
        """
        self.__add_points = points_added

        if ((self.__points_atm + self.__add_points) >= 40) and \
                ((self.__points_atm + self.__add_points) <= 49):

            points_left = (50 - (self.__add_points + self.__points_atm))
            print(f"{self.__name} needs only {points_left} points. "
                  f"It's better to avoid knocking down the pins with "
                  f"higher points.")


        if (points_added + self.__points_atm) > 50:

            self.__points_atm = 25
            self.__hits.append(points_added)
            print(f"{self.__name} gets penalty points!")
            self.__penalty = True

            return self.__points_atm


        if (points_added + self.__points_atm) <= 50:

            self.__points_atm = points_added + self.__points_atm
            self.__hits.append(points_added)

            return self.__points_atm


    def has_won(self):
        """
        Checks if the player has exactly 50 points. If so, player has won.
        Also checks if the last throw's value is higher than average.
        :return: true, if player has 50 points
        """
        if self.__points_atm == 50:

            if self.__add_points > (self.__points_atm / (len(self.__throws))):

                print(f"Cheers {self.__name}!")

            return True


    def average(self):
        """
        Counts the average value of the throws that the player has gotten,
        counts average among them and compares it to current throw. If current
        throw is higher that average, player gets compliments.
        """
        throw = 1
        throw += 1

        amount_of_throws = self.__throws.append(throw)
        average = (self.__points_atm / (len(self.__throws)))

        if self.__add_points < 51:

            if self.__add_points > average and self.__penalty is False:

                print(f"Cheers {self.__name}!")
                self.__penalty = False


    def hit_percentage(self):
        """
        Counts the percentage that players hits something. It doesn't matter
        what the points are, as long as player's hits at least one target.
        :return: float, the percentage that the player hits target
        """
        throws_that_hit = 0
        total_hits = len(self.__hits)

        for value in self.__hits:

            if value >= 1:

                throws_that_hit += 1

        if total_hits >= 1:

            self.__percentage = (throws_that_hit / total_hits) * 100

        return self.__percentage


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1

    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        in_turn.average()

        if in_turn.has_won():

            print("Game over! The winner is " + in_turn.get_name() + "!")

            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(),
              "p, hit percentage", float(round(player1.hit_percentage(), 1)))
        print(player2.get_name() + ":", player2.get_points(),
              "p, hit percentage", float(round(player2.hit_percentage(), 1)))
        print("")

        throw += 1

if __name__ == "__main__":
    main()