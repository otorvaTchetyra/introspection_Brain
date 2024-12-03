class Brain:
    def __init__(self):
        self.regions = []

    def add_region(self, region):
        self.regions.append(region)

    def describe(self):
        return (f'This brain has {len(self.regions)} regions: ' + ', '.join(region.name for region in self.regions))

class Cerebrum(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Cerebrum'
        self.functions = ['thinking', 'sensation', 'movement']

    def describe(self):
        return (f'{self.name} is responsible for {", ".join(self.functions)}')

class Cerebellum(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Cerebellum'
        self.functions = ['coordination', 'balance', 'motor control']

    def describe(self):
        return (f'{self.name} is responsible for {", ".join(self.functions)}')

class Brainstem(Brain):
    def __init__(self):
        super().__init__()
        self.name = 'Brainstem'
        self.functions = ['breathing', 'heart rate', 'sleep']

    def describe(self):
        return (f'{self.name} controls basic life functions like {", ".join(self.functions)}')

def introspection_info(obj):
    # Определяем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    
    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Определяем модуль, к которому принадлежит объект
    obj_module = obj.__module__

    # Собираем информацию в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info

if __name__ == "__main__":
    brain = Brain()
    cerebrum = Cerebrum()
    cerebellum = Cerebellum()
    brainstem = Brainstem()

    brain.add_region(cerebrum)
    brain.add_region(cerebellum)
    brain.add_region(brainstem)

    print(brain.describe())
    print(cerebrum.describe())
    print(cerebellum.describe())
    print(brainstem.describe())

    # Интроспекция объектов
    print("\nBrain introspection:")
    print(introspection_info(brain))

    print("\nCerebrum introspection:")
    print(introspection_info(cerebrum))

    print("\nCerebellum introspection:")
    print(introspection_info(cerebellum))

    print("\nBrainstem introspection:")
    print(introspection_info(brainstem))
