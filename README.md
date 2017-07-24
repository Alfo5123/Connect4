# Connect4
Monte Carlo Tree Search Based AI Connect 4 Bot

<p align="center">
  <img src="https://github.com/Alfo5123/Connect4/blob/master/img/game_example.gif" width="350"/>  
</p>

## Getting Started

### About the game

Connect 4 is a two-player game in which the players take turns dropping colored discs from the top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the next available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

It must be noted that this is a solved game (the first player can always win with *right* moves), the purpose of this project is mianly to implement the algorithm and test its performance in a simple game. We encourage users to find those *right* moves!

### The algorithm

Monte Carlo Tree Search is a recently proposed search method that combines the precision of tree search with the
generality of random sampling. It does not depend on heuristic function to evaluate the best next move to make, rather it just considers the game mechanics to play random rollouts and get an expected reward after a fixed number of iterations. 

Here we attach some of papers as part of the literature revised for developing this project:
- **[A Survey of Monte Carlo Tree Search Methods](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=B7BB1338BDE1F287ECFC52AD86AFD055?doi=10.1.1.297.3086&rep=rep1&type=pdf)**
- **[Monte-Carlo Tree Search and Minimax Hybrids](https://dke.maastrichtuniversity.nl/m.winands/documents/paper%2049.pdf)**
- **[Score Bounded Monte-Carlo Tree Search](https://pdfs.semanticscholar.org/d2c4/8b5d3fe77521bf0b0b0ec5f0b43e6b5f9723.pdf)**
- **[On the Dangers of Random Playouts](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.297.4379&rep=rep1&type=pdf)**

## Running the game

### Prerequisites

The code was written in Python 2.7. In order to display the game's GUI, we used [Tkinter](https://docs.python.org/2/library/tkinter.html) module, which is the standard Python interface to the Tk GUI toolkit. Although you don't need to download Tkinter since it is an integral part of all Python distributions. In any case, you can find more details about Tkinter installation [here](http://ftp.ntua.gr/mirror/python/topics/tkinter/download.html).

### Run
```
git clone https://github.com/Alfo5123/Connect4.git
cd Connect4
python game.py
```

Have fun!

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Alfo5123/Connect4/blob/master/LICENSE) file for details

## Acknowledgments

* Samuel Vidal, for suggesting this challenge.

