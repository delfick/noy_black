from noy_black import VERSION
from setuptools import setup

# fmt: off
setup(
      name = 'noy_black'
    , version = VERSION
    , packages = ["noy_black"]

    , python_requires = ">= 3.6"

    , install_requires =
      [ 'black'
      , 'noseOfYeti>=1.9.1'
      ]

    , entry_points =
      { 'console_scripts' :
        [ 'noy_black = noy_black.main:main'
        ]
      }

    , author = 'Stephen Moore'
    , license = 'MIT'
    , author_email = 'delfick755@gmail.com'

    , url = "https://github.com/delfick/noy_black"
    , description = 'Monkey patched black that understands nose of yeti'
    , long_description = open("README.rst").read()
    )
# fmt: on
