test = {
    'name': 'question 4.7',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> account.balance == 250
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> account.transactions == 10
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': """
                     account = Account("Test", 1, 100)
                     for i in range(5):
                         account.deposit(50)
                         account.withdraw(20)
                     """,
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
