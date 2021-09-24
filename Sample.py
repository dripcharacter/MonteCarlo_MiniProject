import ghalton
sequencer = ghalton.GeneralizedHalton(2, 68)
points = sequencer.get(1000)
print(points)