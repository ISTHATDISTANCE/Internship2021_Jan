import filetype

f = open(r"D:\后端\flaskProject\Image\ltt.jpg", "rb")
kind = filetype.guess(f)
print('File extension: %s' % kind.extension)
print('File MIME type: %s' % kind.mime)
f.close()
