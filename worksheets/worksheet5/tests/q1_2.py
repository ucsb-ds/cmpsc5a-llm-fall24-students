OK_FORMAT = True

test = {   'name': 'q1_2',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> import numpy as np\n>>> type(book_title_words) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> not any([',' in text for text in book_title_words])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> 'and ' in book_title_words.item(2)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> len(book_title_words) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> book_title_words.item(0) == 'Eats'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> book_title_words.item(1) == 'Shoots'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> book_title_words.item(2) == 'and Leaves'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
