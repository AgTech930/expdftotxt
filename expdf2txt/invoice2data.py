from openai import OpenAI
import base64
import pytesseract  
from pdf2image import convert_from_bytes
import logging
from .openaiCredential import OpenAiCredential


class InvoiceExtractor(OpenAiCredential):
    def __init__(self,filePath):
        super().__init__()
        self.filePath = filePath


    def _decode(self,binary_data):
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
    
    def _decode_File(self):
        """
        Read binary data from a file and decode it using base64.

        Returns:
        bytes: Decoded binary data.
        """
        with open(self.filePath, 'rb') as file:
            binary_data = file.read()
            base_data = self._decode(binary_data)
        return base_data

    def extract_document(self):
        """
        Extract text content from a document file, such as a PDF.

        Returns:
        dict: A dictionary containing extracted information.

        """
        isBytes = type(self.filePath) is bytes
        base_data = self.filePath
        if not isBytes:
            base_data = self._decode_File()
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

    def _template(self,template="",pages=""):
        """
        Generate a template string for document extraction.

        Parameters:
        - template (str, optional): Custom template string to append information to.

        Returns:
        str: Generated template string.

        """
        if template:
            template = template+""", invoice number """+f""" in {pages} and i don't want code """
        else:
            template = f"""
                        Extract invoice number, company name , bill from organization, bill from address, bill to , bill to address, date, item name, item quantity, unit price , total price in {pages} and i don't want code
                    """
        return template

    def data_format(self,data):
        """
        Format raw text data into a dictionary.

        Parameters:
        - data (str): Raw text data to be formatted.

        Returns:
        dict or list: If successful, a dictionary containing key-value pairs extracted from the data.
                    If an error occurs during the formatting process, the original data is returned in list.
        """
        
        data = data.split('\n')
        try:
            invoice_dict = {}
            for item in data:
                if item == "": continue
                key,value = item.split() if item.count(":") == 0 else item.split(':',1)
                key = key.lower().replace(' ',"_")
                invoice_dict[key] = value
            return invoice_dict
        except:
            return data
    
    def openai_extract_data(self,temperature="",api_key="",template="",format_data=False):
        """
        Extract structured data from a document using OpenAI's Language Model (LLM) and Named Entity Recognition (NER).

        Parameters:
        - temperature (float, optional): The temperature parameter for the OpenAI LLM.
        - api_key (str, optional): The API key for accessing OpenAI services.
        - template (str, optional): Custom template string for document extraction.
        - format_data (bool, optional): If True, format the extracted data into a dictionary; if False, return raw output.

        Returns:
        dict or str: If successful, a dictionary containing extracted structured data or raw output if `format_data` is False.
                    If an error occurs during the extraction process, the exception message is printed and logged.
        """
        try:
            client = OpenAI(api_key=api_key if api_key else self.api_key)
            temperature = temperature if temperature else self.temperature
            document = self.extract_document()
            template = self._template(template,document)
            max_tokens = 3000
            response = client.completions.create(model="gpt-3.5-turbo-instruct",  # You can choose a different engine
                                                prompt=template,
                                                max_tokens=max_tokens)
            final_data = self.data_format(response.choices[0].text) if format_data else response.choices[0].text
            return final_data
        except ValueError as e:
            print(e)
            logging.info(e)






