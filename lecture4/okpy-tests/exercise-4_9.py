test = {
    'name': 'question 4.9',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(sorted(q.roots()), [-4.7912878474779195, -0.20871215252208009])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     q = Quadratic(a=1, b=5, c=1)
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
