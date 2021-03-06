### Build status

[![Build Status](https://travis-ci.org/scal444/minesweeper.svg?branch=master)](https://travis-ci.org/scal444/minesweeper)
[![codecov](https://codecov.io/gh/scal444/minesweeper/branch/master/graph/badge.svg)](https://codecov.io/gh/scal444/minesweeper)

### Organizational notes
These are working notes on how to organize the setup, discussing (with self)
how to divide responsibilities

We (I) want to make this both an interact-able game and a minesweeper solver
engine, and of course the two will interact. The first division then is that the
GUI stuff should be independent of the underlying data representation. We need
to be able to run this interactively, run it automatically, or any combination
in between. We can start with a draw-board functionality, that gets called to
represent the current state of the board. It doesn't have to be efficient - we can
re-draw every panel at the start, and then worry about the rest afterwards. The only
stipulation is that if we have a game frame up already, it should work on that frame,
rather than recreating a widget or whatever.

So, preliminarily, we'll have 3 main objects. A runner, a board, and a visualization
of the board. The visualization can be drop-in customizable (or even optional), and
is specified by the runner. If a widget, the visualization can send signals back to the runner, which
can handle them by updating the board state and or the visualization


What this gives us is a clear difference between visualization and representation.
We'll start with that. The next thing is manipulation of the representation. This needs
to be able to be accessed both through a gui click, and as an automated workflow. So there
should be some clickaction interface to handle it.

For visibility, we should maybe consider an enum of (unvisited, visited,
marked_as_flag, marked_as_question). Can a numpy array hold that?
