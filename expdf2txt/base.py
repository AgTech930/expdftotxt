import pytesseract
import base64
from PyPDF2 import PdfReader


from pdf2image import convert_from_bytes

class Base:
    def __init__(self,pdfFile):
        self.filePath = pdfFile
    
    def decode(self,binary_data):
        """
        Decode binary data using base64.

        Parameters:
        - binary_data (bytes): Binary data to be decoded.

        Returns:
        bytes: Decoded binary data.
        """
        encoded_data = base64.b64encode(binary_data)
        base_data = base64.b64decode(encoded_data)
        return base_data

    def decode_file(self):
        """
        Read binary data from a file and decode it using base64.

        Returns:
        bytes: Decoded binary data.
        """
        with open(self.filePath, 'rb') as file:
            binary_data = file.read()
            base_data = self.decode(binary_data)
        return base_data

    def countpages(self):
        pdf = PdfReader(self.filePath)
        return len(pdf.pages)

    def extract_document(self):
        """
        Extract text content from a document file, such as a PDF.

        Returns:
        dict: A dictionary containing extracted information.

        """
        isBytes = type(self.filePath) is bytes
        base_data = self.filePath
        if not isBytes:
            base_data = self.decode_file()
        images = convert_from_bytes(base_data)
        page_contents = []
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image, lang='eng')
            page_contents.append(text)

        document = {
            'page_content': page_contents[0],
            'metadata': {'source': 'test_inv.pdf'}
        }
        return document
    
    def extract_string(self):
        extracted_data = ""
        pdf = PdfReader(self.filePath)
        for i in range(self.countpages()):
            page = pdf.pages[i]
            extracted_data += "\n\n" + page.extract_text()
        return extracted_data