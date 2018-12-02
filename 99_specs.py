from gym import envs


def print_spec(spec):
    print('{} ({})'.format(spec.id, spec._entry_point))


if __name__ == "__main__":
    specs = {}
    for spec in envs.registry.all():
        if spec not in specs:
            specs[spec._env_name] = spec

    groups = {}
    for spec in specs.values():
        group = spec._entry_point.split(':')[0]
        if group not in groups:
            groups[group] = []
        groups[group].append(spec.id)

    for (key, spec_ids) in groups.items():
        print(key)
        for spec_id in spec_ids:
            print(' ', spec_id)
