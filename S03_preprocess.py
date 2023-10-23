import os
import tgt
import numpy as np

sampling_rate = 22050
hop_length = 256

def get_alignment(tier):
     sil_phones = ["sil", "sp", "spn"]

     phones = []
     durations = []
     start_time = 0
     end_time = 0
     end_idx = 0
     for t in tier._objects:
          s, e, p = t.start_time, t.end_time, t.text

          # Trim leading silences
          if phones == []:
               if p in sil_phones:
                    continue
               else:
                    start_time = s

          if p not in sil_phones:
               # For ordinary phones
               phones.append(p)
               end_time = e
               end_idx = len(phones)
          else:
               # For silent phones
               phones.append(p)

          durations.append(
               int(
               np.round(e * sampling_rate / hop_length)
               - np.round(s * sampling_rate / hop_length)
               )
          )

     # Trim tailing silences
     phones = phones[:end_idx]
     durations = durations[:end_idx]

     return phones, durations, start_time, end_time

if __name__ == "__main__":
     wav_path = "DATA/test_data/speaker_01/test_0.wav"
     text_path = os.path.join("DATA/test_data/speaker_01/test_0.lab")
     tg_path = os.path.join("DATA/test_aligned/speaker_01/test_0.TextGrid")

     dur_filename = "DATA/duration/speaker_01/test_0.npy"

     textgrid = tgt.io.read_textgrid(tg_path)
     phone, duration, start, end = get_alignment(
               textgrid.get_tier_by_name("phones")
          )

     text = "{" + " ".join(phone) + "}"
     duration = np.array(duration)

     print(text)
     print(duration.shape)

     np.save(dur_filename, duration)