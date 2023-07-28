from pytube import YouTube



while True:
    link = input("Please enter the link: ")

    yt = YouTube(link)
    yr = yt.streams.get_highest_resolution()

    print("Your video is downloading. Please wait.")
    wait = 1
    for i in range(3):
        print("{}/3".format(wait))
        wait += 1
    yr.download()
    print("Your video has been downloaded successfully.")


