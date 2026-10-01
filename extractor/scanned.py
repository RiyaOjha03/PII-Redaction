image_num=1
for image in image_list:
    
    xref=image[0]
    pix=fitz.Pixmap(pdf,xref)
    if pix.n<5:
        pix.save(f'{image_num}.png')
    else:
        pix1=fitz.open(fitz.csRGB,pix)
        pix1.save(f'{image_num}.png')
        pix1=None
    pix=None
    image_num+=1
