test = {
    'name': 'question 1.17',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(my_cumsum([1, 4, 2, 5, 3]), [1, 5, 7, 12, 15])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(my_cumsum([2.4, 5.2, 4.7, 9.3]), [2.4, 7.6, 12.3, 21.6])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': 'import numpy as np',
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
