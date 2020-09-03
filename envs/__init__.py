from envs.Gomoku import Gomoku
from gym.envs.registration import register

register(
  id='Gomoku-v0',
  entry_point='envs:Gomoku',
)
