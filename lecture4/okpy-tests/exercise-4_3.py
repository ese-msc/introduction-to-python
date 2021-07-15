test = {
    'name': 'question 4.3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(triangle_area({1: (0,0), 2: (1,0), 3: (0,2)}), 1.)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(triangle_area({1: (0,0), 2: (2,1), 3: (0,3)}), 3.)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(triangle_area({1: (0,0), 2: (1,0), 3: (0,1)}), 0.5)
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
