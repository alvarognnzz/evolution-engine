import time

from engine.world import World
from engine.entity import Entity
from engine.components.movement import Movement

TPS = 1
tick_interval = 1 / TPS

if __name__ == '__main__':
    world = World(600, 600)
    entity = Entity()
    entity.add_component(Movement())
    world.add_entity(entity)
    print(f'World: {world.width}x{world.height}')
    print(f'Chunks: {len(world.chunks)}x{len(world.chunks[0])}')

    while True:
        time.sleep(tick_interval)
        world.tick()