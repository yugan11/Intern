def subsequence(list):
    sorted_list = sorted(list)   
    min_sum_subseq = []
    current_sum = 0
    for num in sorted_list:
        min_sum_subseq.append(num)
        current_sum += num   
    return min_sum_subseq
list = [3, 1, 4, 2, 5]
result = subsequence(list)
print("Minimum sum subsequence:", result)
