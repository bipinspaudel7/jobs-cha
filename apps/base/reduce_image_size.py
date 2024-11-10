from io import BytesIO

from django.core.files import File

from PIL import Image


def reduce_image_size(photo, quality):
    image = Image.open(photo)
    image_io = BytesIO()
    if image.size[0] > 500:
        image.thumbnail((500, 500))
    image.save(
        image_io, quality=quality, format="JPEG" if image.mode == "RGB" else "PNG"
    )
    image_io.seek(0)
    return File(image_io, name=photo.name)
