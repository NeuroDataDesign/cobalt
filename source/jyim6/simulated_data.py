import sys
sys.path.append('./util/')
from util.ImageGenerator import ImageGenerator


# Feel free to change the dimensions.
# Changing the dimensions will change how many cells are in each image
img_gen = ImageGenerator(1000,1000,100)

# Most basic, easiest image with 45 solid well separated cells
_, centers_1 = img_gen.make_ellipsoidal_image(
    25,
    25,
    5,
    200,
    200,
    10,
    fname = "solid_45_cells"
)


# Smaller cells with gaussian blur
_, centers_2 = img_gen.make_ellipsoidal_image(
    15,
    15,
    5,
    100,
    100,
    20,
    blur = True,
    blur_sigma = 5,
    fname = "blurred_147_cells",
)

# Solid cells with gaussian noise and random intensity levels
_, centers_3 = img_gen.make_ellipsoidal_image(
    25,
    25,
    5,
    200,
    200,
    10,
    add_img_noise = True,
    randomized_intensity = True,
    fname = "solid_45_cells_noise_random_intensity"
)


# Solid cells with gaussian added to the image
_, centers_3 = img_gen.make_ellipsoidal_image(
    15,
    15,
    5,
    100,
    100,
    20,
    add_img_noise = True,
    fname = "solid_147_cells_img_noise"
)


# cells distributed uniformly at random with overlaps and fade applied
_, centers_3 = img_gen.make_ellipsoidal_image(
    15,
    15,
    5,
    100,
    100,
    20,
    random_center = True,
    fade = True,
    overlap = True,
    randomized_intensity = True,
    fname = "faded_147_randomized_cells_random_intensity"
)


# cells distributed standard normal at random with overlaps and fade applied
_, centers_3 = img_gen.make_ellipsoidal_image(
    15,
    15,
    5,
    100,
    100,
    20,
    random_center = 'gauss',
    random_center_sigma = 8,
    fade = True,
    overlap = True,
    fname = "faded_147_randomized_gauss_cells"
)

# More cells distributed standard normal at random with overlaps and fade applied
_, centers_3 = img_gen.make_ellipsoidal_image(
    10,
    10,
    5,
    100,
    100,
    10,
    random_center = 'gauss',
    blur = True,    
    overlap = True,
    fname = "blurred_147_randomized_gauss_cells",
)