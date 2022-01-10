# python3
# rotate_matrix.py - Takes in an image and rotates that images 90 degrees clockwise.

def rotate_matrix(image):
    '''
    Takes in an image and rotates that images 90 degrees counter clockwise.
    '''
    for line in range(0, len(image[0]), 1):
        for pixel in range(len(image), 0, -1):
            print(image[pixel-1][line], end=' ')
        print()
    print('\n')

def mirror_matrix(image):
    for line in range(len(image[0]), 0, -1):
        for pixel in range(len(image), 0, -1):
            print(image[line-1][pixel-1], end=' ')
        print()
    print('\n')

matrix = [
    [[1], [2], [3], [4]],
    [[5], [6], [7], [8]],
    [[9], [10], [11], [12]],
    [[13], [14], [15], [16]],
]

rotate_matrix(matrix)
mirror_matrix(matrix)