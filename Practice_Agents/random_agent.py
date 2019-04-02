# ActionWrapper and Monitor 
import gym
import random

class RandomActionWrapper(gym.ActionWrapper):
  def __init__(self, env, epsilon=.5):
    super(RandomActionWrapper, self).__init__(env)
    self.epsilon = epsilon

  def action(self, action):
    if random.random() < self.epsilon:
      print('Random Move Performed')
    return action


if __name__ == "__main__":
  env = RandomActionWrapper(gym.make('CartPole-v0'))

  obs = env.reset()
  total_reward = 0.0

  while True:
    obs, reward, done, _ = env.step(0) # right move
    env.render()
    total_reward += reward

    if done:
      break

  print(f'Total reward: {total_reward}')
  env.close()
