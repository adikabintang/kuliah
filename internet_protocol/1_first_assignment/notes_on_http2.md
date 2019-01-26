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
- Each stream as a _unique identifier_ and _optional priority identifier_ that is used to carry bidirectional messages.
- Each HTTP2 message consists of one or more HTTP2 frames
- Frames from different streams may be interleaved and then reassembled via the embedded stream identifier in the header of each frame.
![HTTP2 streams](https://developers.google.com/web/fundamentals/performance/http2/images/streams_messages_frames01.svg)

### Request and response multiplexing
...