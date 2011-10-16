# composer/writer.py
# Copyright 2011 Andrey Petrov
#
# This module is part of Composer and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php


import os
import logging


log = logging.getLogger(__name__)


class Writer(object):
    """
    :param base_path:
        Base filesystem path for where the static HTML structure should be
        created.
    """
    def __init__(self, base_path):
        self.base_path = base_path

        try:
            os.makedirs(base_path)
        except os.error:
            pass # Already exists, honeybadger doesn't care.


    def manifest_url(self, url, content, index_file='index.html'):
        url_path = os.path.join(self.base_path, url)

        try:
            os.makedirs(url_path)
        except os.error:
            pass # Already exists, honeybadger doesn't care.

        fp = open(os.path.join(url_path, index_file), 'w')
        fp.write(content)
        fp.close()


    def __call__(self, router):

        for url, content in router:
            log.info("Writing url: ", url)
            self.manifest_url(url, content)


