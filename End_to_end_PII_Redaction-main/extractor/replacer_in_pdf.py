
from extractor.qr_redactor import get_barcode_coordinates
import pymupdf as fitz


def replacer(lst,permanent_path):
    
    

    doc = fitz.open(permanent_path)
    for i in range(len(doc)):
        page = doc.load_page(i)  
        page_text = page.get_text("text")
        for item in lst:
            if item in page_text:
                areas = page.search_for(item)
                for area in areas:
                    page.add_redact_annot(area, fill=(1, 1, 1))  #Black rectangle=>(0, 0, 0) and White=>(1, 1, 1)
        page.apply_redactions()
        # for qr removal 
        coordinate_list = get_barcode_coordinates(permanent_path)
        if coordinate_list == []:
            continue
        else:
            for  coords in coordinate_list:
                for x,y,z,h in coords:
                    page.add_redact_annot(fitz.Rect(x, y, x, y), fill=(1, 1, 1))
        page.apply_redaction()


    #Saving redacted pdf
    finals='backend\\ai\\redacted_uploads\\redacted.pdf'
    doc.save(finals)
    doc.close()
    return finals
