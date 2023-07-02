def to_minutes(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def solution(book_time):
    # 각 예약을 시작 시간, 끝나는 시간 + 청소 시간(분)으로 변환
    book_time = [(to_minutes(s), to_minutes(e) + 10) for s, e in book_time]
    # 시작 시간으로 정렬
    book_time.sort()

    rooms = []
    for start, end in book_time:
        # 사용 가능한 방 찾기
        for i in range(len(rooms)):
            if rooms[i] <= start:
                rooms[i] = end
                break
        else:  # 사용 가능한 방이 없는 경우
            rooms.append(end)  # 새로운 방 추가

    return len(rooms)
