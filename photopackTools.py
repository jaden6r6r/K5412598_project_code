from queue import Full
import fitz

# doc = fitz.open("test.pdf")

# for page in doc:
#     for image in page.get_images():
#         img = doc.extract_image(image[0])
#         with open("./img/{}.png".format(image[0]), "wb") as binary_file:
#             # Write bytes to file
#             binary_file.write(img["image"])


class PhotopackTools:
    def __init__(self):
        pass

    def deconstruct(self, path):
        """
        This method will accept a path to a .pdf file (the photopack) and will iterate through the pages, extracting all images before saving them in a /img/ directory.
        """
        doc = fitz.open(path)
        for page in doc:
            page.clean_contents()
            for image in page.get_images():
                img = doc.extract_image(image[0])
                with open("./img/{}.png".format(image[0]), "wb") as binary_file:
                    # Write bytes to file
                    binary_file.write(img["image"])

    def construct(self, path, dir=None):
        """
        This method is to be used at the end of the process, it accepts a path to a pdf as well as a directory as an argument and will reconstruct the original .pdf with the images output from the blurring stage.
        """
        # get the bounding box for each image.
        doc = fitz.open(path)
        for page in doc:
            # As per the docs - I need to call clean_contents() method to remove 'dead' image entries.
            page.clean_contents()
            for image in page.get_images(full=True):
                # Get the bounding box (bbox) coordinates for each of the images in the page, printing the xref and the bbox coords for each
                bbval = page.get_image_bbox(image)
                print(image[0], bbval)
                # for each image (each iteration) replace the image using the bbox and the xref getting the xref+'_edit' file as the replacement
                page.insertImage(
                    bbval,
                    filename="./img/complete/{}_edit.png".format(image[0]),
                    keep_proportion=False,
                )
        doc.save("./output.pdf")
        doc.close()


# pt = PhotopackTools()
# pt.construct("test.pdf")
