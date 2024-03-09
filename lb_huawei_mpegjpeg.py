import glob

for fname in glob.glob('*.jpg'):
    try:
        with open(fname, 'rb') as src:
            data = src.read()
            idx = data.index(b'\x00\x00\x00\x18ftypmp42')
            with open("lb_" + fname, 'wb') as dst:
                dst.write(data[:idx])
            with open("lb_" + fname[:-3] + 'mp4', 'wb') as dst:
                dst.write(data[idx:])
    except:
        pass
