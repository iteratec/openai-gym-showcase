import gym

SEED = 1730
MAX_STEPS = 500


if __name__ == "__main__":
    env = gym.make('CartPole-v0')
    env.seed(SEED)
    env.reset()

    env.render()
    input("Press Enter to continue...")

    for step in range(MAX_STEPS):
        action = env.action_space.sample()
        print('step {}: {}'.format(step, 'LEFT' if action == 0 else 'RIGHT'))

        observation, reward, done, _ = env.step(action)
        print('  observation: {}, reward: {}, done: {}'.format(observation, reward, done))
        if done:
            break

    env.render()
    input("Press Enter to continue...")

    env.close()
