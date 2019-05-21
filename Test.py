import gym
import cv2

env = gym.make('SpaceInvaders-v0')
env.reset()
for _ in range(3000):
    observation, reward, done, info = env.step(env.action_space.sample())
    cv2.imshow('obs', observation)
    env.render('human')
env.close()
cv2.destroyAllWindows()
