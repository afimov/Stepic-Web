from cgi import parse_qs

def app(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	data = ''
	for key in d:
		data += "{}={}\n".format(key,d[key][0])
	status = '200 OK'
	response_headers = [
		('Content-type', 'text/plain')
	]
	start_response(status, response_headers)
	return [data]
