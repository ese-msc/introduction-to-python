test = {
    'name': 'question 2.2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                            >>> len(tlist)
                            11
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(tlist, [0.0, 0.02038735983690112, 0.04077471967380224, 0.06116207951070336, 0.08154943934760447, 0.1019367991845056, 0.12232415902140673, 0.14271151885830785, 0.16309887869520895, 0.18348623853211007, 0.2038735983690112])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(ylist, [0.0, 0.018348623853211007, 0.03261977573904179, 0.04281345565749235, 0.04892966360856269, 0.0509683995922528, 0.048929663608562685, 0.04281345565749235, 0.03261977573904182, 0.018348623853211038, 0.0])
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(displacement)
                            2
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(displacement[0])==list
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(displacement[0])
                            11
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> type(displacement[1])==list
                            True
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> len(displacement[1])
                            11
                            """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                            >>> np.allclose(displacement, [[0.0, 0.02038735983690112, 0.04077471967380224, 0.06116207951070336, 0.08154943934760447, 0.1019367991845056, 0.12232415902140673, 0.14271151885830785, 0.16309887869520895, 0.18348623853211007, 0.2038735983690112], [0.0, 0.018348623853211007, 0.03261977573904179, 0.04281345565749235, 0.04892966360856269, 0.0509683995922528, 0.048929663608562685, 0.04281345565749235, 0.03261977573904182, 0.018348623853211038, 0.0]])
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
