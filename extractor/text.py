from extractor_import import *

pdf=fitz.open('C:\\Users\\kumar\\Desktop\\hackatron_ml\\uploaded_pdfs\\Profile.pdf')
page=pdf[0]
text_data=page.get_text("dict")
storage_sender(text_data)



# for block in text_data["blocks"]:
#     if block["type"]==0:
        
#         for line in block["lines"]:
#             for span in line["spans"]:
#                 x,y=span["origin"]
#                 #print(f'x={x}, y={y}')
#                 font=span["font"]
#                 color=span["color"]
#                 text=span["text"]
#                 #print(text)
#                 font_size=span["size"]
#                 print(text)
#         # print(block)








# #image extraction part

# image_list= page.get_images(full=True)

# print(image_list)
# dict={}
# lst=[]

# image_num=1
# for image in image_list:
#     dic_in_lst={}
#     xref=image[0]
#     pix=fitz.Pixmap(pdf,xref)
#     if pix.n<5:
#         pix.save(f'{image_num}.png')
#     else:
#         pix1=fitz.open(fitz.csRGB,pix)
#         pix1.save(f'{image_num}.png')
#         pix1=None
#     pix=None
    
#     name=image[7]
#     print(f'name of image {name}')
#     dic_in_lst["type"]=1
#     bbox=page.get_image_bbox(name)
#     dic_in_lst["bbox"]=[bbox.x0,bbox.y0,bbox.x1,bbox.y1]
#     dic_in_lst["image"]=image[7]
#     dic_in_lst["xref"]=image[0]
#     dic_in_lst["ext"]='png'
#     dic_in_lst["path"]=f'C:\\Users\\kumar\\Desktop\\PyMuPDF\\{image_num}.{dic_in_lst["ext"]}'
#     image_num+=1
#     lst.append(dic_in_lst)
# dict["blocks"]=lst
# print(dict)


        


 








    