# goit-algo-hw-05

Найшвидший алгоритм пошуку в тексті - boyer_moore_search.
Час виконання пошуку існуючого рядка склав 0.0014 сек для файлу 12 кБ, і 0.005 сек для файлу 18 кБ.
Для неіснуючих пошук тривав 0.0025 сек

kmp_search і rabin_karp_search мають час виконаня 0.01 і 0.02 для існуючих  і неіснуючих рядків.


|file   |substr|method              |time                    |
|-------|------|--------------------|------------------------|
|                        True search                         |
| data1 | str1 | kmp_search         |   0.011530800024047494 |
| data2 | str2 | kmp_search         |   0.011046500003430992 |
| data1 | str1 | boyer_moore_search |  0.0021912999800406396 |
| data2 | str2 | boyer_moore_search |   0.004331200005253777 |
| data1 | str1 | rabin_karp_search  |   0.009207800001604483 |
| data2 | str2 | rabin_karp_search  |   0.017453599983127788 |
|                        False search                        |
| data1 | str2 | kmp_search         |   0.006199600000400096 |
| data2 | str1 | kmp_search         |   0.015102700010174885 |
| data1 | str2 | boyer_moore_search |  0.0018103999900631607 |
| data2 | str1 | boyer_moore_search |  0.0021775999921374023 |
| data1 | str2 | rabin_karp_search  |   0.013114000001223758 |
| data2 | str1 | rabin_karp_search  |   0.019168200000422075 |
