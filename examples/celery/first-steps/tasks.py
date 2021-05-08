from celery import Celery

# Set celery initial settings using Redis as broker and as backend storage
app = Celery('tasks', backend='redis://localhost/', broker='redis://localhost/')

@app.task
def add(x, y):
    return x + y
