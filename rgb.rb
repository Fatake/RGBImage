# Gemfile
require "mini_magick"
gem 'mini_magick'


image = MiniMagick::Image.open("img/img_512.jpg")

image.colorspace "Blue"
image.colorspace "Red"
image.colorspace "Green"

image.width 
image.height