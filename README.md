# EXPDF2TXT

## 🤔 Overview

The expdf2txt is a versatile and efficient package designed for seamless conversion of PDF (Portable Document Format) files into TXT (Plain Text) format.
This package empowers users with a straightforward and reliable method to extract textual content from PDF documents, making it easily accessible and editable."


# ❓ Features

## 1. InvoiceExtractor (Convert Invoice Pdf to Text)

### Code: 
```python
from expdf2txt.invoice2data import InvoiceExtractor
FILEPATH = "invoice_2001321.pdf"
invocie_extractor = InvoiceExtractor(FILEPATH)
data = invocie_extractor.openai_extract_data(format_data=True)
print(data)
```

## 2. ImageExtractor (extract image from pdf)

### Code:   
```python
from expdf2txt.pdf2data import PDFExtractor
FILEPATH = "invoice_2001321.pdf"
pdf_obj = PDFExtractor(FILEPATH)
pdf_obj.extract_image()
```




# 🚀 Methods

## 1. InvoiceExtractor methods :
**openai_extract_data()** 'This method extracts text from a Invoice Pdf'
- **Parameters:**
 1. ***temperature (float, optional):*** The temperature parameter for the OpenAI LLM.
 2. ***api_key (str, optional):*** The API key for accessing OpenAI services. 
                Note: "If the default API key is not functioning, please provide an alternative API key for use."  
 3. ***template (str, optional):*** Custom template string for document extraction.
 4. ***format_data (bool, optional):*** If True, format the extracted data into a dictionary or list; if False, return raw output.
                Note: "If the data is successfully converted into a dictionary, it will be returned as a dictionary. Otherwise, it will be returned as a list."

## 2. PDFExtractor methods:
- **countpages()** 'Count the number of pages in the document.'
- **extract_string()** 'Extract the data from the source.'
- **extract_image()** 'Extract images from the PDF document and saves them as separate files.'


# Dependencies

- **openai**

- **pytesseract**

- **PyPDF2**

- **PyMuPDF**

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Issues

If you encounter any issues or have suggestions, please create an issue on the GitHub repository.

# Acknowledgments

Mention any libraries or tools you used and give credit to their respective authors.


