#
def hello(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    #return ['Hello !!! world!\n']
    aaa = environ["QUERY_STRING"]
    bbb = aaa.split("&")
    ddd = []
    for c in bbb:
        c = c + "\n"
        ddd.append(c)
    return ddd
