from matplotlib import pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

mat = plt.imread("resources/scale_down.JPG")

# fig=plt.figure(figsize=(2, 3))
# plt.figure()
# plt.axis("off")
# f, axarr = plt.subplots(2, 2)
gs1 = gridspec.GridSpec(2, 2)
gs1.update(wspace=0.025, hspace=0.05)
# imgplot = np.array(imgplot)
mat_gray = np.average(mat, axis=2)
# print(mat_gray.shape)
# print(type(mat_gray))
# print(mat_gray.max())


def prewitt_filter():
    vertical_filter = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    horizontal_filter = np.transpose(vertical_filter)
    return vertical_filter, horizontal_filter


def sobel_filter():
    vertical_filter = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    horizontal_filter = np.transpose(vertical_filter)
    return vertical_filter, horizontal_filter


# vertical_filter, horizontal_filter = prewitt_filter()
s_ver_filter, s_hor_filter = sobel_filter()
p_ver_filter, p_hor_filter = prewitt_filter()


gradient_sobel = np.zeros(mat_gray.shape)
gradient_prewitt = np.zeros(mat_gray.shape)

gradient_dir = np.zeros(mat_gray.shape)
gradient_x = np.zeros(mat_gray.shape)
# gradient_x_dir = np.zeros(mat_gray.shape)
gradient_y = np.zeros(mat_gray.shape)
# gradient_y_dir = np.zeros(mat_gray.shape)
for x in range(1, len(mat_gray) - 1):
    for y in range(1, len(mat_gray[0]) - 1):
        g_sobel_x = np.sum(mat_gray[x - 1 : x + 2, y - 1 : y + 2] * s_ver_filter)
        g_sobel_y = np.sum(mat_gray[x - 1 : x + 2, y - 1 : y + 2] * s_hor_filter)
        g_prewitt_x = np.sum(mat_gray[x - 1 : x + 2, y - 1 : y + 2] * p_ver_filter)
        g_prewitt_y = np.sum(mat_gray[x - 1 : x + 2, y - 1 : y + 2] * p_hor_filter)
        # gradient_x[x, y] = g_x
        # gradient_y[x, y] = g_y
        gradient_sobel[x, y] = np.sqrt(g_sobel_x ** 2 + g_sobel_y ** 2)
        gradient_prewitt[x, y] = np.sqrt(g_prewitt_x ** 2 + g_prewitt_y ** 2)

        # gradient_dir[x, y] = np.arctan2(g_y, g_x)

ax = plt.subplot(gs1[0])
ax.imshow(mat)
ax.axis("off")

ax = plt.subplot(gs1[1])
ax.imshow(mat_gray, cmap="gray")
ax.axis("off")

ax = plt.subplot(gs1[2])
ax.imshow(gradient_sobel, cmap="gray")
ax.axis("off")

ax = plt.subplot(gs1[3])
ax.imshow(gradient_prewitt, cmap="gray")
ax.axis("off")

# plt.imshow(gradient, cmap="gray")
# plt.subplots_adjust(wspace=0.25, hspace=)
plt.show()
# plt.imshow(mat)
