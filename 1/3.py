import timeit


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    shifts = 0
    while shifts <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1
        if j < 0:
            return shifts
        else:
            shifts += max(1, j - bad_char.get(text[shifts + j], -1))
    return -1


def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    h = pow(d, m - 1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1


with open('стаття 1.txt', 'r', encoding='cp1251') as file1:
    text1 = file1.read()

with open('стаття 2.txt', 'r', encoding='cp1251') as file2:
    text2 = file2.read()


existing_substring = "алгоритм"
non_existing_substring = "вигаданийпідрядок"


def run_search_tests(text, pattern, algorithm):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)


results = {
    'Boyer-Moore (Existing Substring)': run_search_tests(text1, existing_substring, boyer_moore),
    'Boyer-Moore (Non-existing Substring)': run_search_tests(text1, non_existing_substring, boyer_moore),
    'KMP (Existing Substring)': run_search_tests(text1, existing_substring, kmp_search),
    'KMP (Non-existing Substring)': run_search_tests(text1, non_existing_substring, kmp_search),
    'Rabin-Karp (Existing Substring)': run_search_tests(text1, existing_substring, rabin_karp),
    'Rabin-Karp (Non-existing Substring)': run_search_tests(text1, non_existing_substring, rabin_karp),

    'Boyer-Moore (Existing Substring) 2': run_search_tests(text2, existing_substring, boyer_moore),
    'Boyer-Moore (Non-existing Substring) 2': run_search_tests(text2, non_existing_substring, boyer_moore),
    'KMP (Existing Substring) 2': run_search_tests(text2, existing_substring, kmp_search),
    'KMP (Non-existing Substring) 2': run_search_tests(text2, non_existing_substring, kmp_search),
    'Rabin-Karp (Existing Substring) 2': run_search_tests(text2, existing_substring, rabin_karp),
    'Rabin-Karp (Non-existing Substring) 2': run_search_tests(text2, non_existing_substring, rabin_karp),
}

for key, value in results.items():
    print(f'{key}: {value:.6f} seconds')
