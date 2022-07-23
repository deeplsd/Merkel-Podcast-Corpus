#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
import os 
import urllib.request as urlRequest
import subprocess

# usage: ./download.py [some-file.xml] [some-path]
#        for existing some-file.xml file
#        if no file given, the script will try to use './corpus.xml'
#        for each 'entry' in the .xml file, the script will download the given media 

#        for existing some-path (if given, some-file.xml must also be given)
#        if no path given or the given path does not exist, the script will try to use ./corpus or create a directory ./corpus if ./corpus does not exist
#        for each 'entry' in the .xml file, the script will store the downloaded media in a directory <some-path>/<entry.id> as <media-type>.<file extension>

def main(corpus_xml='corpus.xml', corpus_path='./corpus'):
   try:
      # try opening given .xml file
      corpus_file = open(corpus_xml, 'r')
      corpus_file.close()

      # try parsing given .xml file
      corpus = ET.parse(corpus_xml)
      root = corpus.getroot()

      #/ try reading given path
      if not os.path.exists(corpus_path):
         print('This path does not exist. Creating {}'.format(corpus_path))
         os.mkdir(corpus_path)

   except FileNotFoundError:
      print('This file does not exist. Please use an existing file or run ./scraping.py to obtain one.')
      sys.exit()

   except ET.ParseError:
      print('This file does not seem to have the correct format. Please run ./scraping.py to obtain a valid .xml file.')
      sys.exit()

   # get number of podcasts 
   total_podcasts = int(root[1][1].text)

   # download media per podcast entry in given .xml file and store in given path/<entry.id>
   for entry in root.iter('entry'):
      print('now on {0} of {1}'.format(entry.get('podcast_num'), total_podcasts))
      
      entry_path = '{0}/{1}'.format(corpus_path, entry.get('id'))
      
      # try opening path for current entry 
      if os.path.exists(entry_path):
         continue
      
      print('Creating {}'.format(entry_path))
      os.mkdir(entry_path)

      # get media links for current entry from .xml file
      video_link = entry.find('video').text

      # download media files. This will create audio and video files in the folder.
      if video_link:
         urlRequest.urlretrieve(video_link, entry_path + '/video.mp4')
         command = 'ffmpeg -i {0}/video.mp4 {0}/audio.wav'.format(entry_path)
         subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if __name__ == "__main__":
   if len(sys.argv) == 1:
      main()
   elif len(sys.argv) == 2:
      main(sys.argv[1])
   else:
      main(sys.argv[1], sys.argv[2])