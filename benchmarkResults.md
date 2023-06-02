### GET

- Concurrency Level:      10
- Time taken for tests:   10.126 seconds
- Complete requests:      106
Failed requests:        0
Total transferred:      199269631 bytes
HTML transferred:       199250157 bytes
- Requests per second:    10.47 [#/sec] (mean)
- Time per request:       955.318 [ms] (mean)
Time per request:       95.532 [ms] (mean, across all concurrent requests)
Transfer rate:          19217.07 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.8      0       4
Processing:   133  892 206.5    893    1382
Waiting:      128  818 196.8    813    1286
Total:        133  893 206.6    895    1382

Percentage of the requests served within a certain time (ms)
  50%    895
  66%    966
  75%   1016
  80%   1077
  90%   1159
  95%   1252
  98%   1285
  99%   1286
 100%   1382 (longest request)

 ### PUT
Concurrency Level:      10
Time taken for tests:   10.002 seconds
Complete requests:      9114
Failed requests:        0
Total transferred:      2333952 bytes
Total body sent:        2088938
HTML transferred:       720243 bytes
Requests per second:    911.23 [#/sec] (mean)
Time per request:       10.974 [ms] (mean)
Time per request:       1.097 [ms] (mean, across all concurrent requests)
Transfer rate:          227.88 [Kbytes/sec] received
                        203.96 kb/s sent
                        431.84 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.4      0      66
Processing:     3   11   9.2      8     100
Waiting:        2   10   9.0      7      99
Total:          3   11   9.3      8     100

Percentage of the requests served within a certain time (ms)
  50%      8
  66%      9
  75%     10
  80%     11
  90%     20
  95%     30
  98%     39
  99%     54
 100%    100 (longest request)

 ### POST
 Concurrency Level:      10
Time taken for tests:   10.000 seconds
Complete requests:      9561
Failed requests:        0
Total transferred:      2744185 bytes
Total body sent:        2431034
HTML transferred:       1042149 bytes
Requests per second:    956.09 [#/sec] (mean)
Time per request:       10.459 [ms] (mean)
Time per request:       1.046 [ms] (mean, across all concurrent requests)
Transfer rate:          267.98 [Kbytes/sec] received
                        237.40 kb/s sent
                        505.39 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.8      0      66
Processing:     1   10   8.3      8     110
Waiting:        1   10   8.3      7     110
Total:          1   10   8.3      8     110

Percentage of the requests served within a certain time (ms)
  50%      8
  66%     10
  75%     11
  80%     13
  90%     20
  95%     25
  98%     37
  99%     45
 100%    110 (longest request)