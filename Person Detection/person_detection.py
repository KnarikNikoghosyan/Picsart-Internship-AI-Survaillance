import cv2
import math
from ultralytics import YOLO

class PersonDetector:
    def __init__(self, model_path='yolo-Weights/yolov8n.pt'):
        """
        Initializes the PersonDetector with the YOLOv8 model.
        
        :param model_path: Path to the YOLOv8 model. Default is 'yolo-Weights/yolov8n.pt'.
        """
        self.model = YOLO(model_path)
        
    def detect(self, frame):
        """
        Detect persons in the given image using YOLOv8.
        
        :param fram: The input frame(image) from the webcam.
        :return: A list of detections for persons.
        """
        results = self.model(frame, stream=True)
        detections = []

        # Coordinates and class ID for "person" (class ID 0 in YOLO)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int
                
                # Confidence score for the detection
                confidence = math.ceil((box.conf[0] * 100)) / 100
                class_id = int(box.cls[0])

                # Only considering the "person" class (class_id = 0 in YOLO)
                if class_id == 0:
                    detections.append({
                        'bbox': (x1, y1, x2, y2),
                        'confidence': confidence,
                        'class': 'person'
                    })

        return detections

    def draw_boxes(self, frame, detections):
        """
        Draw bounding boxes and class names on the image.
        
        :param img: The input image (frame) to draw on.
        :param detections: List of detections to draw (only persons).
        :return: Image with drawn bounding boxes and labels.
        """
        for detection in detections:
            bbox = detection['bbox']
            confidence = detection['confidence']

            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 255), 3)

            # Displaying confidence
            label = f'{detection["class"]}: {confidence:.2f}'
            cv2.putText(frame, label, (bbox[0], bbox[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
        return frame

def run_person_detection():
    """
    Main function to initialize and run person detection on webcam input.
    Continuously reads frames from the webcam, detects persons, and displays results.
    """
    detector = PersonDetector()
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        detections = detector.detect(frame)
        frame_with_boxes = detector.draw_boxes(frame, detections)

        cv2.imshow("Person Detection (Press Q to Exit)", frame_with_boxes)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_person_detection()