from werkzeug.security import generate_password_hash
from mito.utils import send_email
from mito import settings
from flask import render_template

def hash_pwd(password):
	return generate_password_hash(password)


def send_status_change_notification(user):
	if user.status == 'ACCEPTED':
		# txt = render_template('')
		subject = "Congratulations! You've been accepted to {}".format(settings.HACKATHON_NAME)
	elif user.status == 'REJECTED':
		# txt =
		subject = "Your {} application decision".format(settings.HACKATHON_NAME)
	elif user.status == 'WAITLISTED':
		# txt =
		subject = "Update on your application to {}".format(settings.HACKATHON_NAME)

	# send_email('hello@hacktx.com', subject, user.email, txt, html)