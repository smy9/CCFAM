from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import cv2
import face_recognition
import os

path1 = 'celeb_transparent/white_bg_aligned'
path2 = 'celeb_transparent/generated_images/white'

list1 = os.listdir(path1)
list2 = os.listdir(path2)

sum1 = 0
sum2 = 0

cnt = 0
for i in list1:
    if i in list2:
        image1 = cv2.imread(os.path.join(path1, i))
        image2 = cv2.imread(os.path.join(path2, i))
        v1 = face_recognition.api.face_encodings(image1, model='large')
        v2 = face_recognition.api.face_encodings(image2, model='large')
        if not v1 or not v2:
            continue
        cnt += 1
        print(cnt)
        sum1 += cosine_similarity(v1, v2)[0][0]
        sum2 += euclidean_distances(v1, v2)[0][0]
        print('cosine_similarity:', sum1 / cnt)
        print('euclidean_distances:', sum2 / cnt)
