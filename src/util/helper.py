from tifffile import imsave
import numpy as np
import random
import os
import csv

def delta_epsilon(a, b, e):
    return abs(a-b) < e


def generatePointSet(z, y, x,
                     minZRad,
                     maxZRad,
                     minYRad,
                     maxYRad,
                     minXRad,
                     maxXRad):
    center = (rand(0, z), rand(0, y), rand(0, x))
    toPopulate = []
    zRad = rand(minZRad, maxZRad)
    yRad = rand(minYRad, maxYRad)
    xRad = rand(minXRad, maxXRad)

    for cz in range(-zRad, zRad):
        for cy in range(-yRad, yRad):
            for cx in range(-xRad, xRad):
                curPoint = (center[0]+cz, center[1]+cy, center[2]+cx)
                #only populate valid points
                valid = True
                dimLimits = [z, y, x]
                for dim in range(3):
                    if curPoint[dim] < 0 or curPoint[dim] >= dimLimits[dim]:
                        valid = False
                if valid:
                    toPopulate.append(curPoint)
    return set(toPopulate)


def generateTestVolume(z, y, x,
                       minCluster,
                       maxCluster,
                       minZRad,
                       maxZRad,
                       minYRad,
                       maxYRad,
                       minXRad,
                       maxXRad):
    #create a test volume
    volume = np.zeros((z, y, x))
    myPointSet = set()
    for _ in range(rand(minCluster, maxCluster)):
        potentialPointSet = generatePointSet(z, y, x,
                                             minZRad,
                                             maxZRad,
                                             minYRad,
                                             maxYRad,
                                             minXRad,
                                             maxXRad)
        #be sure there is no overlap
        while len(myPointSet.intersection(potentialPointSet)) > 0:
            potentialPointSet = generatePointSet(z, y, x,
                                                 minZRad,
                                                 maxZRad,
                                                 minYRad,
                                                 maxYRad,
                                                 minXRad,
                                                 maxXRad)

        for elem in potentialPointSet:
            myPointSet.add(elem)

    #populate the true volume
    for elem in myPointSet:
        volume[elem[0], elem[1], elem[2]] = 1

    return volume, list(myPointSet)


def visualize_volume(volume):
    points = np.nonzero(volume)
    zs = points[0]
    ys = points[1]
    xs = points[2]

    fig = plt.figure()

    ax1=fig.add_subplot(2,2,1, projection='3d')
    ax2=fig.add_subplot(2,2,2)
    ax3=fig.add_subplot(2,2,3)
    ax4=fig.add_subplot(2,2,4)

    ax1.set_title('3D View')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    ax1.scatter(xs, ys, zs)

    ax2.set_title('xy View')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.scatter(xs, ys)

    ax3.set_title('xz View')
    ax3.set_xlabel('x')
    ax3.set_ylabel('z')
    ax3.scatter(xs, zs)

    ax4.set_title('yz View')
    ax4.set_xlabel('y')
    ax4.set_ylabel('z')
    ax4.scatter(ys, zs)


    plt.tight_layout(pad=1.5)
    plt.show()


def save_tif(img, fname):
    if ".tif" not in fname:
        fname = fname + ".tif"
    save_path = "../img/"+fname if os.path.isdir("../img/") else fname
    save_path = "./img/"+fname if os.path.isdir("./img/") else fname
    imsave(save_path, img.astype(np.uint8))
    print("Saved tif as: ", fname, " at ", save_path)

def write_csv(rows, fname):
    if ".csv" not in fname:
        fname = fname + ".csv"
    save_path = "../centers/"+fname if os.path.isdir("../centers/") else fname
    save_path = "./centers/"+fname if os.path.isdir("./centers/") else fname
    with open(save_path, 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
    print("Saved csv as: ", fname, " at ", save_path)

def read_csv(fname):
    if ".csv" not in fname:
        fname = fname + ".csv"
    # read_path = "../centers/" + fname if os.path.isdir("../centers/") else fname
    # read_path = "./centers/" + fname if os.path.isdir("./centers/") else fname
    content = []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            content.append(r)
    return content

def txt_2_csv(fname):
    pass

def txt_to_3pts(fname, delimiter=' '):
    points = []
    with open(fname, 'r') as f:
        for line in f:
            x, y, z = line.split(delimiter)
            points.append((x, y, z))
    return list(map(lambda x: tuple(map(int, x)), points))

def csv_to_3pts(fname, delimiter=' '):
    points = []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            points.append((r[0], r[1], r[2]))
    return list(map(lambda x: tuple(map(int, tuple(map(float, x)))), points))

def set_rgb(img, x, y, z, r, g, b):
    img[z, y, x, 0] = r
    img[z, y, x, 1] = g
    img[z, y, x, 2] = b

def add_rgb(img, x, y, z, r, g, b):
    img[z, y, x, 0] = min_max(r + img[z, y, x, 0], 255, 0)
    img[z, y, x, 1] = min_max(g + img[z, y, x, 1], 255, 0)
    img[z, y, x, 2] = min_max(b + img[z, y, x, 2], 255, 0)

def min_max(x, minimum, maximum):
    return np.maximum(np.minimum(x, minimum), maximum)

def bound_check(x, minimum, maximum):
    return (x > minimum and x < maximum)

def random_3D(x_range, y_range, z_range):
    x = random.randint(x_range[0], x_range[1])
    y = random.randint(y_range[0], y_range[1])
    z = random.randint(z_range[0], z_range[1])
    return (x, y, z)

def gauss_3D(x_mean, y_mean, z_mean, x_sigma, y_sigma, z_sigma):
    x = random.gauss(x_mean, x_sigma)
    y = random.gauss(y_mean, y_sigma)
    z = random.gauss(z_mean, z_sigma)
    return (x, y, z)

def random_val(max_val):
    return random.random() * max_val

def euc_dist(x_1, y_1, z_1, x_2, y_2, z_2):
    return np.sqrt((x_1 -x_2)**2 + (y_1 - y_2)**2 + (z_2 - z_2)**2)

def euc_dist(c_1, c_2):
    return np.sqrt((c_1[0] - c_2[0])**2 + (c_1[1] - c_2[1])**2 + (c_1[2] - c_2[2])**2)

if __name__ == '__main__':
    print(delta_epsilon(1., 1.1, .2) == True)
    print(delta_epsilon(1., 1.1, .01) == False)
