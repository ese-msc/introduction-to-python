test = {
    'name': 'question 2.6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(approx_pi(4), 2.82842712474619)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(approx_pi(64), 3.1403311569547543)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     _x = [1, 2, 1, 1]
                     _y = [1, 1, 3, 1]
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
