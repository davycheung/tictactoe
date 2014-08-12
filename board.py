
#!/usr/bin/python2.7

class Board(object):

    def __init__(self, num_row, num_col):
        self.num_row = num_row
        self.num_col = num_col
        self.b = {}
        for i in range(1, (num_row*num_col) + 1):
            self.b[i] = None

    def get_available_pos(self):
        pos_list = []
        for i in range(1, (self.num_row*self.num_col) + 1):
            if self.has_mark(i) is False:
                pos_list.append(i)
        return pos_list

    def set_mark(self, pos, value):
        self.b[pos] = value

    def has_mark(self, pos):
        if self.b[pos] is None:
            return False
        else:
            return True

    def is_all_marked(self):
        for i in range(1, (self.num_row*self.num_col) + 1):
            if self.has_mark(i) is False:
                return False
        return True

    def are_marks_equal(self, *pos):
        pos_list = list(pos)
        val_list = []
        for index in pos_list:
            pos_val = self.b[index]
            if pos_val is None:
                return False
            val_list.append(pos_val)
        if len(set(val_list)) == 1:
            return True
        else:
            return False

    def print_board(self):
        j = 0
        print "--------------------"
        print " | ",
        for i in range(1, (self.num_row * self.num_col) + 1):
            if j >= self.num_col:
                j=0
                print " "
                print "--------------------"
                print " | ",

            j += 1
            val = self.b[i]
            if val is None:
                print " ",
            else:
                print val,
            print " | ",
        print " "
        print "--------------------"
