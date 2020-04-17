import picamera

camera = picamera.PiCamera()
for filename in camera.record_sequence('%d.h264' % i for i in range(1, 11)):
	camera.wait_recording(2)

