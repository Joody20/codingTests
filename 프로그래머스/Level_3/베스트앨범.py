def solution(genres, plays):
    answer = []
    # 장르별 재생 횟수를 담은 map
    genre_plays = {}
    # 장르별 가장 많이 들은 노래2개를 담은 map
    genre_songs = {}
    
    for i, genre in enumerate(genres): # 이 때 i는 고유번호 !
        if genre in genre_songs: # genre별 genre가 있다면
            genre_plays[genre] = genre_plays[genre] + plays[i]
            genre_list = genre_songs[genre]
            genre_list.append((i, plays[i]))
            
            # 가장 많이들은 노래 2개만 알면 되기때문에, 2개빼고 버림
            genre_songs[genre] = sorted(genre_list, key=lambda x : x[1], reverse=True)[:2]
        else:
            genre_plays[genre] = plays[i]
            genre_songs[genre] = [(i, plays[i])]

    # 가장 많이들은 순서대로 정렬
    sorted_genres_list = sorted(genre_plays.items(), key=lambda x : x[1], reverse=True)

    for value in sorted_genres_list:
        play_list = genre_songs[value[0]]
        for i in play_list:
            answer.append(i[0])
    return answer