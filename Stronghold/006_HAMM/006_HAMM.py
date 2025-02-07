with open('../data/rosalind_hamm.txt') as input_data :
    lines = input_data.read().splitlines() # 줄 단위로 읽어 리스트로 반환
    s = lines[0] #첫번재 줄을 s에 저장
    t = lines[1] #두번째 줄을 t에 저장

'''
def count_point_mut(seq1,seq2):
    mut = 0
    for i in range(len(seq1)) :
        if seq1[i] != seq2[i] :
            mut += 1   #mut = mut + 1과 같은 말
    return mut
'''

# zip()을 사용해서 두 문자열을 쉽게 한 쌍씩 비교
hamm = sum(1 for a, b in zip(s, t) if a != b)
print(hamm)

count_point_mut(s, t)

#출력결과 : 492
