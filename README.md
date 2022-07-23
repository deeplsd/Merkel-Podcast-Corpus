# Merkel-Podcast-Corpus

![facing](https://user-images.githubusercontent.com/45385843/180602719-f73e9e2b-0648-4aaf-ba55-70df45e1179b.jpg)

This repository contains the files and code necessary to download the Merkel Podcast corpus.

There are following files presently in this repository:

- `corpus.xml`: This is an xml file containing the dates of the podcasts along with links to podcast video, subtitles and transcripts (if they exist).
- `timings.txt`: This file contains the duration and text information that can be used to crop the videos that have been downloaded and get the corresponding text for the cropped video. The file format is as follows:

```
podcast_date | start_duration | end_duration | text | how the snippet was obtained (force if obtained through forced alignment and srt if obtained through subtile file.)
```

We are working towards adding more details for the corpus. Stay tuned :)

### Try out our Angela Merkel speech synthesizer model using FastPitch TTS and Waveglow vocoder
[Colab Notebook](https://colab.research.google.com/drive/12foAOf2RyTt5-2NGhkCs5UYOnXre9d6G)
