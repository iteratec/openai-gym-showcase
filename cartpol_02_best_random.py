import gym

SEED = 1730
MAX_STEPS = 500


def reset(env):
    env.seed(SEED)
    env.reset()


def policy_best_random_steps(env):
    best_actions = []
    for _ in range(200):
        actions = random_steps(env)
        if len(actions) > len(best_actions):
            best_actions = actions[:]  # clone
            # print(len(actions))

    return best_actions


def random_steps(env):
    reset(env)

    actions = []
    for _ in range(MAX_STEPS):
        action = env.action_space.sample()
        actions.append(action)

        observation, reward, done, _ = env.step(action)
        if done:
            break

    return actions


if __name__ == "__main__":
    env = gym.make('CartPole-v0')
    best_actions = policy_best_random_steps(env)

    reset(env)
    print('best_actions:', len(best_actions))

    for idx, action in enumerate(best_actions):
        env.render()
        env.step(action)

    env.close()
