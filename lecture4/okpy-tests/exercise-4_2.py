test = {
    'name': 'question 4.2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> t1 = {'dog': 'Hund', 'cat': 'Katze', 'house': 'Haus', 'bicycle': 'Fahrrad'}
                            >>> assert reverse_dict(t1) == {'Hund': 'dog', 'Katze': 'cat', 'Haus': 'house', 'Fahrrad': 'bicycle'}
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
