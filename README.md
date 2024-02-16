# LLAMA HUB

[Django](https://www.djangoproject.com/) App Server
Using Docker, Postgres, Pika with RabbitMQ for messaging

## High Level Architecture Diagram
![Llama Design](LlamaHerder.png)

## APIs

    GET: /actions -> Retrieve array of existing actions
    GET: /actions/<id> -> Retrieve action by id
    POST: /actions -> Create new action 
    PUT: /actions/<id> -> Update action by id
    DELETE: /action/<id> -> Delete action by id
    POST: /send/<id>  -> Send RabbitMQ action by id to Llama Herder for processing
    

## License

The MIT License (MIT)

Copyright &copy; 2024 Spero Autem LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

