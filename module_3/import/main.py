# Импортируем пакет лесопилки троллей
from troll_lumber_mill import TrollLumberMill, greet_trolls, check_wood_requirements

# Приветствие
greet_trolls()

# Создаём лесопилку
mill = TrollLumberMill()

# Тролли собирают древесину
mill.gather_wood(75)
mill.gather_wood(50)

# Проверяем, хватает ли дерева
check_wood_requirements(100, mill.wood_stock)

# Тролли используют древесину на укрепление строений
mill.reinforce_wood(80)

# Проверяем остаток дерева
check_wood_requirements(50, mill.wood_stock)

# Попытка укрепить строение, когда дерева не хватает
mill.reinforce_wood(100)
