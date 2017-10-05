from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather, Dial
import os

app = Flask(__name__)


@app.route("/forward", methods=['GET', 'POST'])
def forward():
	resp = VoiceResponse()
	dial = Dial(number=os.environ['PROXIED_NUM'], record="record-from-ringing-dual")
	resp.append(dial)
	return str(resp)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming requests."""
	resp = VoiceResponse()
	g = Gather(num_digits=1, action="/handle-key", method="POST")
	g.say("Thank you for calling the National")
	g.play("https://static.jcharante.com/yee/yee.mp3")
	g.say("Emergency Hotline.")
	g.say("""This call may be recorded for quality assurance purposes
			 To listen to a Standard Yee, Press 0.
			 To listen to A-ha - Take on Yee, Press 1.
			 To listen to Smash Mouth - All Yee, Press 2.
			 To Listen to Eiffel 65 - I'm Yee, Press 3.
			 To Listen to Yee Yee Yee Yee Yee, Press 4.
			 To Listen to Rick Astley - Never Gonna Give Yee Up, Press 5.
			 To Listen to Yee Mania, Press 6.
			 To Listen to Yee Busters, Press 7.
			 To Listen to The Original Yee, Press 8.
			 To Listen to Now Watch Me Yee, Press 9.
			 Press any other key to start over.""")
	resp.append(g)

	return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
	"""Handle key press from a user."""

	# Get the digit pressed by the user
	digit_pressed = request.values.get('Digits', None)
	if digit_pressed == "0":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/standard-yee.mp3")
		return str(resp)
	elif digit_pressed == "1":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/take-on-yee-full-version.mp3")
		return str(resp)
	elif digit_pressed == "2":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/smash-yee-yee-star.mp3")
		return str(resp)
	elif digit_pressed == "3":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/yeeffel-65-im-yee.mp3")
		return str(resp)
	elif digit_pressed == "4":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/yee-yee-yee-yee-yee.mp3")
		return str(resp)
	elif digit_pressed == "5":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/never-gonna-give-yee-up.mp3")
		return str(resp)
	elif digit_pressed == "6":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/yee-mania.mp3")
		return str(resp)
	elif digit_pressed == "7":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/yee-busters.mp3")
		return str(resp)
	elif digit_pressed == "8":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/yee-original.mp3")
		return str(resp)
	elif digit_pressed == "9":
		resp = VoiceResponse()
		resp.play("https://static.jcharante.com/yee/now-watch-me-yee.mp3")
		return str(resp)
	else:
		return redirect("/")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=5000)
