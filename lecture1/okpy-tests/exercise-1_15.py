test = {
    'name': 'question 1.15',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> type(my_sum) == types.FunctionType
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(param)
                            1
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': False,
            'setup': 'import inspect, types; param = inspect.signature(my_sum).parameters',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> my_sum(_x) == sum(_x)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': 'import types; import random; _x = random.sample(range(1, 100), 6)',
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
