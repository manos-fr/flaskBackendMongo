## GET

### This is ApacheBench, Version 2.3 <$Revision: 1901567 $>

Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Finished 73 requests

Server Software: Werkzeug/1.0.1
Server Hostname: 127.0.0.1
Server Port: 3000

Document Path: /titles
Document Length: 3112346 bytes

Concurrency Level: 10
Time taken for tests: 10.194 seconds
Complete requests: 73
Failed requests: 0
Total transferred: 227214617 bytes
HTML transferred: 227201258 bytes
Requests per second: 7.16 [#/sec] (mean)
Time per request: 1396.433 [ms] (mean)
Time per request: 139.643 [ms] (mean, across all concurrent requests)
Transfer rate: 21766.74 [Kbytes/sec] received

Connection Times (ms)
min mean[+/-sd] median max
Connect: 0 0 0.2 0 1
Processing: 225 1259 215.5 1300 2084
Waiting: 222 1201 223.5 1261 1980
Total: 225 1259 215.4 1300 2084

Percentage of the requests served within a certain time (ms)
50% 1299
66% 1315
75% 1328
80% 1341
90% 1406
95% 1496
98% 1886
99% 2084
100% 2084 (longest request)
