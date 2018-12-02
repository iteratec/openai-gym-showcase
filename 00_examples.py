import gym


def show_example(name):
    env = gym.make(name)
    env.reset()

    env.render()

    input("Press Enter to continue...")
    env.close()


if __name__ == "__main__":
    # box2d
    show_example('LunarLander-v2')

    # text
    show_example('Taxi-v2')

    # classic control
    show_example('CartPole-v1')

    # robotics (needs mujoco - physics simulation engine)
    # show_example('FetchPickAndPlace-v1')

    # atari
    show_example('SpaceInvaders-ram-v4')
