def solution(genres, plays):
    genre_sum = {}
    genre_songs = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_sum[genre] = genre_sum.get(genre, 0) + play
        if genre not in genre_songs:
            genre_songs[genre] = []
        genre_songs[genre].append((play, i))

    sorted_genres = sorted(
        genre_sum,
        key=lambda genre: genre_sum[genre],
        reverse=True
    )

    answer = []

    for genre in sorted_genres:
        genre_songs[genre].sort(key=lambda x: (-x[0], x[1]))
        for play, index in genre_songs[genre][:2]:
            answer.append(index)

    return answer