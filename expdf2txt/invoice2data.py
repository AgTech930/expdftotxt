from openai import OpenAI
from .base import Base
import logging


class InvoiceExtractor(Base):
    def __init__(self,filePath):
        return super().__init__(filePath)

    def extract_document(self):
        document_data = super().extract_document()
        return document_data

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
    
    def openai_extract_data(self,temperature=.7,api_key="",template="",format_data=False):
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
            if not api_key:
                raise ValueError("API key not found. Please provide an API key.")
            client = OpenAI(api_key=api_key)
            temperature = temperature
            document = self.extract_document()
            template = self._template(template,document)
            max_tokens = 3000
            response = client.completions.create(
                                                model="gpt-3.5-turbo-instruct",
                                                max_tokens=max_tokens
                                                )
            final_data = self.data_format(response.choices[0].text) if format_data else response.choices[0].text
            return final_data
        
        except ValueError as e:
            raise ValueError(e)






