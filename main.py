import cv2 # openCV library for image and video processing :)

def main():
    video_path = 'cat.mp4' # video path
    video_capture = cv2.VideoCapture(video_path) # makes object to capture video

    if not video_capture.isOpened(): # check to see if we opened video file
        print("Cannot open video file") # we didn't here so let user know
        return
    
    while True:
        has_frame, frame = video_capture.read() #Read a frame from the video

        if not has_frame:
            print("Reached end of video") # End of video, so we stop loop
            break

        cv2.imshow("VisAI - Video Feed", frame) # display the frame in window named VisAI - Video Feed

        if cv2.waitKey(30) & 0xFF == ord('q'): # Wait 30ms for a key press. If q is pressed, quit the loop
            break


    #release object
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
