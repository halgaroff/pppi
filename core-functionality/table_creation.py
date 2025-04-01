class Table:
    """
    Класс для создания и управления таблицами.

    Attributes:
        cells (dict): Словарь для хранения значений ячеек таблицы.

    Methods:
        set_cell(address, value): Устанавливает значение в указанную ячейку.
        get_cell(address): Возвращает значение из указанной ячейки.
        clear_table(): Очищает все данные в таблице.
    """

    def __init__(self):
        """Инициализирует пустую таблицу."""
        self.cells = {}

    def set_cell(self, address, value):
        """
        Устанавливает значение в указанную ячейку.

        Args:
            address (str): Адрес ячейки (например, "A1").
            value (any): Значение для записи в ячейку.
        """
        self.cells[address] = value

    def get_cell(self, address):
        """
        Возвращает значение из указанной ячейки.

        Args:
            address (str): Адрес ячейки (например, "A1").

        Returns:
            any: Значение ячейки или None, если ячейка не существует.
        """
        return self.cells.get(address, None)

    def clear_table(self):
        """
        Очищает все данные в таблице.

        Clears the entire table by resetting the cells dictionary.
        """
        self.cells.clear()