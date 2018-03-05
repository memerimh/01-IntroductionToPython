"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mattias Memering.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(1)
bjorn = rg.SimpleTurtle()
ragnar = rg.SimpleTurtle('turtle')
bjorn.pen = rg.Pen('red', 10)
ragnar.pen = rg.Pen('green', 10)
bjorn.forward(25)
for k in range (15):
    bjorn.left(12)
    bjorn.forward(12)
    ragnar.right(30)
    ragnar.forward(30)
bjorn.left(90)
bjorn.forward(115)
bjorn.right(90)
bjorn.forward(75)
for k in range (15):
    bjorn.right(12)
    bjorn.forward(12)
    ragnar.right(30)
    ragnar.forward(30)
bjorn.right(90)
bjorn.forward(115)
window.close_on_mouse_click()