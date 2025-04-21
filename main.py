import time

from world import World
from entity import Entity

TPS = 1
tick_interval = 1 / TPS

if __name__ == '__main__':
    world = World(600, 600)
    entity = Entity()
    world.add_entity(entity)
    print(f'World: {world.width}x{world.height}')
    print(f'Chunks: {len(world.chunks)}x{len(world.chunks[0])}')

    while True:
        time.sleep(tick_interval)
        world.tick()