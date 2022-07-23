import os
import sys
import subprocess
import glob
from collections import defaultdict

def crop_and_create_files(video_path, start_time, end_time, text, snippet_path):
    try:
        # crop video
        save_path_video = os.path.join(snippet_path, 'snippet.mp4')
        command = ("ffmpeg -ss %s -i %s -t %s %s" % (start_time, video_path, end_time-start_time, save_path_video))
        output = subprocess.call(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # create text file for video
        save_path_text = os.path.join(snippet_path, 'text.txt')
        with open(save_path_text, 'w') as f:
            f.write(text)

        return True
    except Exception as e:
        return False

def main(root_dir = './corpus'):
    timings_file = './timings.txt'
    data_store = []
    # open timing file
    with open(timings_file, 'r') as f:
        snippets = f.readlines()
        for snippet in snippets:
            data_store.append(snippet.split('|'))
    
    id_dict = defaultdict(lambda:0)
    for data in data_store:
        podcast_id = data[0]
        # check if the podcast folder exists
        if not os.path.exists(os.path.join(root_dir, podcast_id)):
            print("Podcast {} does not exist, skipping...".format(podcast_id))
            continue
        
        # check if the video exists
        video_path = os.path.join(root_dir, podcast_id, 'video.mp4')
        if not os.path.exists(video_path):
            print("Video does not exist for podcast, skipping...", podcast_id)
            continue
        
        # create the snippets folder for the podcast
        snippets_path = os.path.join(root_dir, podcast_id, 'snippets')
        if not os.path.exists(snippets_path):
            print("Creating", snippets_path)
            os.makedirs(snippets_path)
        
        start_time = float(data[1])
        end_time = float(data[2])
        text = data[3]
        snippet_id = id_dict[podcast_id]

        # create a folder for the snippet
        snippet_path = os.path.join(snippets_path, podcast_id + '_%04d'%snippet_id)
        if not os.path.exists(snippet_path):
            os.makedirs(snippet_path)
            id_dict[podcast_id] += 1
        elif len(os.listdir(snippet_path)) == 2:
            print("Snippet {} already exists, skipping...".format(snippet_path))
            id_dict[podcast_id] += 1
            continue
        else:
            # Only some files may have breen created so deleting them to recreate
            files = glob.glob(snippet_path+'/*')
            for file in files:
                os.remove(file)
            id_dict[podcast_id] += 1
        
        # crop the video
        result = crop_and_create_files(video_path, start_time, end_time, text, snippet_path)
        if result:
            print("Suceesfully created snippet", snippet_path)
        else:
            print("Some error occured, skipping", snippet_path)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1])