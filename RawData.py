import PyCapture2
from sys import exit
from time import sleep
import cv2
import numpy
from PIL import Image



def pollForTriggerReady(cam):
	softwareTrigger = 0x62C
	while True:
		regVal = cam.readRegister(softwareTrigger)
		if not regVal:
			break

def fireSoftwareTrigger(cam):
	softwareTrigger = 0x62C
	fireVal = 0x80000000
	cam.writeRegister(softwareTrigger, fireVal)


# Ensure sufficient cameras are found
bus = PyCapture2.BusManager()
numCams = bus.getNumOfCameras()
print("Number of cameras detected: ", numCams)
if not numCams:
	print("Insufficient number of cameras. Exiting...")
	exit()


c = PyCapture2.Camera()
c.connect(bus.getCameraFromIndex(0))


# Power on the Camera
cameraPower = 0x610
powerVal = 0x80000000

c.writeRegister(cameraPower, powerVal)


# Configure trigger mode
triggerMode = c.getTriggerMode()
triggerMode.onOff = True
triggerMode.mode = 0
triggerMode.parameter = 0
triggerMode.source = 7		# Using software trigger

c.setTriggerMode(triggerMode)

# Configure camera format7 settings
fmt7imgSet = PyCapture2.Format7ImageSettings(0, 0, 0, 1920, 1080, PyCapture2.PIXEL_FORMAT.RAW8)
fmt7pktInf, isValid = c.validateFormat7Settings(fmt7imgSet)
if not isValid:
	print("Format7 settings are not valid!")
	exit()

c.setFormat7ConfigurationPacket(fmt7pktInf.recommendedBytesPerPacket, fmt7imgSet)

pollForTriggerReady(c)

c.setConfiguration(grabTimeout = 5000)

# Start acquisition

c.startCapture()

# Grab images

numRange = 1

for i in range(numRange):
    pollForTriggerReady(c)
    fireSoftwareTrigger(c)

    try:
        image = c.retrieveBuffer()
        #RGGB
        name = 'pic'+str(i)+'.png'

        pixelArr = image.getData()
        temp = numpy.zeros((1080,1920,3),dtype=numpy.uint8)

        count = 0
        for i in range(len(pixelArr)):
            x = int(i / 1920)
            y = i % 1920

            #RG
            if(x%2 == 0):
                if(y%2 == 0):
                    temp[x][y][0] = pixelArr[i]
                else:
                    temp[x][y][1] = pixelArr[i]
            #GB
            else:
                if (y%2 == 0):
                    temp[x][y][1] = pixelArr[i]
                else:
                    temp[x][y][2] = pixelArr[i]

        # Save the image
        Image.fromarray(temp, "RGB").save(name)

        print ('.')

    except PyCapture2.Fc2error as fc2Err:
        print("Error retrieving buffer : ", fc2Err)
        continue

c.setTriggerMode(onOff = False)
print("Finished grabbing images!")

c.stopCapture()
c.disconnect()
input("Done! Press Enter to exit...\n")
