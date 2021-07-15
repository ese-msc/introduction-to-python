test = {
    'name': 'question 1.16',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(distances_list)==list
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': 'distances_list=distance(0.1, 0.6, 6)',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(distance(0.1, 0.6, 6), [0.55095, 1.0038, 1.3585500000000001, 1.6152000000000002, 1.77375, 1.8341999999999996])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(distance(1, 6, 5, 3), [-1.9050000000000002, -18.0815625, -49.58625, -96.41906250000001, -158.58])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': 'import numpy as np',
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
