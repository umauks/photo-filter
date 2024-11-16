from PIL import Image
from typing import Tuple

class Filter:
    '''Общий класс для создания цветных фильтров.'''
    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        raise NotImplementedError()
    def ap_image(self, img: Image.Image) -> Image.Image:
        for i in range(img.width):
            for j in range(img.height):
                pixel = img.getpixel((i, j))
                new_pixel = self.ap_pixel(pixel)
                img.putpixel((i, j), new_pixel)
        return img

class Red(Filter):
    '''Фильтр, который делает изображение красным.'''
    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        r = min(255, int(r * 5))
        return r, g, b


class Green(Filter):
    '''Фильтр, который делает изображение зеленым.'''

    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        g = min(255, int(g * 5))
        return r, g, b

class Blue(Filter):
    '''Фильтр, который делает изображение синим.'''
    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        b = min(255, int(b * 5))
        return r, g, b

class Dark(Filter):
    '''Фильтр, который делает изображение темнее.'''

    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        r = max(0, int(r - 120))
        g = max(0, int(g - 120))
        b = max(0, int(b - 120))
        return r, g, b

class Bright(Filter):
    '''Фильтр, который делает изображение ярче.'''
    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        r = min(255, int(r + 120))
        g = min(255, int(g + 120))
        b = min(255, int(b + 120))
        return r, g, b
class Inverse(Filter):
    '''Фильтр, который инвертирует изображение.'''
    def ap_pixel(self, pixel: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r, g, b = pixel
        r_new = 255 - r
        g_new = 255 - g
        b_new = 255 - b
        return r_new, g_new, b_new

