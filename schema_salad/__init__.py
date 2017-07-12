from __future__ import absolute_import
import logging
import sys
import typing

__author__ = 'peter.amstutz@curoverse.com'

_logger = logging.getLogger("salad")
_logger.addHandler(logging.StreamHandler())
_logger.setLevel(logging.INFO)

import six
if six.PY3:
	from past import autotranslate
	autotranslate(['avro', 'avro.schema'])
