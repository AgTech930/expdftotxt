# EXPDF2TXT

## Overview

The expdf2txt is a versatile and efficient package designed for seamless conversion of PDF (Portable Document Format) files into TXT (Plain Text) format.
This package empowers users with a straightforward and reliable method to extract textual content from PDF documents, making it easily accessible and editable."

## Usage
### Example

from expdf2txt.invoice2text import InvoiceExtractor
FILEPATH = "invoice_2001321.pdf"
invocie_extractor = InvoiceExtractor(FILEPATH)
data = invocie_extractor.openai_extract_data(format_data=True)
print(data)

#Features

1. InvoiceExtractor (Convert Invoice Pdf to Text)
    Code: 
        from expdf2txt.invoice2text import InvoiceExtractor
        FILEPATH = "invoice_2001321.pdf"
        invocie_extractor = InvoiceExtractor(FILEPATH)
        data = invocie_extractor.openai_extract_data(format_data=True)
        print(data)

New Features Comming Soon...


#Methods

1. InvoiceExtractor method :
            -> openai_extract_data() 'This method extracts text from a Invoice Pdf'
                Parameters:
                - temperature (float, optional): The temperature parameter for the OpenAI LLM.
                - api_key (str, optional): The API key for accessing OpenAI services. 
                        Note: "If the default API key is not functioning, please provide an alternative API key for use."  
                - template (str, optional): Custom template string for document extraction.
                - format_data (bool, optional): If True, format the extracted data into a dictionary or list; if False, return raw output.
                        Note: "If the data is successfully converted into a dictionary, it will be returned as a dictionary. Otherwise, it will be returned as a list."

# Dependencies

'langchain',
'pytesseract',
'pdf2image',
'PyPDF2', 

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Issues

If you encounter any issues or have suggestions, please create an issue on the GitHub repository.

# Acknowledgments

Mention any libraries or tools you used and give credit to their respective authors


