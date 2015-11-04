""""Paint program by Dave Michell.

Subject: tkinter "paint" example
From: Dave Mitchell <davem@magnet.com>
To: python-list@cwi.nl
Date: Fri, 23 Jan 1998 12:18:05 -0500 (EST)

  Not too long ago (last week maybe?) someone posted a request
for an example of a paint program using Tkinter. Try as I might
I can't seem to find it in the archive, so i'll just post mine
here and hope that the person who requested it sees this!

  All this does is put up a canvas and draw a smooth black line
whenever you have the mouse button down, but hopefully it will
be enough to start with.. It would be easy enough to add some
options like other shapes or colors...

                                                yours,
                                                dave mitchell
                                                davem@magnet.com

Changes to also print out draw commands to stdout by gorke.aygun@gmail.com
Changes to convert to class by caydinc@gmail.com 
"""

import sys
from Tkinter import *

"""paint.py: not exactly a paint program.. just a smooth line drawing demo."""

class BoardCanvas():
    def __init__(self):
        self.b1 = "up"
        self.x = None
        self.y = None
        self.root = Tk()
        self.drawing_area = Canvas(self.root)
        self.drawing_area.pack()
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>", self.b1up)

    def main(self):
        self.root.mainloop()

    def b1down(self,event):
        self.b1 = "down"  
        print "GOTO %d %d" % (event.x, event.y)
        print "ZDOWN"    # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

    def b1up(self,event):
        self.b1 = "up"
        self.x = None           # reset the line when you let go of the button
        self.y = None
        print "ZUP"
        print ""
        sys.stdout.flush()

    def motion(self,event):
        if self.b1 == "down":
            if self.x is not None and self.y is not None:
                event.widget.create_line(self.x,self.y,event.x,event.y,smooth=TRUE)
                print "MOVE %d %d" % (event.x - self.x, event.y - self.y)
                # here's where you draw it. smooth. neat.
        self.x = event.x
        self.y = event.y

if __name__ == "__main__":
    c = BoardCanvas()
    c.main()

