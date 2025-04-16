def create_world(width, height):
    return {
        'static': {
            'width': width,
            'height': height,
            'chunks': generate_chunks(width, height)
        },
        'dynamic': {
            'entities': 0,
        }
    }

def create_entity():
    pass

def tick():
    pass

def generate_chunks(width, height):
    for i in range(width + 1):      # 0-599 -> 0-600
        for j in range(height + 1): # 0-599 -> 0-600
            print(i, j)

if __name__ == '__main__':
    world = create_world(600, 600)
    print(world)