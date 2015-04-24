from pyramid.response import Response
import xss


class RequestTranslator(object):

  def __init__(self):
    self.map_post = {}

  def create_response(self, request, game_name):

    resp = Response()
    x = xss.XssCleaner()

    i = 0
    js = 'gecoParams = { '
    for key in self.map_post:
      i +=1
      js += key+':"'+x.strip(self.map_post[key])
      if i != len(self.map_post):
        js += '", ' 
      else:
        js += '" '     

    js +='};'
    
    #load index.html as string
    path = 'games/'+game_name+'/index.html'
    file = open(path,'r')
    str = ""

    for line in file:
      str += line

    search_str = "<!--GECO_SCRIPT_START-->"
    replace_str = search_str + "\n<script>\n"+ js + "\n</script>"

    final_str = str.replace(search_str, replace_str)



    print final_str
    resp.text = final_str

    #return response
    return resp
