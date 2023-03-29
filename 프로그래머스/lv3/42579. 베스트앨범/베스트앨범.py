from heapq import heappush, heappop

def solution(genres, plays):
    answer = []
    l = len(genres)
    arr = set(genres)
    genres_total = {}
    genres_list = {}
    for i in arr:
        genres_total[i] = 0
        genres_list[i] = []
        
    for index in range(l):
        genres_total[genres[index]] += plays[index]
        genres_list[genres[index]].append((-plays[index], index))
    
    popular_genres = sorted(genres_total.items(), key=lambda x: -x[1])
    
    for genre in popular_genres:
        popular_musics = sorted(genres_list[genre[0]])
        if len(popular_musics) <= 2:
            for music in popular_musics:
                answer.append(music[1])
        else:
            for j in range(2):
                answer.append(popular_musics[j][1])
        
    
    
    return answer