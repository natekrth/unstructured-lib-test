from unstructured.partition.pdf import partition_pdf

# Applies the Thai language pack for OCR. OCR is only applied
# if the text is not available in the PDF.
elements = partition_pdf("/Users/zkeretho/Desktop/tcas-connect/tcas-test.pdf", languages=["tha"])
print("\n\n".join([str(el) for el in elements]))
