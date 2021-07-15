test = {
    'name': 'question 2.11',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(f_cubic) == types.FunctionType
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
            'scored': False,
            'setup': 'import types, inspect; param = inspect.signature(f_cubic).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(f_cubic(A33), f_A33)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     A33 = np.array([[0,  12, -1],
                                   [-1, -1, -1],
                                   [11,  5,  5]], dtype=np.float32)
                     f_A33 = np.array([[ 1.0000000e+00,  1.9547865e+06, -3.6787939e-01],
                                       [-3.6787939e-01, -3.6787939e-01, -3.6787939e-01],
                                       [ 6.5994756e+05,  8.6806580e+02,  8.6806580e+02]])
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
