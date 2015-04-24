from pyramid.response import Response
import xss

class RequestTranslator(object):

  def __init__(self):
    self.map_post = {}

  def create_response(self, request, game_name):

    resp = Response()
    x = xss.XssCleaner()

    js = 'gecoParams = { '
    js += ', '.join(['{}:"{}"'.format(key,x.strip(value)) for key, value in self.map_post.iteritems()])
    js +=' };'

    #load index.html as string
    path = 'games/'+game_name+'/index.html'

    with open(path, "r") as file:
      str = file.read()

    search_str = "<!--GECO_SCRIPT_START-->"
    replace_str = search_str + "\n<script>\n"+ js + "\n</script>"

    final_str = str.replace(search_str, replace_str)

    print final_str
    resp.body = final_str

    #return response
    return resp
