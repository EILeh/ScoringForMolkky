ScoringForMolkky

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
