#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
from PIL import Image, ImageEnhance

def test4():
    image = 'dreadlocks-styles-for-black-women-766x1024.jpg'
    #watermark = 'wappa-log-640BW-2.png'
    watermark = 'wappa-log-640BW.png'
    #watermark = 'wappa-log-640BW-2-white-removed.png'

    img = Image.open(image) # img de base
    wmark = Image.open(watermark) # img filigrane

    # image sur laquelle je vais d'abord coller mon filigrane
    img_w = Image.new(img.mode, img.size)

    x = (img.size[0] - wmark.size[0])/2 # x pour collage
    y = (img.size[1] - wmark.size[1])/2 # y pour collage

    # je cree un filigrane intermediaire
    img_w.paste(wmark, ( int(x), int(y) ), wmark)
    img_w.save("filigrane.jpg", "jpeg", quality=50,
             optimize=True,
             progressive=True)

    # ensuite j'ouvre mon filigrane intermediaire
    fil = Image.open('filigrane.jpg')

    x1 = (img.size[0] - fil.size[0])/2 # x pour collage
    y2 = (img.size[1] - fil.size[1])/2 # y pour collage
    # je cree un mask en partant de mon filigrane intermediaire
    #mask_fil = fil.convert("L").point(lambda x: max(x, 100))
    mask_fil = fil.convert("L").point(lambda x: min(x, 100))

    img.paste(fil, ( int(x1), int(y2) ), mask_fil)
    img.save("result_filigrane.jpg", "jpeg", quality=50,
             optimize=True,
             progressive=True)

    # reduire opacite ?!
    #mask2 = wmark.convert("L").point(lambda x: max(x, 100))
    #wmark.putalpha(mask2)

    # retire tous les noirs
    mask1 = wmark.convert("L").point(lambda x: min(x, 100))

    img.paste(wmark, ( int(x), int(y) ), mask1)
    img.save("result.jpg", "jpeg", quality=50,
             optimize=True,
             progressive=True)




    # print("img size: %s" % str(img.size))

    # print("img format: %s" % str(img.format))
    # print("wmark size: %s" % str(wmark.size))
    # print("img mode: %s" % str(img.mode))
    # print("wmark mode: %s" % str(wmark.mode))

    # print("wmark format: %s" % str(wmark.format))

    # preciser x,y pour coller si i & w ont des sizes !=
    #img.paste(wmark, (50, 50), wmark)


    # img.paste(wmark2, ( int(x), int(y) ), wmark2)
    # img.save("result2.jpg", "jpeg", quality=50,
    #          optimize=True,
    #          progressive=True)

    # img.paste(wmark3, ( int(x), int(y) ), wmark3)
    # img.save("result3.jpg", "jpeg", quality=50,
    #          optimize=True,
    #          progressive=True)

if __name__ == '__main__':
    test4()
