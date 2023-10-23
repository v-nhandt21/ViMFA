import viphoneme 
from viphoneme import vi2IPA_split

delimit =" "

f = open("vocab.txt", "r", encoding="utf-8")
fw = open("viPhoneme.txt", "w+", encoding="utf-8")

syllables = f.read().splitlines()

for syllable in syllables:
     phonemes = vi2IPA_split(syllable, delimit).replace(" .  .", "").replace("_", " ")
     if phonemes == "":
          print("Skip: ", syllable)
          continue
     fw.write(syllable + "\t" + phonemes + "\n")