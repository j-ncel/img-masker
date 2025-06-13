from img_masker import mask


image_path = "samples/test_image.png"

mask(image_path).save("samples/1.png")

mask(
    image_path,
    mask_color="green",
    bg_color="black",
).save("samples/2.png")
