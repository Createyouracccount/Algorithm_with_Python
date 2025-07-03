def solution(n, w, num):
    # 각 상자의 위치 저장: 인덱스 = 상자 번호 (1-based)
    positions = [None] * (n + 1)
    
    for i in range(n):
        box_num = i + 1
        layer = i // w        # 층 번호
        index_in_layer = i % w
        
        # 짝수층: 좌 -> 우 / 홀수층: 우 -> 좌
        if layer % 2 == 0:
            col = index_in_layer
        else:
            col = w - 1 - index_in_layer
        
        positions[box_num] = (layer, col)

    # 꺼내려는 상자의 위치
    target_layer, target_col = positions[num]
    count = 0

    # 위층에 있는 상자들 중, 같은 열에 있는 상자만 센다
    for i in range(1, n + 1):
        layer, col = positions[i]
        if layer > target_layer and col == target_col:
            count += 1

    return count + 1  # 자기 자신도 포함
