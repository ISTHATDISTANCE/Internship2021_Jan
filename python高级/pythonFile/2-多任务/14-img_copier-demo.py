import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(url,nam):
    img = urllib.request.urlopen(url)
    img_content = img.read()
    with open(nam, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "https://i0.hdslb.com/bfs/vc/fb9521333b8ea79d90bdfc6da31cf83c52d93ec9.png","1.jpg"),
        gevent.spawn(downloader, "https://www.bilibili.com/video/BV11r4y1T7aX?spm_id_from=333.851.b_7265636f6d6d656e64.1","2.mp4"),
        gevent.spawn(downloader, "https://i0.hdslb.com/bfs/sycp/creative_img/202101/f6eaac53a382c5cf76722924734d3af6.jpg@412w_232h_1c","3.jpg"),

    ])


if __name__ == '__main__':
    main()
