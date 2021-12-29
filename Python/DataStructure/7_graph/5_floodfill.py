'''
实际上漫水填充法就是选择一个像素，以四连通为连通域，将其所属的连通域的所有值转化为新值
'''

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def floodFill(image, pixel, color):
    value = image[pixel[0]][pixel[1]]
    dfs(image, pixel, value, color)
    return image

def is_valid(x, y, image):
    m = len(image)
    n = len(image[0])
    return x >= 0 and y >= 0 and x < m and y < n

def get_fourConect(image, node):
    for direct in directions:
        new_x = node[0] + direct[0]
        new_y = node[1] + direct[1]
        if is_valid(new_x, new_y, image):
            yield [new_x, new_y]

def dfs(image, node, value, color):
    image[node[0]][node[1]] = color

    for nbr in get_fourConect(image, node):
        if image[nbr[0]][nbr[1]] != color:
            if image[nbr[0]][nbr[1]] == value:
                dfs(image, nbr, value, color)

'''
简洁写法
'''     

def floodFill(image, sr, sc, newColor):
    rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]
    def traverse(row, col):
        if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
            return
        image[row][col] = newColor
        [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
    if orig_color != newColor:
        traverse(sr, sc)
    return image

if __name__=="__main__":
    image = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ]
    sr = 1
    sc = 1
    newColor = 2
    floodFill(image, sr, sc, newColor)
