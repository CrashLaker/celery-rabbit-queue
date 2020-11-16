import time
from myapp import app


@app.task
def img0():
    time.sleep(5)
    return 'image aux done'
