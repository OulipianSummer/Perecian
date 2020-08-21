# Perecian
Perecian is an open souce CLI tool for writers written in Python.
                    
Based off of the constraints Georges Perec useed to create his masterpeice, Life: A User's Manual, Pereican uses both knight's tours, and mutually  orthogonal latin squares to create a unique list of constrained writing prompts for novels, short stories, poems, and much more.

## Quick Start
Perecian requires Docopt, PyFiglet, and PyInquirer, so make sure to execute:

```
pip install docopt pyfiglet pyinquirer
```

before running.

Perecian has a default run mode that will produce a prompts list for a 10 x 10 chess board starting at space 6,6. 
To run Perecian using the default settings, simply navigate to the Perecain folder using your CLI application of choice, and run 

```
python perecian.py default
```

Alternatively, you can run

```
python perecian.py
```
to pull up the main menu. From there, you can select

```
New Custom Tour
```
to make a new tour to your own specifications, using your own lists (if required).

## How It Works

By default, Perecian creates prompts by first solving a knight's tour on  a 10 x 10 chess board. A knight's tour is a classic logic puzzle involving moving a single knight chess piece in such a way that it visits or "tours" every space on a chess board exactly once. To put this puzzle in perspective, 
a standard 8 x 8 chessboard contains over 19 quadrillion possible knight's tours!

In order to make this puzzle easier to solve, Perecian utilizes a simple rule called Warnsdorff's Rule, first described by H. C. von Warnsdorff in 1823. The rule states that a tour can be solved on any chess board (larger than 4 x 4), from any starting position granted that the puzzle solver always moves the knight to the square with the fewest possible following moves. Using this heuristic, Perecian is able to solve a knight's tour in less than a second on most computers.
    
Next, Perecian uses the move coordinates of the knight's tour to reference 21 mutually orthogonal latin squares (MOLS) of order 10 (also created by  Perecain at run time). A MOLS (someitmes refered to as a latin bi-square or a graeco-latin square) is another mathematical puzzle created from combining two latin squares, which are spiritually similar to a Sudoku square. Each row in  an order 10 latin square contains the numbers 1 - 10, and each column also contains the numbers 1 - 10. A MOLS is created by overlaying two latin squares such that each number pairing across the grid is unique.

Using the coordinates from each step in the knight's tour, Perecian references that same square in each of the 21 MOLS. For example, if the knight starts at row 6, column 6, Perecain will look at the number pairings in row 6, column 6 of each of the MOLS. Using the unique number parings located at that specific cell in each MOLS table, Perecian makes an aditional reference to a list of prompts stored in lists/default.csv. Using each of those unique number pairings stored in the 21 MOLS, Perecian constructs a unique list of 42 prompts for each move the knight makes in its tour.

At the end of this dizzying list of steps, chess moves, and cross references, Perecian produces 100 unique lists of 42 prompts. For the writer, each list is constructed as a checklist of items, colors, materials, movitves, feelings, ideas, books, paintings, quotes, and much more. These lists, like in Life: A User's Manual are considerd to be a sort of inventory of what each chapter of a potential novel will contain. 
                    
## For Writers

Using these lists, a writer is able to construct an entire novel's worth of constrained writing prompts. Perecian can also be customized to export tours both larger and smaller than those created by a 10 x 10 chess board. Writers are encouraged to add or remove constraints as they see fit (since Perec himself did so, either strictly or loosely adhereing to constraints as the need arose or inspiration struck), but the aim of Perecian is to challenge writers to test their skills by trying to adhere to the constraints as much as possible to train and challenge themselves to produce works entirely unlike what they are used to creating.


Writers are encouraged to be as creative as possible when writing using the prompts created by Perecian. Georges Perec himself used similar constratints and took them a step further by overlaying the knight's tour chess board onto a floorplan of a fictional Parisian apartment building wherein each chapter represented stories of the residents of that building told in the order of the knight's tour.
                    
Additionally, Perecain's lists could also be used as prompts for poetry, short stories, letters, and much more. 

## Customization

Perecain's default prompt's list (found in ```lists/default.csv```) can be customized for different themes, genres, settings, and more. In order to make your own, it is best to simply make a copy of ```lists/empty.csv``` and fill in all of the empty cells with your own content.

## Beta V1.1
Perecian is still in beta! If you would like to contribute to this project, feel free to open a PR

## Changelog
+ Aug 21: Update to Beta 1.1, added new features, cleaned up codebase, added some bugfixes, added instructions
+ Aug 20: First build Beta 1.0
