import gym_wapper
import gym


print('env anme:', 'gym_wapper/MCPDseEnv-v0')
env_ = gym.make('gym_wapper/MCPDseEnv-v0')
env_.reset()
for _ in range(5):
    act = env_.sample_act()
    next_obs, reward, done, info = env_.step(act)
    print('observation:{}, reward:{}, done:{}, info:{}'.format(next_obs, reward, done, info))