from PIL import Image
import os

def clean_image_data(filepath):
    directory = f"{filepath}/images/"
    dirs = [file for file in os.listdir(directory) if not file.startswith('.')]
    # dirs = os.listdir(f"{filepath}/images/")
    print(len(dirs))
    print(dirs[:5])
    new_dir = os.path.join(filepath, "cleaned_images")
    os.mkdir(new_dir)
    for n, image in enumerate(dirs, 1):
        im = Image.open(f'{directory}/{image}')
        print(im.format, im.size, im.mode)
        final_size = 512
        new_im = resize_image(final_size, im)
        new_im.save(f'{new_dir}/{image}')
        # new_im.save(f'{new_dir}/{n}_resized.jpg')


def resize_image(final_size, im):
    size = im.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    im = im.resize(new_image_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (final_size, final_size))
    new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_im

if __name__ == '__main__':
    clean_image_data("/Users/venus/Downloads")

    """ Check if it's same size """
    # dirs = os.listdir("/Users/venus/Downloads/cleaned_images")
    # for image in dirs:
    #     im = Image.open(f"/Users/venus/Downloads/cleaned_images/{image}")
    #     print(im.format, im.size, im.mode)
    

