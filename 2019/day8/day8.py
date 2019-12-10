WIDTH = 25
HEIGHT = 6

def get_layer_with_fewest_zeroes(layers):
    zeroes_count = [layer.count('0') for layer in layers]
    return layers[zeroes_count.index(min(zeroes_count))]

def get_checksum(layer):
    return layer.count('1') * layer.count('2')

def get_layers(image):
    global WIDTH
    global HEIGHT
    layers = []
    for i in range(0, len(image), WIDTH*HEIGHT):
        layers.append(image[i:i+WIDTH*HEIGHT])
    return layers

def get_image(filename):
    with open(filename, 'r') as f:
        return f.read().replace('\n', '')

def decode(layers):
    global WIDTH
    global HEIGHT
    decoded_image = []
    for i in range(WIDTH*HEIGHT):
        j = 0
        while j < len(layers) and layers[j][i] == '2':
            j += 1
        if j == len(layers):
            decoded_image.append('2')
        else:
            decoded_image.append(layers[j][i])
    return decoded_image

def print_image(result):
    global WIDTH
    global HEIGHT
    for i in range(HEIGHT):
        for j in range(WIDTH):
            print(result[i*WIDTH + j], end='')
        print()

def main():
    image = get_image("day8.in")
    layers = get_layers(image)
    result = get_checksum(get_layer_with_fewest_zeroes(layers))
    #part 1
    print(result)

    result = decode(layers)
    #part 2
    print_image(result)


if __name__ == "__main__":
    main()
