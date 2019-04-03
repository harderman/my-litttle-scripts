import os

from imageai.Detection import ObjectDetection


def pic_con(old_path, new_path):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    custom_objects = detector.CustomObjects(person=True, car=False)
    detections = detector.detectCustomObjectsFromImage(input_image=os.path.join(execution_path, old_path),
                                                       output_image_path=os.path.join(execution_path, new_path),
                                                       custom_objects=custom_objects)  # , minimum_percentage_probability=65
    for eachObject in detections:
        print(eachObject["name"] + " : " + eachObject["percentage_probability"])


def pic_batch_con():
    dirs = os.listdir('./old_dir')
    dirs.remove('.DS_Store')
    for old in dirs:
        old_path = os.path.join('./old_dir', old)
        new_path = os.path.join('./new_dir', old)
        pic_con(old_path, new_path)


if __name__ == '__main__':
    pic_batch_con()
