from pyramid.response import Responsefrom pyramid.view import view_configfrom requestTranslator import RequestTranslator@view_config(route_name='spacebar')@view_config(route_name='nyx')def request_translator_view(request):       post_dic = request.POST    game_name = request.matchdict['game_name']        responder = RequestTranslator()     responder.map_post["userID"] =  post_dic['PlayerID']    responder.map_post["token"] =  post_dic['SessionID']    responder.map_post["currency"] =  post_dic['CurrencyCode']    responder.map_post["country"] =  post_dic['CountryCode']    responder.map_post["language"] =  post_dic['LanguageCode']    responder.map_post["gameName"] =  post_dic['GameID']            return responder.create_response(request, game_name)@view_config(route_name='openbet')def openbet_request_translator_view(request):    return Response()