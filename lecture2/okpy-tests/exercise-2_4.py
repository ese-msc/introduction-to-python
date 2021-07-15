test = {
    'name': 'question 2.4',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(my_factorial) == types.FunctionType
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
            'setup': 'import types; import inspect; param = inspect.signature(my_factorial).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> my_factorial(0)==math.factorial(0)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> my_factorial(1)==math.factorial(1)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> my_factorial(42)==math.factorial(42)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': 'import math',
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
