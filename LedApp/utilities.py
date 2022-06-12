import board
import neopixel
import time
import math

pixel_pin = board.D18
ORDER = neopixel.GRB
num_of_pixels = 24

def setColor(rgb,brightness):


    pixels = neopixel.NeoPixel(
        pixel_pin,num_of_pixels, brightness = float(brightness), auto_write = False, pixel_order = ORDER
    )

    r, g, b = rgb

    try:
        pixels.fill((r,g,b))
        pixels.show()

        return True
    except:
        return False

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait, brightness):
    pixels = neopixel.NeoPixel(
        pixel_pin,num_of_pixels, brightness = float(brightness), auto_write = False, pixel_order = ORDER
    )
    for j in range(255):
        for i in range(num_of_pixels):
            pixel_index = (i * 256 // num_of_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def trainstion(brightness,t):
    max=255
    step = 255//t
    pixels = neopixel.NeoPixel(
        pixel_pin,num_of_pixels, brightness = float(brightness), auto_write = False, pixel_order = ORDER
    )
    for i in range(0,t):
        blue = 255 * (0.5 * (1 + math.sin((t*math.pi)-(math.pi/2))))
        green = 0
        red = 255 - blue
        RGBtriplet = (int(red), int(green), int(blue))
        pixels.fill(RGBtriplet)
        pixels.show()
        time.sleep(0.5)
        
    return True