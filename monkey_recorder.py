from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner.recorder import MonkeyRecorder as recorder
device = mr.waitForConnection(5,"021YLJ4C35002735")
recorder.start(device)