test = {
    'name': 'question 4.1',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> len([1 for k in d1 if k in d2 and d1[k]==d2[k]]) == len(d2)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': "d1 = read_constants('data/constants.txt'); d2 = {'gravitational constant': 6.67259e-11, 'Boltzmann constant': 1.380658e-23, 'speed of light': 299792458.0, 'Planck constant': 6.6260755e-34, 'electron mass': 9.1093897e-31, 'Avogadro number': 6.0221367e+23, 'elementary charge': 1.60217733e-19, 'proton mass': 1.6726231e-27}",
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
