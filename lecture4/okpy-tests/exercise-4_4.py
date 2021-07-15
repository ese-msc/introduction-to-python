test = {
    'name': 'question 4.4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> sorted(list(densities_join.keys()))
                            ['Earth_core', 'Earth_mean', 'Moon', 'Sun_core', 'Sun_mean', 'air', 'gasoline', 'gold', 'granite', 'human_body', 'ice', 'iron', 'limestone', 'mercury', 'platinium', 'proton', 'pure_water', 'seawater', 'silver']
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len([1 for k in densities_join if k in densities_substrings and densities_join[k]==densities_substrings[k]]) == len(densities_join)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': "f='data/densities.dat';densities_join=read_densities_join(f);densities_substrings=read_densities_substrings(f)",
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
