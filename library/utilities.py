import cv2
from pyzbar import pyzbar

def decode(image)->str:
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    try:
        for obj in decoded_objects:
            return {"data":obj.data.decode()}
    except:
        return None

if __name__=='__main__':
    img=cv2.imread("library/1barcode.jpg")
    res=decode(img)
    print(type(res["data"]),res["data"])
