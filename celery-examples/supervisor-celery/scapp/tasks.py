from __future__ import absolute_import, unicode_literals

from .celery import app

@app.task
def add(n1, n2):
    return n1 + n2
