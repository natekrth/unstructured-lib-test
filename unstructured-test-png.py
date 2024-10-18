from unstructured.partition.image import partition_image

# Applies the Thai language pack for OCR. OCR is only applied
# if the text is not available in the image.
elements = partition_image("/Users/zkeretho/Desktop/tcas-connect/tcas-png.png", languages=["tha"], infer_table_structure=True)
print("\n\n".join([str(el) for el in elements]))