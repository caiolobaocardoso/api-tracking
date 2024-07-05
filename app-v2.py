from doctr import ocr_predictor

path_pdf = 'path'

predictor = ocr_predictor.create_predictor()

result = predictor(path_pdf)

print(result)