from libtorrentx import LibTorrentSession
import time

magnet = "magnet:?xt=urn:btih:4C9B41D664D7B6B23F0BF39AE185858CBADDA3FF"
output_dir = "./downloads"
session = LibTorrentSession()
handle = session.add_torrent(magnet, output_dir)

while True:
    props = handle.props()

    if not props.ok:
        print("waiting for torrent to start...")
        time.sleep(1)
        continue

    print(props.string)

    if props.is_finished:
        break

    time.sleep(1)