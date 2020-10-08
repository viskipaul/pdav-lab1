def encode(filename):
    f = open(filename, "r")
    img = f.read()
    index = 4
    img_rgb = img.splitlines()
    img_yuv = []
    dim_x = int(img_rgb[2].split(" ")[0])
    dim_y = int(img_rgb[2].split(" ")[1])
    print("Dim: ", dim_x, "x", dim_y)
    img_y = []
    img_u = []
    img_v = []
    while(index < len(img_rgb)):
        r = int(img_rgb[index])
        g = int(img_rgb[index+1])
        b = int(img_rgb[index+2])

        y = 0.299 * r + 0.587 * g + 0.114 * b
        u = 128 - 0.1687 * r - 0.3312 * g + 0.5 * b
        v = 128 + 0.5 * r - 0.4186 * g - 0.0183 * b

        img_yuv.append(y)
        img_yuv.append(u)
        img_yuv.append(v)

        img_y.append(y)
        img_u.append(u)
        img_v.append(v)
        index += 3

    print(img_yuv[:5])
    print(img_y[:5])
    print(img_u[:5])
    print(img_v[:5])

    print(len(img_y))
    print(len(img_u))
    print(len(img_v))

    img_y_matrix = []

    #Transform y to matrix:
    for j in range(dim_y):
        aux_array = []
        for i in range(dim_x):
            aux_array.append(img_y[i])
        img_y_matrix.append(aux_array)

    # for i in range(len(img_y)):
