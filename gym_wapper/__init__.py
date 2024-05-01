from gym.envs.registration import register

register(
    id="gym_wapper/MCPDseEnv-v0",
    entry_point="gym_wapper.envs:MCPDseEnv",
)