test = {
    'name': 'question 4.5',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(f.value(x=np.pi), 0.01335383513703555)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     f = F(a=1.0, w=0.1)
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
