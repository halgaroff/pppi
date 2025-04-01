class Table:
    def __init__(self):
        self.cells = {}

    def set_cell(self, address, value):
        self.cells[address] = value

    def get_cell(self, address):
        return self.cells.get(address, None)