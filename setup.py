from setuptools import setup

requires = [
    'pyramid',
]

setup(name='src',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)
