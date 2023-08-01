Buffers:
    binary numbers: only contains 0 and 1

    base 16 numbers: 0X456 is a hexa decimal or base16 number, this means
    we multiply each number by 16 raised to the power of its index to get the final number
    the range is from 0 to 15 represented by 0 to F
    The advantage of using hexa decimal numbers is that they allow us to represent
    a large number in less number of characters compared to decimal and binary numbers

    Character sets: letters and symbols that a writing system uses, and a representation of 
    assigning different numbers to those characters
        unicode and ASCII
    
    Character Encoding: A system of assigning a sequence of bytes to a character
    the most common one is utf-8, defined by the unicode standard, therefore its characters have 
    the same numbers as the Unicode

    Buffers: Buffer is a container in memory that has a fixed size, that gets in some raw binary data
    and it sends it to another place. along the way we do some processing on it.
    the buffer corresponds to memory allocated outside of V8
    its a place that is used to temporarily hold binary data. they are not resizable

    JS dont have a mechanism to deal with raw binary data, Nodejs to deal with file and http has to have a 
    mechanism to deal with binary data, so we have buffers

    nodejs uses buffers to encode and decode URLs, if you have any characeter that is not english in your url
    it will be converted into a hex code and included as query param in the URL

    https://www.youtube.com/watch?v=QZIeZM-yXXU&ab_channel=Cododev

    let buff = Buffer.from("23","hex")
    console.log(buff.toString("utf-8"))

______________________________________
Streams: They are data-handling method and are used to read or write input into output sequentially.

Readable Streams:
    HTTP responses, on the client
    HTTP requests, on the server
    fs read streams
    Zlib streams *
    crypto streams *
    TCP sockets *
    child process stdout and stderr
    process.stdin

Writable Streams:
    HTTP requests, on the client
    HTTP responses, on the server
    fs write streams
    zlib streams *
    crypto streams *
    TCP sockets *
    child process stdin
    process stdout,stderr

* = both readable and writable

Reabable Stream: it is an abstraction for a source from which data can be consumed.
An example of this is the fs.createReadStream method

Writable Stream: it is an abstraction for a destination to which data an be written
An example of this is the fs.createWriteStream method

Duplex Stream: a stream that is both readable and writable. 
example of that is a TCP socket

Transform Stream: a duplex stream that can be used to modify
or transform the data while it being written and read.
example of this is the zlib.

All streams are instances of EventEmitter
we can pipe response from one stream into another stream similar to piping in Linux
______________________________________

HTTP status codes:

100 - 199: informational responses
200 - 299: successful responses
300 - 399: redirection messages
400 - 499; client error responses
500 - 599: server error responses

200: OK
201: created

400: bad request
401: unauthorised
403: forbidden
404: not found

500: internal server error
502: bad gateway
503: service unavailable
504: gateway timeout
______________________________________
child_processes: exec, execFile, spawn, fork

exec:
    exec('command',(err,stdout,stderr)=>{})

    err: defines the error that occurs while executing the command
    stderr: defines the error that occurs after executing the command

execFile: 
    similar to exec but instead of taking a command as input it takes a file that contains
    the commands as input and produces the output

    exec('file path',(err,stdout,stderr)=>{})

these both commands will spawn a new subshell and execute the command in that shell and buffer generated data
when the child process completes, the callback will be invoked with buffered data and errors if any
these both use buffers and they cannot process commands that generate large outputs

spawn: 
    it uses streams and can process commands that generate large outputs
    spawn takes in command as first input and the second input is an array that contains parameters to the command.
    since it uses streams we can handle on data, error, finish events
    spawn creates a new process and returns a streaming interface for IO

    const child = spawn('find',['/])
    child.on('data',()=>{})
    child.on('error',()=>{})
    child.on('exit',()=>{})

fork:
    a new child process will be created which will run on a seperate thread than the server
    and we can pass messages between the main thread and child thread using interprocess communication
    this is similar to worker threads

https://www.youtube.com/watch?v=bbmFvCbVDqo&ab_channel=MafiaCodes
https://www.youtube.com/watch?v=7cFNTD73N88&ab_channel=MafiaCodes
https://dzone.com/articles/understanding-execfile-spawn-exec-and-fork-in-node
______________________________________
Pub sub vs message queue:

    both are async way of communication between services

    Pub Sub:
        each message can be processed by multiple consumers
        message is removed upon expiry or all the consumers consume the message
        used in cases where we want to broadcast
        ordering of messages can be guaranteed in the order in which they are added

    message queue:
        each message is processed by only one consumer
        messge is removed when it is read by a consumer
        no message replay as message is deleted
        ordering of messages cannot be guaranteed

______________________________________
SQL vs NoSQL

small project + low scale + unknown access patterns: SQL
large project + high scale + relational queries: SQL with read and write replicas
medium/large project + high scale + high performance: NOSQL
______________________________________
HTTP headers:

    request headers:
        sent by client sending the request
        Host, User-agent -> info about who the client is
        Referer, Connection,
        Accept-Language, Accept-Encoding -> info about the language that the client understands
    
    response headers:
        sent by server to client to give more context about the response
        Connection: keep-alive
        Date : time stamp
        Server
        Content-Type
        ETag: used for versioning and cache
        Transfer-encoding
    
    Representation Headers:
        gives info about the data that has been transferred
        Content-Type
        Content-Encoding
        Conent-Length
        Content-Range
        Content-Location
______________________________________

stub: abstracts a function call and returns the final value of the function call 
mocks: they helps us to abstract a behaviour, for example if there is a function that changes its output based on the input
to test this we will have to create a mock implementation for this method
spy: they keep watching the function an keeps track of the number of times they are invoked and
the parameters that are passed
______________________________________
logging best practices:
    use log levels
    add descriptive messages
    avoid logging sensitive data
    use structured logging so that they cane be searched easily
______________________________________
microservices: building a large scale system, that consists of many loosely coupled services
    pros:
        polygot architecture: we can develop different pieces of the system in different technology, which ever we feel best
        based on the use case.
        easy to scale busy parts of the system without having to scale the entire system
        each part of the system can be developed independently
    cons:
        complicated to implement, network call, service discovery
        difficult to debug
        hard to find where the bug is without proper logging
______________________________________
SQL joins:
    inner join: only contains rows that contain matching rows in both tables
    outer join: matches on columns and contains data from both the tables
                the matched rows will have all the columns
                if there is no match, then the columns will be null
    left join: matches the tables on a column and returns the entire left table
                the unmatched rows will have null for the columns
    right join: matches the tables on a column and returns the entire right table
                the unmatched rows will have null for the columns
______________________________________
KEYS:
    primary key: a single column that could be used to uniquely identify a row
    id in a employee table can be used as primary key

    Candidate key: set of attributes that could be used to uniquely identify a row
    SSN, license_number, passport_number together can be used as candidate keys

    Foriegn key: points to a primary key in another table

    Composite key: whenever a primary key contains more than one attribute it is 
    called as s composite key
______________________________________

Relationships:
    one to one: one record in table A relates to one record in table B
    example: one person has only one SSN

    one to many: one record in table A can relate to multiple record in table B
    example: one person can have many phone numbers

    many to many: one record in table A can have many records in table B and
    one record in table B can have many records in table A
    example: a customer can purchase many items, a single item can be purchased by many customers
______________________________________

Normalisation:
    in most of the real world applications the best normalisation is achieved in the 3NF

    1NF:
        Each table cell should contain a single value.
        Each record needs to be unique.
        (introduces primary key, composite key)
    2NF:
        Be in 1NF
        Single Column Primary Key that does not functionally dependant on any subset of candidate key relation
        ( introduces forieng key and single column primary key)
    3NF:
        Be in 2NF
        Has no transitive functional dependencies

        A transitive functional dependency is when changing a non-key column,
        might cause any of the other non-key columns to change

        Example: changing the name of an employee results in changing the saluatation
        hence the salutation values should be moved to a seperate table and should use constants

https://www.guru99.com/database-normalization.html
______________________________________
promises:

    race: takes an array of promises as input and returns the first resolved or rejected promise as the output
    Promise.race is settled as soon as any of the promises you feed it settle, whether they are fulfilled or rejected.

    any : takes an array of promises as input and returns the first resolved promise as output.
    if all the promises fail then it rejects with an AggregateError
    Promise.any is settled as soon as any of the promises you feed it is fulfilled or they are all rejected, in which case it's rejected with an AggregateError.

    all :  takes in array of promises as input and returns an input of resolved values if all the promises are fulfilled
    even if one of them fails, then it returns a rejected promise.

    allSetteled: takes in an array of promises as input and returns an array of resolved or rejected responses of 
    all the promises

______________________________________

