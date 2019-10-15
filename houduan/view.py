# -*- coding: utf-8 -*-
from houduan import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from houduan.models import *
import json

def register(request):
    result = {"content": ""}
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = loginuser()
            user.username = username
            user.password = password
            user.save()
            return HttpResponseRedirect("/login/")
        else:
            result["content"] = "用户名或者密码不可以为空"
    return render(request, "register.html", locals())


def login(request):
    result = {"content": ""}
    if request.method == "POST":
        login_dict = json.loads((request.body).decode("utf-8"))
        username = str(login_dict["username"])
        password = str(login_dict["password"])
        #username = request.POST.get("username")
        #password = request.POST.get("password")
        print(username, password)
        if username and password:
            user = loginuser.objects.filter(username=username).first()
            if user:
                if password == user.password:
                    #response = HttpResponseRedirect("/index/")
                    #response.set_cookie("username", user.username)
                    return JsonResponse('ok',safe=False)
                else:
                    return JsonResponse('fail_password',safe=False)
            else:
                return JsonResponse('fail_user',safe=False)
        else:
            return JsonResponse('fail_null',safe=False)
    #return render(request, "login.html", locals())
    return JsonResponse('fail_request',safe=False)


def logout(request):
    response = HttpResponseRedirect("/login/")
    response.delete_cookie("username")
    return response


def show(request):
    return render(request, 'show.html')


def airbnb_detail(request):
    target_id = request.GET.get("id")
    item = listings.objects.get(id=target_id)
    data = datastructure(item)
    response = JsonResponse(data,safe=False)
    return response


def filter(request):


    filter_dict = json.loads((request.body).decode("utf-8"))

    #filter1_arg = request.POST.get("filter1")
    #filter2_arg = request.POST.get("filter2")
    #filter3_arg = request.POST.get("filter3")
    filter1_arg = filter_dict["filter1"]
    filter2_arg = filter_dict["filter2"]
    filter3_arg = filter_dict["filter3"]
    print(filter1_arg)
    # Filter1 ---- Location
    if int(filter1_arg) != 0:
        location_choice_list = ['NOT_EXIST', 'Central Region', 'North Region', 'East Region', 'West Region']
        location_index = int(filter1_arg)
        filter_result = listings.objects.all().filter(neighbourhood_group_cleansed=location_choice_list[location_index])
    else:
        filter_result = listings.objects.all()
        
    # Filter2 ---- Accommodates
    # case 1: 1 to 3 People
    # case 2: 4 to 6 People
    # case 3: 7 to 10 People
    # case 4: Over 10 People
    if int(filter2_arg) == 1:
        filter_result = filter_result.filter(accommodates__lte=3, accommodates__gte=1)
    elif int(filter2_arg) == 2:
        filter_result = filter_result.filter(accommodates__lte=6, accommodates__gte=4)
    elif int(filter2_arg) == 3:
        filter_result = filter_result.filter(accommodates__lte=10, accommodates__gte=7)
    elif int(filter2_arg) == 4:
        filter_result = filter_result.filter(accommodates__gt=10)
    # Filter3 ---- Price
    # $0 -$49
    # $50 -$99
    # $100 -$299
    # $300 -$500
    # Over $500
    if int(filter3_arg) == 1:
        filter_result = filter_result.filter(price_adjust__lte=49, price_adjust__gte=0)
    elif int(filter3_arg) == 2:
        filter_result = filter_result.filter(price_adjust__lte=99, price_adjust__gte=50)
    elif int(filter3_arg) == 3:
        filter_result = filter_result.filter(price_adjust__lte=299, price_adjust__gte=100)
    elif int(filter3_arg) == 4:
        filter_result = filter_result.filter(price_adjust__lte=500, price_adjust__gte=300)
    elif int(filter3_arg) == 5:
        filter_result = filter_result.filter(price_adjust__gt=500)

    # Order by rating
    filter_result = filter_result.order_by("-review_scores_rating")
    final_data = []
    for item in filter_result[:9]:
        final_data = appendQuery(final_data, item)

    # print(filter_result)
    return JsonResponse(final_data,safe=False)


def hotlist(request):
    hotlist_data = []
    if request.method == "GET":
        hotlist = listings.objects.all().order_by("-number_of_reviews")
        for item in hotlist[:3]:
            hotlist_data = appendQuery(hotlist_data, item)
    return JsonResponse(hotlist_data,safe=False)

def latest_booking(request):
    latest_booking_data = []
    if request.method == "GET":
        booking_list = listings.objects.all().order_by("-last_review")
        for item in booking_list[:3]:
            latest_booking_data = appendQuery(latest_booking_data, item)
    return JsonResponse(latest_booking_data,safe=False)

def recommender(request):
    target_id = request.GET.get("id")
    user_id = request.GET.get("user_id")
    way = request.GET.get("recommender_way")

    if way == 'simi':
        item = simi.objects.get(id=target_id)
        recommender_result = listings.objects.filter(Q(id=item.item1) | Q(id=item.item2) | Q(id=item.item3))
        recommender_by_similarity = []
        for item in recommender_result:
            recommender_by_similarity = appendQuery(recommender_by_similarity, item)
        return JsonResponse(recommender_by_similarity,safe=False)
    elif way == 'als':
        item = als.objects.get(id=user_id)
        recommender_result = listings.objects.filter(
            Q(id=item.listing_id1) | Q(id=item.listing_id2) | Q(id=item.listing_id3))
        recommender_by_als = []
        for item in recommender_result:
            recommender_by_als = appendQuery(recommender_by_als, item)
        return JsonResponse(recommender_by_als,safe=False)
    elif way == 'topic':
        item_lookfortopic = topic_model.objects.get(id=target_id)
        # print(item_lookfortopic.topic1)
        item = topic_reference.objects.get(id=item_lookfortopic.topic1)
        recommender_result = listings.objects.filter(Q(id=item.item1) | Q(id=item.item2) | Q(id=item.item3))
        recommender_by_topic = []
        for item in recommender_result:
            recommender_by_topic = appendQuery(recommender_by_topic, item)
        return JsonResponse(recommender_by_topic,safe=False)

    return JsonResponse('recommender way not defined',safe=False)


def appendQuery(origin, item):
    data = datastructure(item)
    origin.append(data.copy())
    return origin


def datastructure(item):
    data = {
        'listing_id': item.id,
        'picture_url': item.picture_url,
        'name': item.name,
        'price': item.price,
        'review_scores_rating': item.review_scores_rating,
        'neighbourhood_group_cleansed': item.neighbourhood_group_cleansed,
        'accommodates': item.accommodates,
        "room_type": item.room_type,
        'host_id': item.host_id,
        'host_name': item.host_name,
        'availability_365': item.availability_365,
        'amenities': item.amenities,
        'bedrooms': item.bedrooms,
        'bathrooms': item.bathrooms,
        'last_review': item.last_review,
        'number_of_reviews': item.number_of_reviews,
        'reviews_per_month': item.reviews_per_month,
        'minimum_nights': item.minimum_nights,
        'calculated_host_listings_count': item.calculated_host_listings_count,
        'description': item.description,
    }
    return data
