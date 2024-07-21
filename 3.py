import timeit

with open('article1.txt', 'r', ) as file:
    article1 = file.read()

with open('article2.txt', 'r', ) as file:
    article2 = file.read()


#алгоритм бойєра-мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    skip = {chr(i): m for i in range(256)}
    
    for k in range(m - 1):
        skip[pattern[k]] = m - k - 1
    
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m) 
    return -1



#алгоритм кнутта-морріса-пратта
def kmp_search(text, pattern):
    def compute_lps_array(pattern):
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

    lps = compute_lps_array(pattern)
    i = 0
    j = 0
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


#алгоритм рабіна-карпа
def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    if m > n:
        return -1

    for i in range(m-1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


#підрядки
pattern_exist_article1 = "Лінійний пошук можна використовувати для малого, несортоване набору даних, який не збільшується в розмірах."
pattern_nonexist_article1 = "Зв’язний список (linked list) – це структура даних, у якій кожен елемент має вказівник на наступний елемент"
pattern_exist_article2 = "Наявність такої великої кількості різних методів реалізації баз даних та представлення інформації, що можна використати при побудові рекомендаційних систем, викликає необхідність порівняльного аналізу та вибору оптимального методу і структури даних для зберігання інформації рекомендаційних систем."
pattern_nonexist_article2 = "Двійковий або логарифмічний пошук часто використовується через швидкий час пошуку"

#вимірювання часу
time_boyer_moore_exist_article1 = timeit.timeit(lambda: boyer_moore(article1, pattern_exist_article1), number=100)
time_boyer_moore_nonexist_article1 = timeit.timeit(lambda: boyer_moore(article1, pattern_nonexist_article1), number=100)

time_kmp_exist_article1 = timeit.timeit(lambda: kmp_search(article1, pattern_exist_article1), number=100)
time_kmp_nonexist_article1 = timeit.timeit(lambda: kmp_search(article1, pattern_nonexist_article1), number=100)

time_rabin_karp_exist_article1 = timeit.timeit(lambda: rabin_karp(article1, pattern_exist_article1), number=100)
time_rabin_karp_nonexist_article1 = timeit.timeit(lambda: rabin_karp(article1, pattern_nonexist_article1), number=100)

time_boyer_moore_exist_article2 = timeit.timeit(lambda: boyer_moore(article2, pattern_exist_article2), number=100)
time_boyer_moore_nonexist_article2 = timeit.timeit(lambda: boyer_moore(article2, pattern_nonexist_article2), number=100)

time_kmp_exist_article2 = timeit.timeit(lambda: kmp_search(article2, pattern_exist_article2), number=100)
time_kmp_nonexist_article2 = timeit.timeit(lambda: kmp_search(article2, pattern_nonexist_article2), number=100)

time_rabin_karp_exist_article2 = timeit.timeit(lambda: rabin_karp(article2, pattern_exist_article2), number=100)
time_rabin_karp_nonexist_article2 = timeit.timeit(lambda: rabin_karp(article2, pattern_nonexist_article2), number=100)

results = {
    'Article 1': {
        'Existing': {
            'Boyer-Moore': time_boyer_moore_exist_article1,
            'KMP': time_kmp_exist_article1,
            'Rabin-Karp': time_rabin_karp_exist_article1
        },
        'Non-Existing': {
            'Boyer-Moore': time_boyer_moore_nonexist_article1,
            'KMP': time_kmp_nonexist_article1,
            'Rabin-Karp': time_rabin_karp_nonexist_article1
        }
    },
    'Article 2': {
        'Existing': {
            'Boyer-Moore': time_boyer_moore_exist_article2,
            'KMP': time_kmp_exist_article2,
            'Rabin-Karp': time_rabin_karp_exist_article2
        },
        'Non-Existing': {
            'Boyer-Moore': time_boyer_moore_nonexist_article2,
            'KMP': time_kmp_nonexist_article2,
            'Rabin-Karp': time_rabin_karp_nonexist_article2
        }
    }
}

#визначення найшвидшого алгоритму для кожного тексту
for article, data in results.items():
    for pattern_type, times in data.items():
        fastest_algorithm = min(times, key=times.get)
        print(f"The fastest algorithm for {pattern_type} pattern in {article} is {fastest_algorithm} with time {times[fastest_algorithm]}")

#визначення найшвидшого алгоритму загалом
total_times = {'Boyer-Moore': 0, 'KMP': 0, 'Rabin-Karp': 0}
for article, data in results.items():
    for pattern_type, times in data.items():
        for algorithm, time in times.items():
            total_times[algorithm] += time

overall_fastest_algorithm = min(total_times, key=total_times.get)
print(f"The fastest algorithm is {overall_fastest_algorithm} with total time {total_times[overall_fastest_algorithm]}")
