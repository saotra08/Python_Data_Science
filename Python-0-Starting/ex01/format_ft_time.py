import time
import datetime

seconds = time.time()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))
