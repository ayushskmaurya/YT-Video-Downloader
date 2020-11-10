# YT-Video-Downloader
Download YouTube Videos using Python Flask.

This application allows user to download different YouTube videos in local device.<br />
YouTube videos can also be downloaded having different resolutions.<br />

#### Note
1. Install pytube3
2. In pytube/extract.py file change

```
cipher_url = [
                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
            ]
```

to

```
cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]
```
