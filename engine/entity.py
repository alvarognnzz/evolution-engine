class Entity:
    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[component.name] = component
    
    def get_component(self, name):
        return self.components.get(name)
    
    def update(self):
        for component in self.components.values():
            if hasattr(component, 'update'):
                component.update()
