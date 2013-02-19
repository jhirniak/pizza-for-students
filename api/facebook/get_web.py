import pycurl

class ContentCallback:
        def __init__(self):
                self.contents = ''

        def content_callback(self, buf):
                self.contents = self.contents + buf

t = ContentCallback()
curlObj = pycurl.Curl()
curlObj.setopt(curlObj.URL, 'http://www.inf.ed.ac.uk/teaching/courses/inf2b/')
curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
curlObj.perform()
curlObj.close()
print t.contents
