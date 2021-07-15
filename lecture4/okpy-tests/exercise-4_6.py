test = {
    'name': 'question 4.6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> s1.i==64
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> s2.i=='HelloHelloHelloHello'
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': """
                     s1 = Simple(4)
                     for i in range(4):
                         s1.double()

                     s2 = Simple('Hello')
                     for i in range(2):
                         s2.double()
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
