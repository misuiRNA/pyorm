

class TemplateTitle:

    @classmethod
    def print_head(cls):
        print("-------+-----------+-------+-----------------------------------------------------------")
        print("|  id  ", end="")
        print("| doctype id", end="")
        print("| status", end="")
        print("| template data", end="")
        print("")
        print("-------+-----------+-------+-----------------------------------------------------------")

    @classmethod
    def print_end(cls):
        print("")
        print("-------+-----------+-------+-----------------------------------------------------------")

    @classmethod
    def print_cut_line(cls):
        print("")
        print(">>>>>>===========================================================================<<<<<<")
