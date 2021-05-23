# -----------------------------------------------------------------------
# -----This Program For Download Any Video Or Playlist From YOUTUBE------
# -----Using Module Pytube-----------------------------------------------
# -----------------------------------------------------------------------
from pytube import YouTube
from pytube import Playlist
from termcolor import colored
import re
import pyfiglet
import os
# -----------------------------------------------------------------------
print(colored(pyfiglet.figlet_format("Develop By Mina Hany"), color="red"))
# -----------------------------------------------------------------------


def is_path():
    while True:
        global path
        path = input(
            r"Enter The Location Like: C:\Users\Mina hany\Downloads\Video ")
        is_dir = os.path.isdir(path)
        if is_dir:
            break
        else:
            print(colored("Invalid Choosed, Try Again!", color="red"))
# -----------------------------------------------------------------------


def is_url():
    while True:
        global url
        url = input("Enter The URL For Video\n").strip()
        is_url = re.search(
            r"^ ((?: https?:)?\/\/)?((?: www|m)\.)?((?: youtube\.com|youtu.be))(\/ (?: [\w\- ] +\?v=|embed\/ |v\/)?)([\w\- ]+)(\S+)?$", url)
        if is_url:
            break
        else:
            print(colored("Invalid Choosed, Try Again!", color="red"))
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
def videoDownload():
    is_url()
    is_path()
    video = YouTube(url)

    print(colored(f"The video Title is : {video.title}\n", color="blue"))
    while True:

        print("Enter The Quality")
        quality = input("1- Low Quality\n2- High Quality\n").strip().lower()
        if quality in ["1", "low", "low quality"]:
            video.streams.get_lowest_resolution().download(output_path=path)
            video.register_on_complete_callback(
                print(colored("Downloading Done", color="green")))
            break
        elif quality in ["2", "high", "high quality"]:
            video.streams.get_highest_resolution().download(output_path=path)
            video.register_on_complete_callback(
                print(colored("Downloading Done", color="green")))
            break
        else:
            print(colored("Invalid Choosed, Try Again!", color="red"))


# -----------------------------------------------------------------------
def playListDownload():
    is_url()
    is_path()
    videos = Playlist(url)

    print(colored(f"The video Title is : {videos.title}\n", color="blue"))
    while True:

        print("Enter The Quality")
        quality = input("1- Low Quality\n2- High Quality\n").strip().lower()
        if quality in ["1", "low", "low quality"]:
            for video in videos.videos:
                video.streams.get_lowest_resolution().download(
                    output_path=path)
            video.register_on_complete_callback(
                print(colored("Downloading Done", color="green")))
            break
        elif quality in ["2", "high", "high quality"]:
            for video in videos.videos:
                video.streams.get_highest_resolution().download(
                    output_path=path)
            video.register_on_complete_callback(
                print(colored("Downloading Done", color="green")))
            break
        else:
            print(colored("Invalid Choosed, Try Again!", color="red"))


# -----------------------------------------------------------------------
def main():
    while True:
        option = input(
            "Do You Want Download Video Or Playlist?\n").strip().lower()
        if option in ["video", "1", 'v']:
            videoDownload()
            break
        elif option in ["playlist", "2"]:
            playListDownload()
            break
        else:
            print(colored("Invalid Choosed, Try Again!", color="red"))


# -----------------------------------------------------------------------
main()
