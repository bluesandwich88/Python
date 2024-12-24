import os
def rename_files(directory):
    for filename in os.listdir(directory):
        print(filename)
        # originalname = os.path.splitext(directory[filename])[0]
        new_filename = filename + '.jpg'
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

if __name__ == "__main__":
    directory = "E:/ddd/"
    rename_files(directory)
