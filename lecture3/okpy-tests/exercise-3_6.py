test = {
    'name': 'question 3.6',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(calc_material_velocity(*_m1), _v1)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(calc_material_velocity(*_m2), _v2)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(calc_material_velocity(*_m3), _v3)
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
                     _m1 = (44, 38, 2650)
                     _v1 = (6039.700938074968, 4074.772826171499)
                     _m2 = (6.85, 20.9, 2580)
                     _v2 = (3411.865600135066, 1629.4289673655376)
                     _m3 = (0, 2.29, 1000)
                     _v3 = (1513.2745950421556, 0.0)
                     import numpy as np
                     def sanity_check():
                         try:
                             calc_material_velocity(-6.85, 20.9, 2580)
                             return False
                         except ValueError:
                             pass
                         try:
                             calc_material_velocity(6.85, -20.9, 2580)
                             return False
                         except ValueError:
                             pass
                         try:
                             calc_material_velocity(6.85, 20.9, -2580)
                         except ValueError:
                             pass
                         return True""",
            'teardown': '',
            'type': 'doctest'
        }
    ]
}
