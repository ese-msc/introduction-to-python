test = {
    'name': 'question 1.7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(gaussian) == types.FunctionType
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': False,
            'setup': 'import types',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> len(param)
                            3
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[0][0]].name
                            'x'
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[0][0]].default
                            <class 'inspect._empty'>
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[1][0]].name
                            'm'
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[1][0]].default
                            0
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[2][0]].name
                            's'
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> param[lparam[2][0]].default
                            1
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': """
                     import inspect;
                     param = inspect.signature(gaussian).parameters
                     lparam = list(param.items())
                     """,
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(gaussian(0.5), 0.3520653267642995)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(gaussian(1), 0.24197072451914337)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(gaussian(1,1,2), 0.19947114020071635)
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
