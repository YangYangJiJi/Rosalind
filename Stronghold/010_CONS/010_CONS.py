#---------------------------- fasta 파일 읽기 ----------------------------
dna_sequence = []  # DNA 서열을 저장할 리스트
current_sequence = ""  # 현재 서열을 저장할 변수

with open("../data/rosalind_cons.txt", "r") as fasta_input:  # FASTA 파일 읽기
    for line in fasta_input:
        line = line.strip()  # 줄바꿈 제거
        
        if line.startswith(">"):  # FASTA 헤더 라인 확인
            if current_sequence:
                dna_sequence.append(current_sequence)  # 이전 서열 저장
                current_sequence = ""  # 새로운 서열을 위한 초기화
        else:
            current_sequence += line  # 서열 추가

    if current_sequence:  # 마지막 서열 추가
        dna_sequence.append(current_sequence)

#---------------------------- 염기 빈도수 세기 (profile matrix 생성) ----------------------------
dna_length = len(dna_sequence[0]) #DNA 길이 확인

# A, C, G, T 개수를 저장할 프로필 매트릭스 틀을 딕셔너리로 만듦
#KeyError 방지를 위해 먼저 0으로 초기화해야 함
profile = {
    'A' : [0] * dna_length, 
    'C' : [0] * dna_length,
    'G' : [0] * dna_length,
    'T' : [0] * dna_length
}

#---------------------------- 각 위치별로 A, C, G, T 개수 세기 ----------------------------
for sequence in dna_sequence:
    for i, base in enumerate(sequence):
        profile[base][i] += 1

'''
<profile[base][i] += 1> 추가설명
- profile은 { 'A': [0,0,0,0,0,0,0,0], ... } 형태의 2D 리스트
- 현재 base의 프로필 테이블에서 해당 위치(i) 카운트를 증가시킴.
'''


#---------------------------- 각 위치에서 가장 많이 등장한 염기 찾기 ----------------------------
consensus_sequence = "" #변수 생성

for i in range(dna_length) :
    max_base = max(profile, key=lambda x: profile[x][i]) #최대 빈도 염기 찾기
    consensus_sequence += max_base

#---------------------------- consensus sequence 출력 ----------------------------
print(consensus_sequence)
#profile matrix을 포맷 맞춰서 출력 (각 염기의 개수)
for base in "ACGT" : # base에는 "A" → "C" → "G" → "T" 순서로 값이 들어감
    print(f"{base}: {' '.join(map(str, profile[base]))}")













### output
'''
GTGATTATCACCACCAAGATCTATCGGATCACTAGATATAAAGAGCGGAACGGAAAAAGTGGTGATAATAACAAATTCGCATCCGTATAAGCACAGCTTTACGTCTAGCCCAACCCCAAGTTAAAGAGGCAGTCTTCCCAATTAGTTAACATAGTCGCAAATCAGATTTAGGACATAAAAAATCTACAGACAGCGGGACAAGAACGTCGAGCCTATAAATGTACGGAGACCACAAGAACCCCTCAAGTGTTAATAGACAAGAACGTGGTACGGAGATGTCCTCGAGACAAACTCAACTCTAATCCGGTAACGACTAAACAACGCTCAAATAATTCACCACCCAGCAAAACTCCGACAACCAAGACGGCCATATGGATGGTAAGTGTGTCTGTGAAGCGTGAACAAGACATTCAGAATTGACGCCGGAATGAACTATGAGTGGCTCAACCAGCATAGGCGAGGAGAATTACCCTCGAAACCCCCACCATAGAGGAAACCTAAACCGAAACCTTCAGCCCTAAGCTGTAATCAGACGAGAACACCAGGTAGACGTTACATGAGGGAGCATCACCCACCAGAAGAGCTTCTAAAAAACTGTACTTATACCAGCGATCATAAGAACAGAGCACCGCTCTCGTGCAGGACAAACTAACAGCGGTACTGAGGTCCACCTGGCCACAATTCACGGGCCAAAAAGTGCCGTCAGGGTAGATAATTACGTCAACCCAAACCACCGTAAAAAGTGCCCAACGTCCGAGCTCCGAGCTACACCAAACCCCGCACAAAAGGCAAGAAAAGGGCATGCCCATCTCCCTCACCGCTCACCCTATGGAGGACGAAGATGTCTCACTGGGTTCACAGCTGTAGACCCGCAATATAATGAGCTTTCCTGGCTGCGGAAATTTGACCTCAACGGGTAATGGACCAGGATCGGAATGGAGAGACGTCCCCCAA
A: 1 1 3 3 2 1 4 2 1 4 1 2 4 0 2 4 3 2 5 1 2 1 6 3 2 1 4 4 3 0 3 0 1 3 2 7 3 4 1 6 6 3 1 5 0 3 3 2 3 3 3 2 1 4 7 6 3 3 3 3 3 1 2 2 4 2 3 3 3 4 6 2 3 4 6 3 2 2 1 2 5 1 0 3 2 3 4 2 6 5 1 2 3 2 4 3 1 0 3 2 3 1 3 3 2 1 4 3 1 1 3 3 4 2 3 2 3 4 5 3 2 1 7 3 5 1 3 1 2 2 4 1 1 2 2 1 2 2 2 5 4 2 2 4 2 0 1 5 4 1 4 3 4 1 2 2 1 1 4 5 4 3 3 5 1 4 2 3 2 3 1 3 3 2 4 3 3 4 4 4 3 3 2 2 2 3 2 3 1 4 2 3 3 0 2 2 2 4 1 4 5 2 4 3 2 3 2 2 1 3 3 1 2 2 4 2 3 4 5 2 2 2 3 2 3 1 4 3 3 2 2 3 2 3 5 1 3 5 3 0 2 3 3 2 4 6 2 2 2 1 2 6 5 2 3 1 4 1 3 3 2 5 4 2 2 2 0 1 3 4 1 1 1 6 2 4 2 0 1 2 2 3 2 4 6 2 6 3 7 4 4 0 2 2 3 4 1 1 2 0 4 4 2 2 2 1 1 3 3 3 1 1 4 2 0 5 3 3 2 5 5 0 2 1 0 2 4 4 3 1 4 4 4 3 3 4 3 1 3 1 2 2 4 2 2 4 5 4 4 3 1 2 2 3 5 1 3 5 2 0 4 6 2 4 2 3 3 3 0 3 2 3 3 2 1 4 3 1 3 2 4 4 3 3 1 3 0 1 2 1 1 1 0 5 3 3 2 2 2 2 5 3 2 5 4 1 3 2 4 2 3 0 4 0 6 4 2 2 1 3 2 1 2 3 1 3 3 4 2 2 4 3 3 3 3 1 2 5 2 2 2 2 1 2 2 3 3 2 1 3 1 2 3 2 4 2 3 1 2 6 1 2 5 0 4 3 0 3 3 3 1 2 2 2 3 6 4 4 0 2 3 2 1 5 3 2 4 1 3 3 4 2 2 3 3 4 2 1 0 3 4 3 1 3 2 4 6 3 0 2 2 2 1 3 2 1 1 3 2 5 3 2 1 2 1 1 3 3 3 3 5 2 3 1 2 4 0 5 3 2 3 2 1 6 2 2 3 3 2 3 2 1 3 3 3 2 4 3 2 4 0 2 2 3 1 2 7 3 1 4 0 1 2 5 0 2 6 2 4 3 2 4 2 2 2 2 2 3 4 3 6 4 3 4 1 2 2 2 3 0 0 1 3 0 5 1 2 3 0 2 2 3 1 1 5 3 5 4 0 3 3 2 5 0 5 3 0 3 3 1 1 1 2 1 2 3 3 1 3 3 4 2 3 3 1 6 4 5 3 1 4 5 2 4 2 1 2 2 3 3 2 3 2 4 3 1 2 2 2 4 1 0 2 1 3 2 2 4 3 3 4 1 0 2 5 0 1 3 3 2 3 4 3 3 3 4 3 2 3 2 2 1 1 2 5 2 2 2 1 4 3 4 3 4 4 3 2 3 2 1 1 3 4 3 0 1 2 3 5 4 1 3 3 2 0 0 2 5 3 3 3 3 1 2 1 1 1 2 3 5 3 2 3 2 0 3 3 1 2 3 2 2 2 3 1 2 3 4 1 5 1 2 3 5 3 3 3 1 2 0 3 4 2 4 3 3 4 2 1 2 7 3 1 5 4 4 4 2 1 2 3 3 1 0 3 2 3 6 1 2 3 3 3 1 2 0 5 2 0 2 2 3 0 4 3 2 2 1 4 2 1 2 3 2 2 3 3 1 3 5 1 4 2 3 2 0 2 2 3 2 2 2 3 3 2 4 2 4 3 3 2 1 2 2 1 3 2 4 1 3 1 3 3 5 3 2 4 1 3 6 1 2 5 1 2 1 0 1 1 3 3 3 2 1 1 1 3 1 2 4 5 3 1 2 2 1 4 2 1 0 2 3 4 2 3 3 1 2 6 3 3 2 0 4 2 1 4 0 1 5 3 2 2 2 3 3 3 3 1 5 2 4 3 4 2 3 1 2 2 1 3 2 5 4
C: 3 3 1 2 0 3 3 2 5 3 5 4 2 4 4 2 3 3 2 1 3 3 1 0 3 2 0 0 2 6 3 4 4 3 2 3 1 0 3 2 2 1 3 4 2 4 1 2 3 3 4 2 2 3 3 2 2 2 2 1 1 1 2 1 2 2 3 1 2 1 2 3 3 0 2 1 2 3 3 3 0 1 5 5 1 2 3 2 2 2 1 4 3 5 1 2 5 3 0 2 3 4 2 1 6 3 0 2 4 5 4 3 3 3 5 4 4 2 2 3 2 2 1 1 3 1 3 2 2 5 1 1 2 3 1 2 5 4 4 3 4 3 3 3 1 4 3 3 1 5 3 2 2 3 2 3 2 3 2 0 2 0 6 1 2 0 3 1 2 2 3 0 3 4 2 1 2 3 1 2 2 1 2 4 1 1 6 3 1 2 4 2 1 4 1 2 2 1 3 1 2 1 3 3 4 1 1 3 3 2 0 5 3 3 3 2 2 3 1 1 2 2 2 4 0 1 1 2 1 4 5 3 5 2 2 0 3 2 4 4 6 5 1 5 2 2 2 2 2 2 0 1 2 2 1 1 2 5 2 2 3 3 3 5 2 1 1 3 2 2 4 3 2 1 3 4 1 1 2 5 3 1 4 1 1 1 3 4 1 2 2 4 2 4 1 2 4 3 4 2 1 1 2 3 3 2 0 2 2 2 5 2 2 4 3 2 1 3 4 1 2 6 2 4 3 3 3 1 3 3 3 2 0 1 4 0 4 7 2 6 4 4 3 3 3 3 3 1 2 4 1 5 4 2 2 3 1 0 3 4 1 3 3 2 3 1 1 4 7 3 1 1 3 2 2 2 1 2 1 2 0 1 0 2 0 1 2 3 3 2 1 3 2 0 3 1 4 2 2 3 1 2 3 2 1 1 2 5 4 1 1 4 4 2 1 2 2 2 3 1 3 2 4 4 2 0 3 1 3 2 2 3 5 1 1 1 2 2 2 1 2 2 3 2 3 1 2 4 4 3 0 3 3 3 3 2 2 4 2 1 1 2 1 3 1 3 2 0 3 4 5 3 2 3 2 2 0 2 5 5 4 4 4 1 4 4 0 2 2 0 2 1 2 1 2 1 4 5 3 1 2 2 3 4 1 4 0 3 4 4 1 3 5 2 2 6 5 4 1 1 1 1 3 2 3 1 3 3 1 4 1 3 2 3 1 2 2 3 3 3 3 4 5 1 3 2 1 3 2 2 4 2 1 2 3 5 4 1 2 1 2 2 2 3 1 5 1 2 3 3 5 5 4 0 5 4 2 3 1 3 3 2 1 4 2 1 3 2 2 3 4 1 2 3 5 2 2 2 3 7 3 2 2 4 2 3 4 2 3 4 2 3 0 4 1 1 2 1 2 2 3 4 1 2 2 3 7 3 5 5 2 4 1 4 2 4 1 3 2 4 3 2 1 2 6 2 3 3 4 2 2 1 3 1 2 4 2 2 1 2 3 2 1 1 2 1 1 4 3 1 4 4 2 3 1 3 3 3 4 2 2 3 3 3 0 5 2 2 2 3 4 2 2 2 3 1 3 1 2 4 3 3 3 4 0 2 1 2 1 1 1 1 0 4 1 2 0 2 3 1 4 4 2 2 4 5 5 3 2 4 5 4 3 3 4 1 2 2 3 1 2 2 3 2 3 5 4 4 3 2 4 0 0 6 7 2 3 2 7 0 5 3 1 3 1 3 2 1 4 3 5 3 2 0 2 4 4 5 4 1 4 3 3 1 3 3 2 0 3 4 2 3 3 1 3 2 3 3 3 0 4 2 3 3 4 4 4 1 1 5 3 4 4 5 2 5 1 4 6 2 5 0 6 3 4 5 5 2 3 2 4 3 3 2 2 2 5 1 3 1 3 3 2 0 1 4 3 5 2 4 1 2 3 1 1 1 4 1 6 2 3 3 2 2 2 2 1 1 3 5 4 3 5 1 3 2 1 2 3 2 1 3 1 0 3 1 2 3 5 5 1 1 2 4 3 3 4 0 2 2 2 2 3 1 2 1 2 4 4 2 6 2 2 4 1 1 2 1 1 1 1 0 3 3 5 5 0 1 1 2 2 4 2 0 2 2 1 2 2 1 2 1 2 3 3 2 3 4 3 6 4 3 1 2
G: 4 2 5 2 3 1 1 2 3 3 4 2 2 3 0 3 1 4 3 3 3 1 1 3 3 4 5 2 1 2 3 3 0 2 3 0 2 3 2 2 0 3 4 0 5 1 4 4 3 1 1 4 4 1 0 2 2 3 4 2 4 5 1 5 1 2 2 3 0 3 2 2 3 2 0 0 2 2 4 2 2 2 3 0 5 1 0 2 0 3 6 4 3 1 3 5 2 3 2 1 2 1 4 2 1 2 2 4 2 1 2 1 2 2 0 3 2 3 2 4 1 2 1 3 0 5 2 5 3 2 2 4 2 2 3 2 0 2 4 0 2 1 1 3 4 1 1 1 2 4 1 1 0 4 2 3 5 3 2 3 1 3 0 2 5 3 1 2 1 3 5 5 2 2 3 0 2 1 2 2 2 3 1 2 2 3 0 1 5 2 2 3 4 3 6 3 5 3 3 4 1 5 2 3 1 4 2 3 4 2 4 2 2 1 2 2 2 1 2 3 3 2 3 3 6 6 3 4 3 2 1 1 1 2 3 6 2 1 2 2 2 1 1 2 1 1 3 1 3 2 1 2 0 2 3 5 0 3 3 3 5 2 1 2 4 2 5 4 1 2 3 5 6 3 4 2 3 7 3 1 3 2 2 5 2 4 0 1 0 3 3 3 2 2 3 3 1 1 1 3 3 3 2 3 3 5 5 0 2 2 1 4 1 3 3 0 3 1 2 4 2 4 4 4 1 3 2 2 3 2 2 2 1 1 2 3 1 2 3 0 2 1 0 4 3 2 2 3 2 2 2 1 2 4 3 3 3 1 3 2 2 1 5 1 3 4 4 3 0 2 3 3 0 5 5 3 2 4 4 2 3 2 5 1 6 1 4 2 2 3 4 2 5 2 2 5 1 3 2 4 1 2 3 0 1 4 2 1 1 3 2 4 1 4 1 3 1 2 5 3 3 4 1 1 5 4 2 3 1 3 2 2 1 1 3 2 4 1 3 3 4 3 3 2 3 3 3 3 3 3 6 2 2 1 2 3 4 2 5 1 4 3 1 4 2 2 2 2 1 3 2 3 2 3 4 2 3 1 2 2 2 1 1 2 2 3 4 1 3 4 1 4 3 3 3 2 2 3 3 3 3 2 3 2 7 2 0 2 2 2 3 0 3 3 3 1 2 3 3 1 3 5 3 2 4 3 3 3 2 0 3 4 3 3 4 4 5 0 1 3 1 2 1 1 4 4 2 1 3 2 2 5 1 1 1 0 0 2 4 2 4 3 3 2 4 2 2 1 3 3 3 1 4 2 1 3 2 4 2 1 4 3 5 1 2 2 2 0 1 1 0 3 3 1 1 2 4 2 1 3 2 3 2 1 1 3 1 3 4 3 4 2 3 2 1 2 3 2 4 3 3 3 1 4 2 4 3 3 1 1 5 3 3 1 2 1 4 1 4 1 2 4 6 2 0 1 1 1 2 3 3 2 2 3 3 2 5 3 1 2 2 1 4 3 4 5 2 2 2 4 4 3 1 5 5 2 3 1 1 2 1 2 3 3 2 1 5 4 4 2 2 0 2 3 1 1 4 2 4 1 3 4 2 1 2 3 4 4 2 2 4 1 2 0 1 1 3 2 3 4 0 2 2 3 3 1 0 3 1 0 2 1 2 2 4 8 1 3 3 3 2 3 4 1 5 2 3 1 1 1 2 5 3 2 0 4 1 4 1 2 1 2 5 3 5 2 1 2 3 0 1 2 3 2 3 2 2 0 1 5 0 2 3 3 1 3 3 4 4 2 0 1 6 3 1 2 0 4 5 6 1 3 2 4 1 1 2 2 2 3 0 2 3 2 1 2 1 2 3 3 2 1 3 2 2 1 2 3 1 2 5 4 2 3 4 3 2 4 2 2 6 2 1 5 0 3 0 2 2 1 3 4 4 5 3 0 3 2 1 3 4 3 1 4 3 3 4 3 3 1 4 4 1 3 1 2 2 2 2 2 2 4 0 5 3 2 3 2 2 2 2 4 3 4 0 4 2 5 3 2 3 3 1 3 2 6 3 1 1 3 0 2 1 3 4 4 6 2 3 3 1 4 4 1 1 2 2 6 5 1 0 3 3 5 3 2 2 4 4 3 4 3 4 0 3 4 2 1 2 2 1 2 3 2
T: 2 4 1 3 5 5 2 4 1 0 0 2 2 3 4 1 3 1 0 5 2 5 2 4 2 3 1 4 4 2 1 3 5 2 3 0 4 3 4 0 2 3 2 1 3 2 2 2 1 3 2 2 3 2 0 0 3 2 1 4 2 3 5 2 3 4 2 3 5 2 0 3 1 4 2 6 4 3 2 3 3 6 2 2 2 4 3 4 2 0 2 0 1 2 2 0 2 4 5 5 2 4 1 4 1 4 4 1 3 3 1 3 1 3 2 1 1 1 1 0 5 5 1 3 2 3 2 2 3 1 3 4 5 3 4 5 3 2 0 2 0 4 4 0 3 5 5 1 3 0 2 4 4 2 4 2 2 3 2 2 3 4 1 2 2 3 4 4 5 2 1 2 2 2 1 6 3 2 3 2 3 3 5 2 5 3 2 3 3 2 2 2 2 3 1 3 1 2 3 1 2 2 1 1 3 2 5 2 2 3 3 2 3 4 1 4 3 2 2 4 3 4 2 1 1 2 2 1 3 2 2 3 2 3 0 3 2 2 1 4 0 1 5 1 3 1 3 5 3 5 7 1 3 4 3 3 4 1 2 2 0 0 2 1 2 5 4 2 4 2 2 1 1 0 1 0 4 2 4 2 2 4 2 0 1 3 1 2 2 1 1 3 4 2 3 1 4 5 3 5 2 2 4 2 2 2 4 5 3 3 3 3 3 1 4 3 3 3 2 0 1 0 2 1 6 2 1 3 1 4 1 2 5 5 1 3 2 0 2 3 2 3 3 1 2 1 0 2 2 1 6 2 2 1 0 3 3 4 2 4 3 0 0 3 2 2 2 0 3 2 4 3 4 1 2 1 4 3 2 4 3 3 2 4 3 5 4 4 3 4 4 4 3 3 2 1 3 3 4 1 3 3 2 3 4 4 3 2 1 4 4 2 1 4 2 1 5 4 1 3 2 3 3 2 2 3 2 2 4 3 2 2 1 5 3 6 2 2 3 4 2 3 3 4 2 3 2 1 2 1 3 3 2 4 1 3 1 3 1 2 4 3 3 3 3 2 6 5 3 0 2 2 4 2 1 0 3 3 3 1 1 3 4 2 1 1 2 6 2 3 3 3 3 3 2 3 2 1 4 3 1 3 3 1 0 0 4 2 4 2 4 5 1 2 3 2 2 0 4 3 3 2 3 4 2 5 1 1 4 3 1 1 2 3 3 0 3 2 3 2 3 2 3 2 1 2 4 3 3 3 2 2 5 4 3 3 2 4 2 3 4 3 3 2 4 1 0 4 3 0 2 3 0 3 4 1 0 1 3 3 1 1 2 3 4 5 3 5 3 3 0 2 2 2 3 4 2 4 3 0 5 4 3 5 2 3 3 2 3 1 2 2 6 3 3 4 0 3 4 2 1 1 3 4 1 0 0 1 1 3 2 2 4 4 4 2 2 5 1 2 1 2 0 3 3 1 2 1 1 4 1 2 3 2 3 3 1 3 5 3 3 4 3 2 1 3 5 2 3 1 1 3 5 1 1 3 2 2 2 3 3 4 4 2 3 4 2 1 1 3 1 4 3 2 3 4 0 5 1 3 2 2 4 3 3 3 3 2 6 3 2 4 5 2 4 4 5 3 2 4 5 1 2 2 3 3 3 1 2 2 2 2 2 3 2 1 5 0 1 3 3 2 2 5 1 2 2 3 3 2 1 3 4 0 3 1 3 3 0 5 2 3 2 1 3 3 4 3 2 2 3 3 2 3 2 1 1 4 3 4 3 1 2 2 3 1 1 4 2 2 1 3 0 1 2 2 3 1 1 2 2 2 4 3 2 3 1 1 6 0 4 1 0 2 5 3 3 2 1 3 1 6 1 1 1 2 1 4 2 4 0 1 2 3 2 2 0 4 2 2 0 1 5 2 7 3 5 1 3 3 4 2 0 1 4 5 1 3 0 2 1 3 5 2 4 2 3 2 3 1 1 0 1 1 3 4 3 5 2 0 6 1 4 4 2 6 5 4 2 0 4 2 3 1 6 2 1 4 3 2 0 2 5 4 4 2 1 3 4 5 2 3 3 1 2 2 1 5 0 3 5 4 3 2 2 2 4 3 3 2 5 1 3 3 2 3 4 1 3 1 2 2 1 3 2 1 4 3 3 1 2 3 1 2
'''