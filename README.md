# Merkel-Podcast-Corpus

![facing](https://user-images.githubusercontent.com/45385843/180602719-f73e9e2b-0648-4aaf-ba55-70df45e1179b.jpg)

This dataset is presented in the paper ***Merkel Podcast Corpus: A Multimodal Dataset Compiled from 16 Years of Angela Merkel's Weekly Video Podcasts*** published at LREC 2022 [(Paper)](https://arxiv.org/abs/2205.12194). 

## Quick Setup
### Download
```
git clone https://github.com/deeplsd/Merkel-Podcast-Corpus.git
cd Merkel-Podcast-Corpus
python download_video.py
```
### Extract Snippets
> Raw snippets might contain multiple speakers. For single-speaker corpus, please refer below.
```
python crop_snippets.py
```
### Extract Single-speaker Snippets
> These operations can be used to extract face-cropped video-clips containing only Angela Merkel.
```
cd ..
git clone https://github.com/Debjoy10/preprocess_Merkel.git
conda install -c conda-forge face_recognition
pip install -r requirements.txt
bash run_with_timings.sh
```

## Directory Structure
```
┌── Merkel-Podcast-Corpus
│   ├── README.md
│   ├── corpus
│   │   └── date
│   │       ├── audio.wav
│   │       ├── video.mp4
│   │       └── snippets
│   │           └── date_id
│   │               ├── snippet.mp4
│   │               └── text.txt
│   ├── corpus.xml
│   ├── crop_snippets.py
│   ├── download_video.py
│   └── timings.txt
│
├── Merkel_Single_Speaker
│   ├── date_id
│   │   ├── date_id.avi
│   │   ├── date_id_lips.avi
│   │   ├── audio.wav
│   │   ├── highpassaudio.wav
│   │   └── text.txt
│   ├── metadata.csv
│   ├── metadata_train.csv
│   └── metadata_val.csv
│
└── preprocess_Merkel
```

- `Merkel-Podcast-Corpus/timings.txt`: This file contains the duration and text information that can be used to crop the videos that have been downloaded and get the corresponding text for the cropped video. The file format is as follows:
```
podcast_date | start_duration | end_duration | text | how the snippet was obtained (force if obtained through forced alignment and srt if obtained through subtile file.)
```
- `Merkel-Podcast-Corpus/corpus/` directory is created after setup. It contains full podcasts and (uncropped multi-speaker) snippets (video and audio files).
- `Merkel_Single_Speaker/` directory contains all face-cropped single-speaker snippets (face-cropped videos, lip-cropped videos, audio and text files).


### Try out our Angela Merkel speech synthesizer!
> Built using FastPitch TTS and Waveglow vocoder  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Debjoy10/FastPitch_demo/blob/main/Merkel_Corpus_FastPitch_Demo.ipynb)
[![Open In Github](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Debjoy10/FastPitch_demo/blob/main/Merkel_Corpus_FastPitch_Demo.ipynb)

## Citation

Please cite our work if you use our code or data.

```
@article{saha2022merkel,
  title={Merkel Podcast Corpus: A Multimodal Dataset Compiled from 16 Years of Angela Merkel's Weekly Video Podcasts},
  author={Saha, Debjoy and Nayak, Shravan and Baumann, Timo},
  journal={arXiv preprint arXiv:2205.12194},
  year={2022}
}
```
