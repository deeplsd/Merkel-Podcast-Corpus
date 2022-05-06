# Merkel-Podcast-Corpus

This repository contains the files and code necessary to download the Merkel Podcast corpus.

There are following files presently in this repository:

- `corpus.xml`: This is an xml file containing the dates of the podcasts along with links to podcast video, subtitles and transcripts (if they exist).
- `timings.txt`: This file contains the duration and text information that can be used to crop the videos that have been downloaded and get the corresponding text for the cropped video. The file format is as follows:

```
podcast_date | start_duration | end_duration | text | how the snippet was obtained (force if obtained through forced alignment and srt if obtained through subtile file.)
```

We are working towards adding more details for the corpus. Stay tuned :)
