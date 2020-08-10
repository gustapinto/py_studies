from __future__ import absolute_import, unicode_literals

from celery import Celery

app = Celery('next-steps',
             broker='redis://localhost/',
             backend='redis://localhost/',
             include=['next-steps.tasks'])


app.conf.update(result_expires=3600)

if __name__ == "__main__":
    app.start()
