import sys
import wave
import json

class Test:
    def __init__(self, arr):
        self.arr = arr

def read_wav(path):
    with wave.open(path, "rb") as wav:
        nchannels, sampwidth, framerate, nframes, _, _ = wav.getparams()
        print(wav.getparams(), "\nBits per sample =", sampwidth * 8)

        signed = sampwidth > 1  # 8 bit wavs are unsigned
        byteorder = sys.byteorder  # wave module uses sys.byteorder for bytes

        values = []  # e.g. for stereo, values[i] = [left_val, right_val]
        for _ in range(nframes):
            frame = wav.readframes(1)  # read next frame
            channel_vals = []  # mono has 1 channel, stereo 2, etc.
            for channel in range(nchannels):
                as_bytes = frame[channel * sampwidth: (channel + 1) * sampwidth]
                as_int = int.from_bytes(as_bytes, byteorder, signed=signed)
                channel_vals.append(as_int)
            values.append(channel_vals[0])

    return values, framerate



data, rate = read_wav('./smoke_30s_mono.wav')
min = min(data)
min = min * -1
from_zero = []
for each in data:
    for_now = each + min
    from_zero.append(for_now)
true_max = max(from_zero)
as_floats = []
for these in from_zero:
    each_float = these / true_max
    as_floats.append(each_float)
as_nms = []
for float in as_floats:
    nm = float * 400 + 381
    as_nms.append(nm)
as_obj = { "data": as_nms }
with open("smoke_30s_mono_nm.json", "w") as j:
    json.dump(as_obj, j)    

# t = open("smoke_30s_mono_floats.txt", "a")
# for each in as_float:
#     # up = each[0]
#     t.write(str(each))
#     t.write(', ')
# t.close()
    
