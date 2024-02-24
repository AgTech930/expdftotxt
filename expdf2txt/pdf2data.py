from .base import Base
import fitz
import os

class PDFExtractor(Base):
    def __init__(self,pdfFile):
        self.pdfFile = pdfFile
        return super().__init__(pdfFile=pdfFile)
    
    def countpages(self):
        """
        Count the number of pages in the document.

        This method returns the total number of pages in the document.

        Returns:
            int: The number of pages in the document.
        """
        return super().countpages()

    def extract_string(self):
        """
        Extract the data from the source.

        This method retrieves the data from the source data. The specific behavior
        of extraction might depend on the implementation in the subclass.

        Returns:
            str: The extracted string.
        """
        return super().extract_string()

    def extract_image(self):
        """
        Extract images from the PDF document.

        This method extracts images from each page of the PDF document and saves them as separate files.
        
        Raises:
            ValueError: If no images are found in the PDF document.

        Returns:
            bool: True if images are extracted successfully.
        """
        pdf_file = fitz.open(self.pdfFile)
        page_nums = self.countpages()
        img_list = []

        for page in range(page_nums):
            page_content = pdf_file[page]
            img_list.extend(page_content.get_images())
        
        if len(img_list)==0:
            raise ValueError(f'No images found in {self.pdfFile}')
        
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
        
        return True
