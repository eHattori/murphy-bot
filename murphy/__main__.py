import signal
import sys
import threading
from trading import main, stop

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        signal.signal(signal.SIGINT, stop)
        forever = threading.Event()
        forever.wait()
        sys.exit(0)

