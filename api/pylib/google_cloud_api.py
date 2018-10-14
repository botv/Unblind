import io
import os
import sys

from google.cloud import vision
from google.cloud.vision import types
from loc_summary import locational_summary
from exec_summary import exec_summary


def localize_objects_uri(uri):
	"""Localize objects in the image on Google Cloud Storage

	Args:
	uri: The path to the file in Google Cloud Storage (gs://...)
	"""
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()

	image = vision.types.Image()
	image.source.image_uri = uri

	objects = client.object_localization(
		image=image).localized_object_annotations
	# print(len(objects))
	return locational_summary(objects)


def detect_labels_uri(uri):
	"""Detects labels in the file located in Google Cloud Storage or on the
	Web."""
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	image.source.image_uri = uri

	response = client.label_detection(image=image)
	labels = response.label_annotations
	# print(exec_summary(labels))
	return exec_summary(labels)

# uri = sys.argv[1]
# response = ""
# response = response+detect_labels_uri(uri)+" "
# response = response+localize_objects_uri(uri)
# print(response)
