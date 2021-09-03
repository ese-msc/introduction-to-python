test = {
    'name': 'question 3.9',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> isinstance(time_array, np.ndarray)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> time_array.shape
                            (101,)
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> time_array[0] == 0.
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> time_array[1] == 0.5
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> time_array[-2] == 49.5
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> time_array[-1] == 50
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> isinstance(acc_array, np.ndarray)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> acc_array.shape
                            (101,)
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(acc_array[0], -0.00506375204384)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(acc_array[1], 0.00500006128645)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(acc_array[-2], 0.495000061286)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(acc_array[-1], 0.479565276825)
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.isclose(compute_velocity(2, 10, acc_array), 0.69115419125176)
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
