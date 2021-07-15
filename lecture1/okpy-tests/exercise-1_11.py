test = {
    'name': 'question 1.11',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(num_digits(5), 1)
                            True
                            >>> np.isclose(num_digits(555), 3)
                            True
                            >>> np.isclose(num_digits(555555), 6)
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
