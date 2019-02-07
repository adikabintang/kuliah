# Part 1
- Create a HTTP2 server and client
- GET, POST, PUT
- upload image
- get json
- receive notification with server push

# part 2
select 2 of 4 features: flow control, stream priority, multiplexing, and server push.
analyze its:
- the day of data transmissions
- amount of traffic
- throughput
- latency

Use wireshark and other tools needed. Repeat the experiment > 3 times.
Instructions of how to compare in the experiment:
- HTTP1.1 vs HTTP2
or
- HTTP2 with features enabled/disabled (for example, disabling/enabling multiplexing)

# Notes
https://jimshaver.net/2015/02/11/decrypting-tls-browser-traffic-with-wireshark-the-easy-way/
how to get the sslkeylog
export SSLKEYLOGFILE=$HOME/sslkeylog.log
then open firefox from the same terminal 