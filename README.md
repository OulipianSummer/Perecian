# Knight's Tour v1.0.0

The current software implementation utilizes Warnsdorff's Rule to solve the knight's tour, which is a puzzle involving the movement of a knight on a chessboard such that the knight visits every square only once.

Warnsdorff's Rule is practical but far from perfect; it involves checking the next possible movements, determining the number of possible movements of those movements, and choosing the move that contains the least possibilities. The main rationale is that because the one rule of a knight's tour is to visit squares only once, choosing the move with the least possible moves decreases the chance of repeating any squares.

The Warnsdorff's Rule heuristic is static, meaning that the same path will always be taken for whichever starting position. Unfortunately, this means that Warnsdorff's Rule cannot solve tours that end prematurely. Therefore, this opens the opportunity to improve the knight's tour software solution via machine learning that can learn from failures and slightly adjust to take different paths.

Regardless, this software implementation is a basic introduction to utilizing a common heuristic and is an ample solution to beginner and intermediate programmers alike.


## Requirements

To run the implementation, you will need the following:
* [Python 3](https://www.python.org/downloads/)

## Execution

### Via Command Line

To run using the command line:

1. Open your command terminal.
2. Run the following command: `python main.py` or `python PATH\TO\main.py`
3. Enter x & y starting coordinates separated by spaces: `x y`

  ```
  Enter x & y (1-8) separated by a space (e.g. 4 4): x y
  ```

4. Hit "Enter" and view results.

  ```
  Enter x & y (1-8) separated by a space (e.g. 4 4): 6 7

  56 11 58 31 54 13 18 33 
  47 30 55 12 59 32 53 14 
  10 57 48 63 50 17 34 19 
  29 46 41 60 39 62 15 52 
  42  9 64 49 16 51 20 35 
  25 28 45 40 61 38  1  4 
   8 43 26 23  6  3 36 21 
  27 24  7 44 37 22  5  2 
  ```
  
### Via IDLE

To run using IDLE:

1. Open IDLE.
2. Open main.py.
3. Hit F5 or Run -> Run Module.
4. Enter x & y starting coordinates separated by spaces: `x y`

  ```
  Enter x & y (1-8) separated by a space (e.g. 4 4): x y
  ```

5. Hit "Enter" and view results.

  ```
  Enter x & y (1-8) separated by a space (e.g. 4 4): 6 5

  The knight's tour ended prematurely at (5,1) during move #60.

  34 31 10  0 26 29  8  5 
  11  0 33 30  9  6 23 28 
  32 35  0 25 48 27  4  7 
   0 12 59 36 53 24 49 22 
  60 43 54 47 58 37 18  3 
  13 46 57 52  1 50 21 38 
  42 55 44 15 40 19  2 17 
  45 14 41 56 51 16 39 20 
  ```
