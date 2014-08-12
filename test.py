
#!/usr/bin/python2.7

from board import Board

#b = Board(3,3)
#b.set_mark(1, "X")
#b.set_mark(2, "X")
#b.set_mark(3, "X")
#b.set_mark(4, "Y")

#print b.b
#b.are_marks_equal(1,2,3)
#b.print_board()


instruction_b = Board(3,3)
for i in range(1, 10):
    instruction_b.set_mark(i, i)

instruction_b.print_board()
