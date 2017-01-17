import alsaaudio, sys, time, subprocess
m = alsaaudio.Mixer()   # defined alsaaudio.Mixer to change volume

t = int(sys.argv[1])*60
vol = m.getvolume()[0]
print vol
dt = t/vol

for i in xrange(vol, 0, -1):
    m.setvolume(i)
    time.sleep(dt)

subprocess.call(["pm-hibernate"])
