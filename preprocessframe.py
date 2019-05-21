from skimage import transform
from skimage.color import rgb2gray
from skimage import io


# def pre_process(frame):
#     gray_frame = rgb2gray(frame)
#     # cropped_frame = gray_frame[8:-12, 4:-12]
#     # normalised_frame = cropped_frame / 255.0
#     # perfect_frame = transform.resize(normalised_frame, [110, 84])
#     return gray_frame
def pre_process(frame):
    # Greyscale frame
    gray = rgb2gray(frame)

    # Crop the screen (remove the part below the player)
    # [Up: Down, Left: right]
    cropped_frame = gray[8:-12, 4:-12]

    # Normalize Pixel Values
    normalized_frame = cropped_frame / 255.0

    # Resize
    # Thanks to Mikołaj Walkowiak
    preprocessed_frame = transform.resize(normalized_frame, [110, 84])

    io.imshow(preprocessed_frame)
    io.show()
