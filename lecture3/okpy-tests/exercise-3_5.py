test = {
    'name': 'question 3.5',
    'points': 1,
    'suites': [
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
                {
                    'code': r"""
                            >>> sanity_check()
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     import math
                     def sanity_check():
                         try:
                             my_factorial(-7)
                         except ValueError:
                             return True
                         return False
                      """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
