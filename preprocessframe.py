import gym
import cv2

def preprocess_frame(frame):
    # Greyscale frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Crop the screen (remove the part below the player)
    cropped_frame = gray[8:-12, 4:-12]

    # Normalize Pixel Values
    normalized_frame = cropped_frame / 255

    # Resize
    preprocessed_frame = cv2.resize(normalized_frame, (110, 84))
    return preprocessed_frame  # 110x84x1 frame


import cv2

env = gym.make('SpaceInvaders-v0')
env.reset()
for i in range(3000):
    observation, reward, done, info = env.step(env.action_space.sample())
    cv2.imshow('test', observation)
    if i == 100:
        obs1 = observation
    env.render('human')
env.close()
cv2.destroyAllWindows()

cv2.imshow('processed', preprocess_frame(obs1))

cv2.waitKey()
cv2.destroyAllWindows()
