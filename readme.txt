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


