# Merkel-Podcast-Corpus

![facing](https://user-images.githubusercontent.com/45385843/180602719-f73e9e2b-0648-4aaf-ba55-70df45e1179b.jpg)

**This repository contains the files and code necessary to download the Merkel Podcast corpus.**

## Quick Setup
```
git clone https://github.com/deeplsd/Merkel-Podcast-Corpus.git
cd Merkel-Podcast-Corpus
python download_video.py
python crop_snippets.py
```

## Directory Structure
```
Merkel-Podcast-Corpus/
├── README.md
├── corpus
│   ├── date
│   │   ├── audio.wav
│   │   ├── video.mp4
│   │   └── snippets
│   │       └── date_id
│   │           ├── snippet.mp4
│   │           └── text.txt
├── corpus.xml
├── crop_snippets.py
├── download_video.py
└── timings.txt
```
`corpus/` directory is created after setup. It contains full podcasts and snippets.
  
There are following files presently in this repository:

- `corpus.xml`: This is an xml file containing the dates of the podcasts along with links to podcast video, subtitles and transcripts (if they exist).
- `timings.txt`: This file contains the duration and text information that can be used to crop the videos that have been downloaded and get the corresponding text for the cropped video. The file format is as follows:

```
podcast_date | start_duration | end_duration | text | how the snippet was obtained (force if obtained through forced alignment and srt if obtained through subtile file.)
```
- `download_video.py`: Python script that downloads podcasts listed in the XML file.
- `crop_snippets.py`: Python script the crops video-snippets from full podcasts using durations provided in `timings.txt`

We are working towards adding more details about our downstream preprocessing. Stay tuned :)


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
