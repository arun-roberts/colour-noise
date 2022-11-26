import sys
import wave
import json
import colorsys

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



data, rate = read_wav('./smoke_12k.wav')
print(len(data))
min = min(data)
min = min * -1
from_zero = []
for each in data:
    for_now = each + min
    from_zero.append(for_now)
true_max = max(from_zero)
as_rgb = []
for these in from_zero:
    each_float = these / true_max
    hsl_float = each_float * 300 / 360
    rgb_floats_tuple = colorsys.hls_to_rgb(hsl_float, 0.5, 1)
    rgb_string = ''
    for e in rgb_floats_tuple:
        rgb_value = round(e * 255)
        holder = rgb_string + str(rgb_value) + ","
        rgb_string = holder
    as_rgb.append(rgb_string.rstrip(',') + ';')
t = open("smoke_12k_full_rgb.txt", "a")
for each in as_rgb:
    t.write(each)
t.close()
    

# as_nms = []
# as_hues = []
# for float in as_floats:
#     hue = round(float * 270, 1)
#     as_hues.append(hue)
    # nm = float * 400 + 381
    # as_nms.append(nm)
# as_obj = { "data": as_nms }
# as_obj = { "data": as_hues }
# with open("smoke_12k_full.js", "w") as j:
#     json.dump(as_hues, j)    