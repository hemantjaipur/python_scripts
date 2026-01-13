import os
os.environ['USE_TORCH'] ='1'
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# 1. Load a pre-trained OCR model
# Use the ocr_predictor factory function with desired architectures
model = ocr_predictor(pretrained=True,assume_straight_pages=False,
    export_as_straight_boxes=False)

#previously used this 
# Use the ocr_predictor factory function with desired architectures
# model = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)

#using this

# model = ocr_predictor(det_arch='db_resnet50', reco_arch='sar_resnet31', pretrained=True)
# result = model.predict([site_plan_image])

# 2. Load your document (image or PDF)
# You can use DocumentFile.from_images or DocumentFile.from_pdf
doc = DocumentFile.from_images(["/content/site_plan_2.png"])

# 3. Perform the OCR
result = model(doc)

# 4. Export the results to a structured format (e.g., JSON)
json_output = result.export()

# Accessing the orientation for each page
for page in result.pages:
    # The orientation attribute gives the angle in degrees
    orientation_angle = page.orientation
    print(f"Page orientation: {orientation_angle} degrees")

age = result.pages[0]
img_height, img_width = page.dimensions

# 5. Print the extracted text (simple iteration)


for page in json_output['pages']:
    for block in page['blocks']:
        for line in block['lines']:
            line_text = " ".join([word['value'] for word in line['words']])
            print(line_text)


