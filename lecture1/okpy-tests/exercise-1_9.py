test = {
    'name': 'question 1.9',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(P_earth, 31603718.929927427)
                            True
                            >>> np.allclose(P_mars, 58059817.3950661)
                            True
                            >>> np.allclose(birthdays, 18.3711978719333)
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
