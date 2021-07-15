test = {
    'name': 'question 2.12',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(C, np.array([[ 34.,  -3.,  67.], [ -3.,  -4., -18.],[  3.,  26., 132.]]))
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(C) == np.ndarray
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
