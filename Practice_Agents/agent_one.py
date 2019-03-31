"""
This is a basic Agent/Enviroment script that acts at random. 

To learn more about this script go to the appropriate jupyter notebook
"""
import random
from tqdm import tqdm, trange
import time

class Environment:
  def __init__(self):
    self.steps_left = 100

  def get_observation(self):
    return [0.0, 0.0, 0.0]

  def get_actions(self):
    return [0,1]

  def is_done(self):
    return self.steps_left == 0

  def action(self, action):
    if self.is_done():
      raise Exception('Game is over')

    self.steps_left -= 1
    return random.random() # returns a random float


class Agent:
  def __init__(self):
    self.total_reward = 0.0

  def step(self, env):
    current_obs = env.get_observation()
    actions = env.get_actions()
    reward = env.action(random.choice(actions))
    self.total_reward += reward


# Initializing game
if __name__ == "__main__":
  env = Environment()
  agent = Agent()

  while not env.is_done():
    for i in trange(env.steps_left, desc="Training Agent"):
      agent.step(env)
      time.sleep(.05) # sleeping for 100 miliseconds
      tqdm.write(f'Iteration: {i+1}, Total Reward: {agent.total_reward}')