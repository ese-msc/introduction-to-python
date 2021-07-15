test = {
    'name': 'question 2.3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(heaviside) == types.FunctionType
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
            'setup': 'import types; import inspect; param = inspect.signature(heaviside).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(heaviside(-0.5), 0)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(heaviside(0), 1)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(heaviside(0.5), 1)
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
