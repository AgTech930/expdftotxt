from .base import Base
import fitz
import os

class PDFExtractor:
    def __init__(self,pdf_data):
        self.base = Base(pdf_data)
        self.pdf_data = pdf_data
    
    def countpages(self):
        return self.base.countpages()

    def extract(self):
        extracted_data = self.base.extract_string()
        return extracted_data

    def extract_image(self):
        pdf_file = fitz.open(self.pdf_data)
        page_nums = self.countpages()
        img_list = []

        for page in range(page_nums):
            page_content = pdf_file[page]
            img_list.extend(page_content.get_images())
        
        if len(img_list)==0:
            raise ValueError(f'No images found in {self.pdf_data}')
        
        for i, img in enumerate(img_list, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            #Store image bytes
            image_bytes = base_image['image']
            image_ext = base_image['ext']
            image_name = str(i) + '.' + image_ext
            with open(os.path.join(image_name) , 'wb') as image_file:
                image_file.write(image_bytes)
                image_file.close()
