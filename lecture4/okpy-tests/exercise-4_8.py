test = {
    'name': 'question 4.8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(l.value(0.5), 0.25)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> lNone.value(0.5)==None
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     l = Line([0, 0], [1, 0.5])
                     lNone = Line([0, 0], [0, 0])
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
