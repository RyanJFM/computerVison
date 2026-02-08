import cv2 as cv

def read_images():
    img = cv.imread('photos/cat.webp')
    cv.imshow('Cat', img)
    cv.waitKey(0)
    

def read_video():
    capture = cv.VideoCapture('videos/dog.mp4')
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)
        
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
        
    capture.release()
    cv.destroyAllWindows() 
    
    
def main():
    #read_images()
    read_video()
    
if __name__ == '__main__':
    main()