class TrollLumberMill:
    def __init__(self):
        self.wood_stock = 0  # Изначальный запас дерева
        print("Лесопилка троллей построена! 🪓")

    def gather_wood(self, amount):
        self.wood_stock += amount
        print(f"Тролли собрали {amount} дерева. Всего: {self.wood_stock}.")

    def reinforce_wood(self, amount):
        if self.wood_stock >= amount:
            self.wood_stock -= amount
            print(f"Тролли использовали {amount} дерева для укрепления строений. Осталось: {self.wood_stock}.")
        else:
            print("Тролли орут: 'Нужна еще древесина!'")
