from chunk import Chunk
from entity import Entity

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chunks = self.generate_chunks()
        self.entities = []

    def generate_chunks(self):
        chunks = []
        for i in range(self.width):
            row = []
            for j in range(self.height):
                row.append(Chunk(i, j))
            chunks.append(row)
        return chunks

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def tick(self):
        print('hola')
        for entity in self.entities:
            entity.update()
