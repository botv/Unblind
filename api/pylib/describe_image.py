import sys
from google_cloud_api import localize_objects_uri
from google_cloud_api import detect_labels_uri

uri = sys.argv[1]
response = ""
response = response + detect_labels_uri(uri) + " "
response = response + localize_objects_uri(uri)
print(response)
