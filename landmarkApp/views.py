from django.shortcuts import render

# Create your views here.
import pymysql
from django.shortcuts import render, redirect
from .models import Landmarks, Hotels, Restaurants
from haversine import haversine

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

    result = '명동성당'
    # 랜드마크의 lat, lng
    landmark_list = {}
    landmark = Landmarks.objects.values('name')



    # 전체호텔 리스트
    hotel = Hotels.objects.values('name', 'lat', 'lng')
    hotel[0]['lat']
    for count, value in enumerate(hotel):
        hotel_lat = hotel[count]['lat']
        hotel_lng = hotel[count]['lng']

    hotel_latlng = hotel_lat, hotel_lng

    # 가까운 5개

    #distance = haversine(landmark_latlng, hotel_latlng, unit='km')

    context = {
        'hotel': hotel,
        'landmark': landmark,
        'result': result,
        # 'hh' : hh
        #'distance': distance

    }

    return render(request, "hotel/show.html", context)

