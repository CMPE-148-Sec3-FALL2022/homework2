# Chapter 2 Problems

### P1 -> P4
1. True or false?
    1. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.<br>
    ***FALSE***
    2. Two distinct Web pages (for example, www.mit.edu/research.html and www.mit.edu/students.html ) can be sent over the same persistent connection.<br>
    ***TRUE***
    3. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages.<br>
    ***FALSE***
    4. The Date: header in the HTTP response message indicates when the object in the response was last modified.<br>
    ***FALSE***
    5.  HTTP response messages never have an empty message body.<br>
    ***FALSE***
2. SMS, iMessage, and WhatsApp are all smartphone real-time messaging systems. After doing some research on the Internet, for each of these systems write one paragraph about the protocols they use. Then write a paragraph explaining how they differ.
    - SMS can send text up to 160 characters long. In implementation this means that if a longer text is sent, it either splits up the message, or gets switched to using MMS instead. It uses the SMPP protocol and can be communicated over many kinds of cellular networks. 
    - iMessage seems similar to SMS but uses completely different network pathways. It uses the standard internet stack to do the lifting of the data through the network. This allows for larger content to be sent across iMessage than with SMS. Apple uses a proprietary protocol called APNS.
    - WhatsApp is similar to iMessage in its implementation and internet requirement and they way it carries data around the network. The difference being that Facebook (Meta) owns WhatsApp and this app in particular uses a protocol called XMPP.
    - The SMS is the most different from iMessage and WhatsApp, as it works over the cellular network, and doesnt require internet. SMS is also farily insecure as the data is not usually encrypted. iMessage and WhatsApp messages are encrypted and stored in the cloud, and this also allows them to be backed up in a fairly simple way as well.
3. Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and application-layer protocols besides HTTP are needed in this scenario?
    - Application: HTTP, DNS
    - Transport: TCP for sending HTTP, and UDP for sending DNS
4. Consider the following string of ASCII characters that were captured by Wireshark when the browser sent an HTTP GET message (i.e., this is the actual content of an HTTP GET message). The characters `<cr><lf>` are carriage return and line-feed characters (that is, the italized character string `<cr>` in the text below represents the single carriage-return character that was contained at that point in the HTTP header). Answer the following questions, indicating where in the HTTP GET message below you find the answer.<br>`
GET /cs453/index.html HTTP/1.1<cr><lf>Host: gaia.cs.umass.edu<cr><lf>User-Agent: Mozilla/5.0 ( Windows;U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax) <cr><lf>Accept:ext/xml, application/xml, application/xhtml+xml, text/html;q=0.9, text/plain;q=0.8, image/png,*/*;q=0.5<cr><lf>Accept-Language: en-us, en;q=0.5<cr><lf>Accept-Encoding: zip, deflate<cr><lf>Accept-Charset: ISO-8859-1, utf-8;q=0.7,*;q=0.7<cr><lf>Keep-Alive: 300<cr><lf>Connection:keep-alive<cr><lf><cr><lf>`
    1. What is the URL of the document requested by the browser?
        - `http://gaia.cs.umass.edu/cs453/index.html` As determined by the address and request location combined.
    2. What version of HTTP is the browser running?
        - `HTTP Version 1.1` As indicated before the Host field.
    3. Does the browser request a non-persistent or a persistent connection?
        - PERSISTENT as indicated by the (Keep-Alive) mesage
    4. What is the IP address of the host on which the browser is running?
        - The IP address is not shown in the message
    5. What type of browser initiates this message? Why is the browser type needed in an HTTP request message?
        - `Mozilla 5.0` as indicated by `User-Agent: Mozilla/5.0`. The browser type is needed in case a certain browser needs a different kind of way of rendering the message

### P25 -> P32
25. Consider an overlay network with N active peers, with each pair of peers having an active TCP connection. Additionally, suppose that the TCP connections pass through a total of M routers. How many nodes and edges are there in the corresponding overlay network?
    - `Nodes = M`<br>
    `Edges = (N*M)/2`
26. Suppose Bob joins a BitTorrent torrent, but he does not want to upload any data to any other peers (so called free-riding).
    1. Yes Bob can get a complete copy, because the **seeders** in the network will give all the parts over time.
    2. It doesnt seem like Bob can make it go faster, while still not seeding the network. But if he did add computers to the network as seeders, it would increase th throughput ability of the network.
27. Consider a DASH system for which there are N video versions (at N different rates and qualities) and N audio versions (at N different rates and qualities). Suppose we want to allow the player to choose at any time any of the N video versions and any of the N audio versions.
    1. If we create files so that the audio is mixed in with the video, so server sends only one media stream at given time, how many files will the server need to store (each a different URL)?
        - `NV = N video streams`<br>
        `NA = N audio streams`<br>
        If combined there will be `NV * NA` different files and URLs.
    2. If the server instead sends the audio and video streams separately and has the client synchronize the streams, how many files will the server need to store?
        - Only `NA + NV` unique files need to be stored.
28. Install and compile the Python programs TCPClient and UDPClient on one host and TCPServer and UDPServer on another host.
    1. Suppose you run TCPClient before you run TCPServer. What happens? Why?
        - The TCP client will not find the server and error out. TCP connections require a server to be up first. It is possible that the client could loop checking until a server is up though.
    2. Suppose you run UDPClient before you run UDPServer. What happens? Why?
        - Nothing of note will happen, and the client and server will function as expected because UDP does not require a server connection before transfer.
    3. What happens if you use different port numbers for the client and server sides?
        - Then communication will attempt to happen on the wrong ports and will result in errors. TCP client needs to know the port of the server. And the UDP server needs to know the port of the client.
29. Suppose that in UDPClient.py, after we create the socket, we add the line:<br>
`clientSocket.bind((’’, 5432))`<br>
Will it become necessary to change UDPServer.py? What are the port numbers for the sockets in UDPClient and UDPServer? What were they before making this change?
    - This will not really do anything, ad the only change that happens is that the client port is hardcoded. The server will still respond on the port that it is contacted on.
30. Can you configure your browser to open multiple simultaneous connections to a Web site? What are the advantages and disadvantages of having a large number of simultaneous TCP connections?
    - Yes you can do that.<br>
    **Advantages:** Many things can be recieved at once instead of waiting for them to come in order.<br>
    **Disadvantages:** Each individual page will load slower as the congestion on the network will be greater in some scenarios.
31. We have seen that Internet TCP sockets treat the data being sent as a byte stream but UDP sockets recognize message boundaries. What are one advantage and one disadvantage of byte-oriented API versus having the API explicitly recognize and preserve application-defined message boundaries?
    - Items will come in an expected order and a trustworthy stream is created. But if somehow a single piece of data is lost, the whole message is invalid.
32. What is the Apache Web server? How much does it cost? What functionality does it currently have? You may want to look at Wikipedia to answer this question.
    - An Apache Web Server is an open source system for creating and deploying web servers. It is free, as it is open source. It has almost anything you would expect in a modern webserver framework.