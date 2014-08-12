
#!/usr/bin/python2.7

from tictactoe import Board

b = Board(3,3)
b.set_mark(1, "X")
b.set_mark(2, "X")
b.set_mark(3, "X")
#b.set_mark(4, "Y")

#print b.b
#b.are_marks_equal(1,2,3)
b.print_board()



