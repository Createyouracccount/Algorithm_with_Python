def solution(s):
    # 각 단어를 공백을 기준으로 분리한다.
    words = s.split(' ')
    
    # 각 단어를 JadenCase로 변환합니다.
    jaden_case_words = []
    for word in words:
        if len(word) > 0: # len(word)의 길이가 길다면?
            # 첫 문자가 알파벳이면 대문자로 변환한다.
            # 아니면 그대로 두고 나머지 문자는 소문자로 변환한다.
            jaden_case_word = word[0].upper() + word[1:].lower()
        else:
            # 단어가 빈 문자열인 경우 (공백이 연속으로 나올 때)
            jaden_case_word = ''
        jaden_case_words.append(jaden_case_word)
    
    # 변환된 단어들을 공백으로 이어붙여 최종 문자열을 만든다.
    return ' '.join(jaden_case_words)