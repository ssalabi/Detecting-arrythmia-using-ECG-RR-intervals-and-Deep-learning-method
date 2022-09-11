import numpy as np


SAMPLE_RATE = 0.004  # ms

# normal rr length 0.6 to 1.2 sec : 50 - 100 hr
MAX_RATE_IN_SAMPLES = 1.2 / SAMPLE_RATE
#print(MAX_RATE_IN_SAMPLES) # above that is lower than 50 hr bpm
MIN_RATE_IN_SAMPLES = 0.6 / SAMPLE_RATE
#print(MIN_RATE_IN_SAMPLES) # below that is higher than 100 hr bpm
# normal range of interval length in samples is 150-300


def samples_length_to_hr(length):
    return 60.0 / (length * SAMPLE_RATE)


def hr_to_seconds_interval(hr):
    return 60.0 / hr


def samples_length_to_array(lengths):
    f = np.vectorize(samples_length_to_hr)
    return f(lengths)



h = hr_to_seconds_interval(50)
#print(h / SAMPLE_RATE)

h = hr_to_seconds_interval(200)
#print(h / SAMPLE_RATE)