from montreal_forced_aligner.g2p.generator import (
    PyniniConsoleGenerator
)

g2p_model_path = "g2p_model/viIPA.zip"

g2p = PyniniConsoleGenerator(g2p_model_path=g2p_model_path)
g2p.setup()

sentence ="thời gian địa điểm rõ ràng"
delimit = "/"
space = " "

sequence = ""
for word in sentence.split():
    phoneme = g2p.rewriter(word)[0].split()
    phoneme = delimit.join(phoneme)
    sequence += phoneme + space

print(sequence)


# https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/issues/653