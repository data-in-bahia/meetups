import os, subprocess
from os.path import join

ffmpeg = 'C:\\Python37\\Scripts\\ffmpeg.exe'
inputdir = 'E:\\Projetos\\apresentacao_jus\\deeptrolldetector\\data\\30segs'
outputdir = 'E:\\Projetos\\apresentacao_jus\\deeptrolldetector\\data\\converted'


for file_path in os.listdir(inputdir):
    sourceAudio = join(inputdir, file_path)
    destinationAudio = join(outputdir, f"{file_path[:-4]}.wav")
    print(f"Vou processar o {file_path}")
    command = f"{ffmpeg} -t 30 -i {sourceAudio} -acodec pcm_u8 -ar 22050 {destinationAudio}"

    subprocess.call(command)

