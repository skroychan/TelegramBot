from config import BASE_URL
from api.entity import File

import http.client, mimetypes, urllib, uuid, logging


def send_response(method, data):
    try:
        if any(isinstance(x, File) and x.is_binary for x in data.values()):
            post_multipart(BASE_URL + method, data)
        else:
            urllib.request.urlopen(BASE_URL + method, urllib.parse.urlencode(data, True).encode('utf-8')).read()
        return True
    except Exception as e:
        logging.info('Data:\n' + str(data) + '\nException:\n' + repr(e))
        return False


def post_multipart(url, data):
    parts = urllib.parse.urlparse(url)
    host = parts[1]
    selector = parts[2]
    limit = '----------' + uuid.uuid4().hex
    clrf = '\r\n'
    l = []
    for (key, value) in list(data.items()):
        l.append('--' + limit)
        if isinstance(value, File):
            l.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, value.name))
            l.append('Content-Type: %s' % mimetypes.guess_type(value.name)[0] or 'application/octet-stream')
            l.append('')
            l.append(value.content)
        else:
            l.append('Content-Disposition: form-data; name="%s"' % key)
            l.append('')
            l.append(str(value))
    l.append('--' + limit + '--')
    l.append('')
    body = clrf.join(l)
    content_type = 'multipart/form-data; boundary=%s' % limit
    h = http.client.HTTPS(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()
