# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse


# def movie_list(request):
#     movies = Movie.objects.all()

#     print(movies.values)
#     data = {
#         'movies':list(movies.values())
#     }
#     return JsonResponse(data)


# def movie_detail(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     print(movie.name)
#     data = {
#         'name': movie.name,
#         'discription': movie.discription
#     }
#     return JsonResponse(data)








