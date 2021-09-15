from ftplib import FTP

with FTP("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu") as ftp:
    img = open("20210915_124848.mp4", 'r+b')
    ftp.storbinary("STOR 20210915_124848.mp4", img)
    ftp.dir()