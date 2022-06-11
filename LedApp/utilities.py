import board
import neopixel


def setColor(rgb,brightness):
    pixel_pin = board.D18
    ORDER = neopixel.RGB
    num_of_pixels = 24

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
