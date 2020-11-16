import time
from myapp import app


@app.task
def vid0():
    time.sleep(5)
    return 'video aux done'
