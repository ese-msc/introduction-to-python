test = {
    'name': 'question 2.10',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(A, [[0, 12, -1], [-1, -1, -1], [11, 5, 5]])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(A) == np.ndarray
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(b, [-2, 1, 7])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(b) == np.ndarray
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

        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(c, [5., -6., 18.])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(c) == np.ndarray
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
