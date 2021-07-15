test = {
    'name': 'question 2.13',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> np.allclose(odd, [ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19., 21., 23., 25., 27., 29., 31., 33., 35., 37., 39., 41., 43., 45., 47., 49., 51., 53., 55.])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(odd_sq, [[ 1.,  3.,  5.,  7.,  9., 11., 13.],[15., 17., 19., 21., 23., 25., 27.],[29., 31., 33., 35., 37., 39., 41.],[43., 45., 47., 49., 51., 53., 55.]])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(odd_bits, [[17., 21., 25.],[31., 35., 39.]])
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
