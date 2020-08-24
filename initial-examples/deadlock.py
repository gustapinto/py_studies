import threading

""" Forcing a simple and harmless deadlock
    Tip: if the process remain open, it deadlocked
"""

# Initialize the multithread process
lock = threading.Lock()

print("Printed before first acquire")
lock.acquire()  # Decrease the default Python semaphore counter

print("Printed before second acquire")
lock.acquire()  # If you doesn't want the lock comment this line ...
# lock.release()  # And uncomment this line (this increase the counter)

# Print 'Success' if nothing goes wrong
# Spoiler: things will go wrong ;D
print("Success")
