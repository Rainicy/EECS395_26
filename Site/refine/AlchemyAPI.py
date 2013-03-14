import json
import urllib
import urllib2

# should be made a class and class variables
# oh well

base_api_url = 'http://access.alchemyapi.com/calls/'
api_key_file = 'alchemyapikey.dat'

def loadApiKey(fname=api_key_file):
  f = open(fname, 'r')
  base_params["apikey"] = f.read()
  f.close()


base_params = {
  "apikey": None,
  "outputMode": "json",
  "linkedData": 0
}



def MakeApiCall(typ, function, payload, params=base_params):
  if params["apikey"] == None:
    raise ValueError('apikey must be set / loaded before calling the api')
  url = base_api_url + typ + '/' + function + '?' + typ + "=" + urllib.quote_plus(payload)
  for k in params.keys():
    url = url + "&" + k + "=" + urllib.quote_plus(params[k])
  try:
    socket = urllib2.urlopen(url)
    raw_json = socket.read()
    socket.close()
  except (urllib2.HTTPError):
    raw_json = '{"status": "No connection"}'
  return json.loads(raw_json)


def URLGetRankedNamedEntities(url):
  return MakeApiCall("url", "URLGetRankedNamedEntities", url)

def TextGetRankedNamedEntities(txt):
  return MakeApiCall("text", "TextGetRankedNamedEntities", txt)
