# Montreal Forced Aligner for G2P Vietnamese

Instruction for training two essential module in TTS for Vietnamese:

- G2P model: to extract phoneme for Vietnamese syllable, especially phonologize for OOV

- Acoustic model: to force align phoneme with waveform frames of audio (to align the acoustic features of the input audio with the corresponding phonemes in the transcription)

### Install

```
conda create -n aligner kaldi pynini python=3.11

conda activate aligner

conda install -c conda-forge montreal-forced-aligner
```

It may take 10 minutes to search for MFA

# MFA G2P Model

### Prepare phoneme dictionary

Prepare dictionary (txt file) with format with one sylablle for each line:

```<word><tab><phoneme>```

Please check example dictionaries in folder phoneme_dict: author provide two format of grapheme for Vietnamese in ARPAber and IPA

[Option] Reference phoneme_dict/generate_vidict.py if you want to make dictionary using IPA viphoneme

### Train G2P model

Check this doc: [Train a new G2P model](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/g2p_train.html)

```mfa train_g2p [OPTIONS] DICTIONARY_PATH OUTPUT_MODEL_PATH```

```mfa train_g2p phoneme_dict/viIPA.txt g2p_model/viIPA.zip```

### Align Inference

Check more option stdin/stdout: [Generate pronunciations for words](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/dictionary_generating.html)

- Run with file txt:

```mfa g2p [OPTIONS] INPUT_PATH G2P_MODEL_PATH OUTPUT_PATH```

```mfa g2p -n 1 DATA/input.txt g2p_model/viIPA.zip DATA/output.txt```

- Interact with i/o terminal:

```mfa g2p - g2p_model/viIPA.zip -```

- Generate with python script:

```python S01_g2p_infer.py```

# MFA Acoustic Model

*You must re-train acoustic model with your dataset, checkpoint model in this repo is example only*

### Train Acoustic model [Train a new acoustic model](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/train_acoustic_model.html)

```mfa train [OPTIONS] CORPUS_DIRECTORY DICTIONARY_PATH OUTPUT_MODEL_PATH```

```mfa train --config_path acoustic_model/config_test.yaml DATA/test_data phoneme_dict/viIPA.txt acoustic_model/viIPA.zip```

### Adaptive Acoustic Aligner in Case Voice Cloning / Speaker Adaptation [Adapt acoustic model to new data](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/adapt_acoustic_model.html)

Prepare data corpus following the format in "DATA/test_data/speaker_01"

```mfa adapt [OPTIONS] CORPUS_DIRECTORY DICTIONARY_PATH ACOUSTIC_MODEL_PATH OUTPUT_MODEL_PATH```

```mfa adapt --config_path acoustic_model/config_test.yaml DATA/test_data phoneme_dict/viIPA.txt acoustic_model/viIPA.zip acoustic_model/viIPA_adapt.zip```

### Infer/Force Align Model [Align with an acoustic model](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/alignment.html)

Align with dataset

```mfa align [OPTIONS] CORPUS_DIRECTORY DICTIONARY_PATH ACOUSTIC_MODEL_PATH OUTPUT_DIRECTORY```

```mfa align DATA/test_data/speaker_01 phoneme_dict/viIPA.txt acoustic_model/viIPA.zip DATA/test_aligned/speaker_01```

Align a single file

```mfa align_one [OPTIONS] SOUND_FILE_PATH TEXT_FILE_PATH DICTIONARY_PATH ACOUSTIC_MODEL_PATH OUTPUT_PATH```

```mfa align_one DATA/test_data/speaker_01/test_0.wav DATA/test_data/speaker_01/test_0.lab phoneme_dict/viIPA.txt acoustic_model/viIPA.zip DATA/test_aligned/test_0.TextGrid```

[Option] For more advancement in training and adaptation stage, check [MFA Configuration](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/configuration/index.html)

# Extract Duration Numpy

Reference on this: https://github.com/ming024/FastSpeech2/blob/master/preprocessor/preprocessor.py

```python S03_preprocess.py```