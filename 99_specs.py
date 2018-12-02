import re
from gym import envs


def extract_name(spec):
    name = spec.id.split('-')[0]
    name = re.sub('Deterministic$', '', name)
    name = re.sub('NoFrameskip$', '', name)

    return name


if __name__ == "__main__":
    groups = {}
    for spec in envs.registry.all():
        group, env_name = spec._entry_point.split(':')
        if group not in groups:
            groups[group] = {}

        name = extract_name(spec)
        if name not in groups[group]:
            groups[group][name] = []

        groups[group][name].append(spec)

    for (group, spec_data) in groups.items():
        print(group)
        for (name, specs) in spec_data.items():
            print(' ', name)
            for spec in specs:
                print('   ', spec.id)
