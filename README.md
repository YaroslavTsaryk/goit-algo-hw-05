# goit-algo-hw-05

Найшвидший алгоритм пошуку в тексті - boyer_moore_search.
Час виконання пошуку існуючого рядка склав 0.0014 сек для файлу 12 кБ, і 0.005 сек для файлу 18 кБ.
Для неіснуючих пошук тривав 0.0025 сек

kmp_search і rabin_karp_search мають час виконаня 0.01 і 0.02 для існуючих  і неіснуючих рядків.


|file   |substr|method              |time                    |
|-------|------|--------------------|------------------------|
| data1 | str1 | kmp_search         |   0.010317399981431663 |
| data2 | str2 | kmp_search         |   0.008802800002740696 |
| data1 | str1 | boyer_moore_search |  0.0014466999855358154 |
| data2 | str2 | boyer_moore_search |   0.005375999986426905 |
| data1 | str1 | rabin_karp_search  |   0.014775799994822592 |
| data2 | str2 | rabin_karp_search  |    0.02303599999868311 |
|                False search                                |
| data1 | str2 | kmp_search         |   0.007410799997160211 |
| data2 | str1 | kmp_search         |   0.011130600003525615 |
| data1 | str2 | boyer_moore_search |  0.0025061999913305044 |
| data2 | str1 | boyer_moore_search |   0.002525099989725277 |
| data1 | str2 | rabin_karp_search  |   0.010436900018248707 |
| data2 | str1 | rabin_karp_search  |   0.019885399990016595 |
