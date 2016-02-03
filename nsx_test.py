from creds import *
from nsxramlclient.client import NsxClient
import pprint
pp = pprint.PrettyPrinter(indent=1)

nsxraml_file = 'nsxraml/nsxvapiv614.raml'
client_session = NsxClient(nsxraml_file, nsx_manager, nsx_username, nsx_password)

vdn_scopes = client_session.read('vdnScopes', 'read')
pp.pprint(vdn_scopes['body'])

