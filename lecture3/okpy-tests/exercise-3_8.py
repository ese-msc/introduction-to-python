test = {
    'name': 'question 3.8',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> x
                            [-10.0, -5.0, 0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0]
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> y
                            [1.341, 1.316, 1.293, 1.269, 1.247, 1.225, 1.204, 1.184, 1.164]
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> temp_air_list == x and dens_air_list == y
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': 'x, y = readTempDenFile("data/density_air.dat")',
            'teardown': "",
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                            >>> x
                            [0.0, 4.0, 15.0, 20.0, 25.0, 37.0, 50.0, 100.0]
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> y
                            [999.8425, 999.975, 999.1026, 998.2071, 997.0479, 993.3316, 988.04, 958.3665]
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> temp_water_list == x and dens_water_list == y
                            True
                            """,
                    'hidden': False,
                    'locked': False
                }
            ],
            'scored': True,
            'setup': 'x, y = readTempDenFile("data/density_water.dat")',
            'teardown': "",
            'type': 'doctest'
        }
    ]
}
