from PIL import Image
from gsbl.stick_bug import StickBug

sb = StickBug(Image.open('funni2.png'))
sb.video_resolution = (640, 640)
sb.lsd_scale = 0.5
sb.save_video('funni2.mp4')
