import simplejson
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
import pymysql
from django.shortcuts import render, redirect
from .models import Landmarks, Hotels, Restaurants
from haversine import haversine

import numpy as np

# def image_upload_view(request):
#     """Process images uploaded by users"""
#
#
#     file = r'D:\bigdata_project\ImgProcessing\media\media\images\testFile.jpg'
#
#     X = []
#     img = Image.open(file)
#     img = img.resize((224, 224))
#     img = img.convert("RGB")
#     data = np.asarray(img)
#     X.append(data)
#
#     X = np.array(X)
#     new_prediction = new_model.predict(X)
#     pre_ans = new_prediction[0].argmax()  # 예측 레이블
#
#     if pre_ans == 0:
#         pre_ans_str = "63buliding"
#     elif pre_ans == 1:
#         pre_ans_str = "castle"
#     elif pre_ans == 2:
#         pre_ans_str = "coex"
#     elif pre_ans == 3:
#         pre_ans_str = "general"
#     elif pre_ans == 4:
#         pre_ans_str = "indep_door"
#     elif pre_ans == 5:
#         pre_ans_str = "judgement_castle"
#     elif pre_ans == 6:
#         pre_ans_str = "lotte_tower"
#     elif pre_ans == 7:
#         pre_ans_str = "moonlight"
#     elif pre_ans == 8:
#         pre_ans_str = "namsan"
#     elif pre_ans == 9:
#         pre_ans_str = "seoulstation"
#     elif pre_ans == 10:
#         pre_ans_str = "tapgol_park"
#     else:
#         pre_ans_str = "what the!!"
#
#     if os.path.exists(file):
#         os.remove(r'D:\bigdata_project\ImgProcessing\media\media\images\testFile.jpg')
#
#     else:
#         pass
#
#     awb_dict = {'pre_ans_str':pre_ans_str}
#
#     return HttpResponse(simplejson.dumps(awb_dict) )

def hotel_recommendation(request):
    pre_ans = '롯데타워'
    if pre_ans == '경복궁':
        result = 0
    elif pre_ans == '명동성당':
        result = 1
    elif pre_ans == '이순신 동상':
        result = 2
    elif pre_ans == '63빌딩':
        result = 3
    elif pre_ans == '탑골공원팔각정':
        result = 4
    elif pre_ans == '독립문':
        result = 5
    elif pre_ans == '남산타워':
        result = 6
    elif pre_ans == '롯데타워':
        result = 7
    elif pre_ans == '코엑스':
        result = 8
    elif pre_ans == '서대문형무소':
        result = 9
    elif pre_ans == '구서울역':
        result = 10

    landmark = Landmarks.objects.values('name', 'lat', 'lng')
    landmark_lat = landmark[result]['lat']
    landmark_lng = landmark[result]['lng']
    landmark_latlng = landmark_lat, landmark_lng
######################################################################

    hotel = Hotels.objects.values('name', 'lat', 'lng', 'address', 'rank')

    distance_hot = []
    for count, value in enumerate(hotel):
        hotel_lat = hotel[count]['lat']
        hotel_lng = hotel[count]['lng']
        hotel_latlng = hotel_lat, hotel_lng
        d = haversine(landmark_latlng, hotel_latlng, unit='km')
        distance_hot.append((d, hotel[count]['name'], hotel[count]['lat'],
                            hotel[count]['lng'], hotel[count]['address'], hotel[count]['rank']))

    distance_hot = sorted(distance_hot, key=lambda x:x[0])
    n = 5
    distance_hot_final = distance_hot[:n]

    new_dict = {}

    for i in range(len(distance_hot_final)):
        new_dict[distance_hot_final[i][1]] = (distance_hot_final[i][0], distance_hot_final[i][2],\
                                              distance_hot_final[i][3], distance_hot_final[i][4])


    return JsonResponse(new_dict, safe=False)


def restaurant_recommendation(request):
    pre_ans = '롯데타워'
    if pre_ans == '경복궁':
        result = 0
    elif pre_ans == '명동성당':
        result = 1
    elif pre_ans == '이순신 동상':
        result = 2
    elif pre_ans == '63빌딩':
        result = 3
    elif pre_ans == '탑골공원팔각정':
        result = 4
    elif pre_ans == '독립문':
        result = 5
    elif pre_ans == '남산타워':
        result = 6
    elif pre_ans == '롯데타워':
        result = 7
    elif pre_ans == '코엑스':
        result = 8
    elif pre_ans == '서대문형무소':
        result = 9
    elif pre_ans == '구서울역':
        result = 10

    landmark = Landmarks.objects.values('name', 'lat', 'lng')
    landmark_lat = landmark[result]['lat']
    landmark_lng = landmark[result]['lng']
    landmark_latlng = landmark_lat, landmark_lng
    ###########################################################

    restaurant = Restaurants.objects.values('name', 'lat', 'lng', 'address', 'represent')

    distance_res = []
    for count, value in enumerate(restaurant):
        restaurant_lat = restaurant[count]['lat']
        restaurant_lng = restaurant[count]['lng']
        restaurant_latlng = restaurant_lat, restaurant_lng
        d = haversine(landmark_latlng, restaurant_latlng, unit='km')
        distance_res.append((d, restaurant[count]['name'], restaurant[count]['lat'],\
                            restaurant[count]['lng'], restaurant[count]['address'], restaurant[count]['represent']))

    distance_res = sorted(distance_res, key=lambda x: x[0])
    n = 10
    distance_res_final = distance_res[:n]

    new_dict = {}

    for i in range(len(distance_res_final)):
        new_dict[distance_res_final[i][1]] = (distance_res_final[i][0], distance_res_final[i][2], \
                                              distance_res_final[i][3], distance_res_final[i][4], distance_res_final[i][5])

    return HttpResponse(simplejson.dumps(new_dict))

