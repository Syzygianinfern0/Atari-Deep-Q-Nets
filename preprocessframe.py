import cv2


def pre_process(frame):
    gray_frame = cv2.imread(frame, 0)
    cropped_frame = gray_frame[8:-12, 4:-12]
    normalised_frame = cropped_frame / 255.0
    perfect_frame = cv2.resize(normalised_frame, [110, 84])
    return perfect_frame
