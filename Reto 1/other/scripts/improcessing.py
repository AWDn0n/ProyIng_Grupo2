from skimage import transform

def resize_image(image_array, target_size: tuple):
    return transform.resize(image_array, (target_size[0], target_size[1]))