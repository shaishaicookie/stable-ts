import stable_whisper

# [Errno 63] File name too long
# input files are under same dir as this script
try:
    audio_path = "audio.mp3"
    srt_path = "audio.srt"

    stable_whisper.encode_video_comparison(
        audio_path,
        [srt_path],
        output_videopath="FileNameTooLong.mp4",
        labels=["FileNameTooLong"],
    )
except Exception as e:
    print("**** An error occurred ****")
    print("**** When input files are under same dir as this script ****")
    print(e)

print("\n\n")

# FileNotFoundError
# input files are not under same dir as this script
try:
    audio_path = "audio/audio.mp3"
    srt_path = "audio/audio.srt"

    stable_whisper.encode_video_comparison(
        audio_path,
        [srt_path],
        output_videopath="FileNotFoundError.mp4",
        labels=["FileNotFoundError"],
    )
except Exception as e:
    print("**** An error occurred ****")
    print("**** When input files are not under same dir as this script ****")
    print(e)
