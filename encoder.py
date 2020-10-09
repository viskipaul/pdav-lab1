def encode(filename):
    f = open(filename, "r")
    img = f.read()
    index = 4
    img_rgb = img.splitlines()
    img_yuv = []
    dim_x = int(img_rgb[2].split(" ")[0])
    dim_y = int(img_rgb[2].split(" ")[1])

    img_y = []
    img_u = []
    img_v = []

    while(index < len(img_rgb)):
        r = int(img_rgb[index])
        g = int(img_rgb[index+1])
        b = int(img_rgb[index+2])

        # read the PPM image and convert each pixel value from RGB to YUV (use the arithmetic equations from the slides of the course)
        y = 0.299 * r + 0.587 * g + 0.114 * b
        u = 128 - 0.1687 * r - 0.3312 * g + 0.5 * b
        v = 128 + 0.5 * r - 0.4186 * g - 0.0183 * b

        img_yuv.append(y)
        img_yuv.append(u)
        img_yuv.append(v)

        # form 3 matrixes: one for Y components, one for U components and one for V components
        img_y.append(y)
        img_u.append(u)
        img_v.append(v)
        index += 3

    img_y_matrix = []
    img_u_matrix = []
    img_v_matrix = []

    #Transform y,u,v to 800x600 matrix:
    for j in range(dim_y):
        aux_array_y = []
        aux_array_u = []
        aux_array_v = []
        for i in range(dim_x):
            aux_array_y.append(img_y[i])
            aux_array_u.append(img_u[i])
            aux_array_v.append(img_v[i])
        img_y_matrix.append(aux_array_y)
        img_u_matrix.append(aux_array_u)
        img_v_matrix.append(aux_array_v)


    print(img_y_matrix[90:95])
    print(img_u_matrix[90:95])
    print(img_v_matrix[90:95])

    # divide the Y matrix into blocks of 8x8 values; for each block store:
    # the 64 values/bytes from the block, the type of block (Y) and the position of the block in the image

    img_y_8x8blocks = []
    img_y_8x8blocks.append("y")
    img_u_8x8blocks = []
    img_u_8x8blocks.append("u")
    img_v_8x8blocks = []
    img_v_8x8blocks.append("v")

    for j in range(int(dim_x / 8)):
        for i in range(int(dim_y/8)):
            fin_array_y = []
            fin_array_u = []
            fin_array_v = []
            aux_array_y = []
            aux_array_u = []
            aux_array_v = []
            fin_array_y.append(i)
            fin_array_u.append(i)
            fin_array_v.append(i)
            fin_array_y.append(j)
            fin_array_u.append(j)
            fin_array_v.append(j)
            for n in range(8):
                for m in range(8):
                    aux_array_y.append(img_y_matrix[i*8+n][j*8+m])
                    aux_array_u.append(img_u_matrix[i*8+n][j*8+m])
                    aux_array_v.append(img_v_matrix[i*8+n][j*8+m])
            fin_array_y.append(aux_array_y)
            fin_array_u.append(aux_array_u)
            fin_array_v.append(aux_array_v)
            img_y_8x8blocks.append(fin_array_y)
            img_u_8x8blocks.append(fin_array_u)
            img_v_8x8blocks.append(fin_array_v)

    img_u_4x4blocks = []
    img_v_4x4blocks = []

    print(img_y_8x8blocks[85:95])
    print(img_u_8x8blocks[85:95])
    print(img_v_8x8blocks[85:95])
