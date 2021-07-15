test = {
    'name': 'question 2.8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(h) == types.FunctionType
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(param) # wrong number of argument
                            1
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': 'import types; import inspect; param = inspect.signature(h).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(x)==np.ndarray
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(x, [-4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
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
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(y)==np.ndarray
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(y, [1.33830226e-04, 4.43184841e-03, 5.39909665e-02, 2.41970725e-01, 3.98942280e-01, 2.41970725e-01, 5.39909665e-02, 4.43184841e-03, 1.33830226e-04])
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
