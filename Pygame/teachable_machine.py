# Python
# SF
# Raspberry Pi Teachable Machine Integration Script
import time
import logging
import argparse
import pygame
import os
import sys
import numpy as np
import subprocess

CONFIDENCE_THRESHOLD = 0.5   # at what confidence level do we say we detected a thing (Make higher if Pi is running low FPS)
PERSISTANCE_THRESHOLD = 0.25  # what percentage of the time we have to have seen a thing (Make lower if Pi is running low FPS)

os.environ['SDL_FBDEV'] = "/dev/fb1"
os.environ['SDL_VIDEODRIVER'] = "fbcon"

# App
from rpi_vision.agent.capture import PiCameraStream
from rpi_vision.models.teachablemachine import TeachableMachine

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

# initialize the display
pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

capture_manager = PiCameraStream(resolution=(screen.get_width(), screen.get_height()), rotation=180, preview=False)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--include-top', type=bool,
                        dest='include_top', default=True,
                        help='Include fully-connected layer at the top of the network.')

    parser.add_argument('savedmodel', help='TeachableMachine savedmodel')

    parser.add_argument('--tflite',
                        dest='tflite', action='store_true', default=False,
                        help='Convert base model to TFLite FlatBuffer, then load model into TFLite Python Interpreter')
    args = parser.parse_args()
    return args

last_seen = [None] * 10
last_spoken = None

def main(args):
    global last_spoken

    pygame.mouse.set_visible(False)
    screen.fill((0,0,0))
    try:
        splash = pygame.image.load(os.path.dirname(sys.argv[0])+'/bchatsplash.bmp')
        screen.blit(splash, ((screen.get_width() / 2) - (splash.get_width() / 2),
                    (screen.get_height() / 2) - (splash.get_height() / 2)))
    except pygame.error:
        pass
    pygame.display.update()

    # use the default font
    smallfont = pygame.font.Font(None, 24)
    medfont = pygame.font.Font(None, 36)
    bigfont = pygame.font.Font(None, 48)

    model = TeachableMachine(args.savedmodel)
    capture_manager.start()

    while not capture_manager.stopped:
        if capture_manager.frame is None:
            continue
        frame = capture_manager.read()
        # get the raw data frame & swap red & blue channels
        previewframe = np.ascontiguousarray(np.flip(np.array(capture_manager.frame), 2))
        # make it an image
        img = pygame.image.frombuffer(previewframe, capture_manager.camera.resolution, 'RGB')
        # draw it!
        screen.blit(img, (0, 0))

        timestamp = time.monotonic()
        if args.tflite:
            prediction = model.tflite_predict(frame)[0]
        else:
            prediction = model.predict(frame)[0]
        logging.info(prediction)
        delta = time.monotonic() - timestamp
        logging.info("%s inference took %d ms, %0.1f FPS" % ("TFLite" if args.tflite else "TF", delta * 1000, 1 / delta))
        print(last_seen)

        # add FPS on top corner of image
        fpstext = "%0.1f FPS" % (1/delta,)
        fpstext_surface = smallfont.render(fpstext, True, (255, 0, 0))
        fpstext_position = (screen.get_width()-10, 10) # near the top right corner
        screen.blit(fpstext_surface, fpstext_surface.get_rect(topright=fpstext_position))

        for p in prediction:
            label, name, conf = p
            if conf > CONFIDENCE_THRESHOLD:
                print("Detected", name)

                persistant_obj = False 
                last_seen.append(name)
                last_seen.pop(0)

                inferred_times = last_seen.count(name)
                if inferred_times / len(last_seen) > PERSISTANCE_THRESHOLD: 
                    persistant_obj = True

                detecttext = name.replace("_", " ")
                detecttextfont = None
                for f in (bigfont, medfont, smallfont):
                    detectsize = f.size(detecttext)
                    if detectsize[0] < screen.get_width():
                        detecttextfont = f
                        break
                else:
                    detecttextfont = smallfont 
                detecttext_color = (0, 255, 0) if persistant_obj else (255, 255, 255)
                detecttext_surface = detecttextfont.render(detecttext, True, detecttext_color)
                detecttext_position = (screen.get_width()//2,
                                       screen.get_height() - detecttextfont.size(detecttext)[1])
                screen.blit(detecttext_surface, detecttext_surface.get_rect(center=detecttext_position))

                if persistant_obj and last_spoken != detecttext:
                    os.system('echo %s | festival --tts & ' % detecttext)
                    last_spoken = detecttext
                break
        else:
            last_seen.append(None)
            last_seen.pop(0)
            if last_seen.count(None) == len(last_seen):
                last_spoken = None

        pygame.display.update()

if __name__ == "__main__":
    args = parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        capture_manager.stop()
