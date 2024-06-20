class Group:

    def __init__(self, name=None, header=None, footer=None): # =None означает, что если значение при вызове
                                                    # конструктора не будет заполнено, то оно не будет
                                                    # инициализировано (останется таким же, как было)
        self.gp_name = name
        self.gp_header = header
        self.gp_footer = footer
