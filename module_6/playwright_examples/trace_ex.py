from fileinput import filename
from pathlib import Path
from datetime import datetime


class Tools:
    @staticmethod
    def project_dir():
        """
        Возвращает корневую директорию проекта.
        Предполагается, что текущий файл находится в поддиректории `common`.
        """
        return Path(__file__).parent.parent.parent #Добавил .parent, чтобы попасть в корневую папку. /Users/Marsel/Coconut_tests

    '''
    - Path(__file__): Получает путь к текущему файлу (тому, где написан этот код)
    - .parent: Поднимается на один уровень выше (в родительскую директорию)
    - .parent.parent: Поднимается ещё на один уровень выше, чтобы получить корневую директорию проекта'''

    @staticmethod
    def files_dir(nested_directory: str = None, filename: str = None):
        """
        Возвращает путь к директории `files` (или её поддиректории).
        Если директория не существует, она создается.
        Если указан `filename`, возвращает полный путь к файлу.
        """
        files_path = Tools.project_dir() / "files" # Берет путь к корневой папке, добавляет папку files
        if nested_directory: # Если передали имя папки, которой нужно вложить в files
            files_path = files_path / nested_directory # берет путь ../file/ добавляет имя вложенной директории
        files_path.mkdir(parents=True, exist_ok=True) # Создает директорию
        #parents=True: Создаёт все необходимые родительские директории, exist_ok=True: Не выбрасывает ошибку, если директория уже существует

        if filename:
            return files_path / filename
        return files_path

    @staticmethod
    def get_timestamp():
        """
        Возвращает текущую временную метку в формате YYYY-MM-DD_HH-MM-SS.
        """
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

if __name__ == "__main__":
    #print(Tools.project_dir()) #принтует коневую директорию
    Tools.files_dir() #Создает папку files
    #print(Tools.files_dir(filename='my_str')) #Создает папку files, test return filename