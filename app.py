from server import app
import os
import threading
from funcs.Platinum_plan import start_measuring

thread1 = threading.Thread(target = start_measuring)
thread1.start()

PORT = int(os.environ.get('PORT', 3000))
app.run(host='0.0.0.0', port=PORT)
