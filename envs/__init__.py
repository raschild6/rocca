from gym.envs.registration import register

register(
    id='Chase-v0',
    entry_point='envs.gym_chase:ChaseEnv',
)
