## Веб-сервер частично реализующий протокол HTTP
### Описание
Сервер частично реализующий протокол HTTP, в частности методы GET и HEAD.




### Нагрузочный тест сервера

* Ubuntu 22.04.4 LTS
* Intel® Xeon(R) CPU E3-1270 v3 @ 3.50GHz × 8
* 8Gb RAM

Тестирование производилось с помощью *ApacheBench*:
sh ab -n 1000 -c 10 http://localhost:8080/index.html

__Результаты__
```
This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        MyTestServer
Server Hostname:        localhost
Server Port:            8080

Document Path:          /index.html
Document Length:        169 bytes

Concurrency Level:      10
Time taken for tests:   0.309 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      309000 bytes
HTML transferred:       169000 bytes
Requests per second:    3233.59 [#/sec] (mean)
Time per request:       3.093 [ms] (mean)
Time per request:       0.309 [ms] (mean, across all concurrent requests)
Transfer rate:          975.76 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     1    2   0.5      2       5
Waiting:        1    2   0.5      2       5
Total:          1    2   0.5      2       5

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      3
  90%      3
  95%      3
  98%      3
  99%      4
 100%      5 (longest request)

```


### Совместимость
Python 3.6 +
