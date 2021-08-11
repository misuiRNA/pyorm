

class MarkTaskTitle:

    @classmethod
    def print_head(cls):
        print("-------+---------+------------------")
        print("|  id  ", end="")
        print("| group id", end="")
        print("| template id", end="")
        print("")
        print("-------+---------+------------------")

    @classmethod
    def print_end(cls):
        print("-------+---------+------------------")

    @classmethod
    def print_cut_line(cls):
        print("")
        print(">>>>>>========================<<<<<<")
