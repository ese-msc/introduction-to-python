test = {
    'name': 'question 2.5',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(path_length) == types.FunctionType
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(param) # wrong number of argument
                            2
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': False,
            'setup': 'import types; import inspect; param = inspect.signature(path_length).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.isclose(path_length(_x, _y), 5.23606797749979)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(path_length(_x2, _y2), 6.39834563766817)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import numpy as np
                     _x = [1, 2, 1, 1]
                     _y = [1, 1, 3, 1]
                     _x2 = [1, 2, 1, 2]
                     _y2 = [1, 1, 3, 6]
                    """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
