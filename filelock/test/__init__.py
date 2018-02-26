from filelock.filelock import FileLock, FileLockException


lock1 = FileLock("test.json")
lock2 = FileLock("test.json")

lock1.acquire()
assert lock1.is_locked

lock1.release()
assert not lock1.is_locked

lock2.acquire()
assert lock2.is_locked
lock2.release()
assert not lock2.is_locked

lock1.acquire()
try:
    lock2.acquire()
except FileLockException:
    pass

lock2.release(force_release=True)
lock2.acquire()

lock1.release()
lock2.release()

pass