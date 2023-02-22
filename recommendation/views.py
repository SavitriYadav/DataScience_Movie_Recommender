from django.shortcuts import render
import pickle
import numpy
import string
# Create your views here.

with open('recommendation/similarity.pkl','rb') as data: 
    similarity = pickle.load(data)

with open('recommendation/new.pkl','rb') as newdf: 
    new = pickle.load(newdf)

def recommend(request):
    return render(request, 'recommendation/main.html')

def recommend(request):
    movie_list = []
    movie = ''
    error = ''
    if request.method == 'POST':
        movie = string.capwords(request.POST['movies'])
        # print(movie)
        try:
            movie_index = new[new['original_title'] == movie].index[0]
            distances = similarity[movie_index]
            movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
            
            movie_list = [new.iloc[i[0]].original_title for i in movie_list]
        except Exception as es:
            error = 'Sorry! This movies is not found in training list.'

    return render(request, 'recommendation/main.html',{'l_movies':movie_list or None,'movie':movie or None, 'error':error or None})
        
    