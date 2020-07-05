# Banner-Print3r / Plott3r / Druck3r

A robot printer let EV3 sign your name!

PLOTT3R is a simple robot that prints block letters on standard calculator paper!

The "LEGO EV3" program prints its name on the paper. Each block letter is described on its own line, the soimplest way possible.

More advanced users might be able to make this program better by reading the text from a file, or storing the letter paths in a file, but we'll leave that up to you to figure out.

PlotStep is the basic building block of this little application.
------------------------------------------------
You can tell the block to draw a line to any absolute target coordinate.

The arrow parameter is the pen Up/Down value. Use TRUE for up and FALSE for down.

Note this assumes that the program starts with the pen in the UP position!
------------------------------------------------
The Y parameter moves the pen up and down. 0 is the lowest value, and 100 is the higest value.

Don't use values outside this range unless you fix the block to limit the range :-)
------------------------------------------------
The X parameter moves the paper left and right. You can use any value for X, but a reasonable character width is 50.

Note that it's best to reset the X motor before printing a character so that it's easier to figure out the coordinates of each stroke in the letter.
------------------------------------------------
