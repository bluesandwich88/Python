import os
import re

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".iso"):
            # 提取数字部分
            match = re.search(r'E(\d+)\-', filename)
            if match:
                digits = match.group(1)
                new_filename = 'Criminal.Minds.S' + season + 'E' + digits +'.'+ years +'.1080p.WEBrip.x265.10bit.AC3￡cXcY@FRDS.mkv'
                # print(filename)
                # new_filename = new_filename.replace(".iso", ".mkv")
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory = "e:/testmkv/"
    season = '16'
    years = '2022'
    rename_files(directory)
