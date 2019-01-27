# Understanding HTTP2, The Basics
This note is taken from here: https://developers.google.com/web/fundamentals/performance/http2/ 

## Design Goal
HTTP2 focuses more on performance.

## What's New
### Binary Framing Layer
According to [[1]](https://developer.ibm.com/articles/wa-http2-under-the-hood/#binary-protocol), it means the same with "HTTP2 as a binary protocol". 

Now, what is binary protocol?

Consider this HTTP1.1 request and response:

Request
```
GET
Host: google.com
```

Response:
```
HTTP/1.1 200 OK
Content-Length: 6969  // look at this, hint (1)
```

HTTP1.1 is a text protocol. It means that the number 6969 in Content-Length is represented in string (['6', '9', '6', '9']). In contrast, if it's a binary protocol, that 6969 would be presented as 0d6969 (the number 6969 in decimal format). Here are good explanations from stackoverflow [[1]](https://stackoverflow.com/questions/2645009/binary-protocols-v-text-protocols) [[2]](https://stackoverflow.com/questions/2364581/binary-vs-text-protocols).

![HTTP2 binary protocol](https://developers.google.com/web/fundamentals/performance/http2/images/binary_framing_layer01.svg)

### Streams, messages, and frames
HTTP2 terminology:
- _Stream_: A bidirectional flow of bytes within an established connection.
- _Message_: A complete sequence of frames that map to a logical request or response message.
- _Frame_: The smallest unit of communication in HTTP2. Think of the term "TCP frame", now think of "HTTP2 frame". Huh?

The relation of these terms:
- All communication is performed over a single TCP connection that can carry any number of streams. Yes, multiplexed.
- Each stream has a _unique identifier_ and _optional priority identifier_ that is used to carry bidirectional messages.
- Each HTTP2 message consists of one or more HTTP2 frames
- Frames from different streams may be interleaved and then reassembled via the embedded stream identifier in the header of each frame.
![HTTP2 streams](https://developers.google.com/web/fundamentals/performance/http2/images/streams_messages_frames01.svg)

### Request and response multiplexing
In HTTP1.1, there is no multiplexing. As a result, each HTTP1.1 request is done by one TCP connection [[3]](https://hpbn.co/http1x/#using-multiple-tcp-connections). Most browsers are able to open 6 TCP connections at a time.

The picture below shows that HTTP2 can break down HTTP2 message into independent frames, interleave them, and reassemble them on the other ends. 

![Multiplexing](https://developers.google.com/web/fundamentals/performance/http2/images/multiplexing01.svg)

The picture also shows that on a single connection, there are 3 streams: stream 1, stream 3, and stream 5. This multiplexing brings some advantages:
- Interleave multiple requests and response in parallel
- Use a single connection to deliver multiple requests and response in parallel
- Deliver lower page load times by eliminating unnecessary latency and improving utilization of available network capacity

### Stream prioritization
Once an HTTP message is split into many frames, the frames from multiple streams is multiplexed, HTTP2 has mechanism to interleave these streams. 

How?
- Each stream may be assigned an integer weight between 1 and 256
- Each stream may be given an explicit dependency on another stream

Huh? OK. Example:

![Stream](https://developers.google.com/web/fundamentals/performance/http2/images/stream_prioritization01.svg)

Focus on the first two from the left:
1. A and B are said to be dependent on the implicit "root stream". A does not depend on B. A has weight 12, B has 4. Therefore, stream A should receive 12/(12+4) of available resource. B should receive 4/(12+4) of available resource
2. C depends on D. C should receive full available resource. Weight does not matter here since C should be processed after D.

Stream dependencies and weights express a transport reference, not a requirement. Therefore, it does not guarantee the transmission order.