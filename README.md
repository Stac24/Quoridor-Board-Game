# Quoridor-Strategy-Game

GAME RULES:
Quoridor is a two-player strategy board game played on a 9x9 grid. Each player has one pawn and ten fences. 
In general pawns can move up, down, left, or right unless blocked by a fence. However, there are two scenarios which allow for special movement. Firstly, if the two pawns are face-to-face and there is no fence in between them, the current player may jump the other pawn (see image below).

Secondly, if the two pawns are face-to-face and there exists a fence behind the pawn that is to be jumped, the current pawn may move diagonally to land beside the other pawn only if the pawn has no fence on that side(see image below). 

The objective of this game is to get your pawn to the other side of the board. Use your fences wisely to block your opponent from reaching the other side before you do! 

You can learn more about the rules of this game by reading this article: https://cdn.1j1ju.com/medias/fe/36/08-quoridor-rulebook.pdf
Or by watching this youtube video: https://www.youtube.com/watch?v=I3-j6Q6Nk5g
Note that the video is a slightly different implementation. In the version you will play, there are only two players and each fence only covers one     cell.  

HOW TO PLAY:
Ensure that python and pygame are installed on your machine and run main.py.
Once the game is running, the starting player will always be red. 
Moving a pawn: In order to move your pawn, select your pawn by clicking on it and all valid moves will be displayed. Click on any of the valid cells to move to it. 
Placing a fence: In order to place a fence, click on any cell. All valid fence placements will be highlighted in yellow. Use the arrow keys on your keyboard to give your selected cell an up, down, left, or right fence. 
Once there is a winner, there will be a pop-up on the screen to let you know who won! 
