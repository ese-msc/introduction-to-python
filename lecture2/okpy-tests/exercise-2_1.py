test = {
    'name': 'question 2.1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(mult([1, 2, 3, -6], 3), [3, 6, 9, -18])
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
