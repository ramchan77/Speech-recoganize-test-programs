import cv2
import tesseract
gray = cv2.LoadImage('out.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.Threshold(gray, gray, 231, 255, cv2.CV_THRESH_BINARY)
api = tesseract.TessBaseAPI()
api.Init(".","eng",tesseract.OEM_DEFAULT)
api.SetVariable("tessedit_char_whitelist", "ABCDEFGHIJKLMNOPQRSTUVWZYZ")
api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
tesseract.SetCvImage(gray,api)
print api.GetUTF8Text()
