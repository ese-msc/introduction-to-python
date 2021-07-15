test = {
    'name': 'question 1.14',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(even_numbers(11))==list
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(even_numbers(21), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
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
