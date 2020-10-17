# instagram-seamless-swipe
A script to automate the process of generating slices of a landscape picture so you can post them as a seamless swipe... beccause I'm not good at Photoshop.

### How to Use

1. Download the script
- it only depends on base python3 packages
2. Run with args:
```
usage: split-pic.py [-h] -p PATH -k K

Split a landscape picture into k vertical slices.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path to the image we're splitting
  -k K, --k K           number of slices to do
```
*IMPORTANT NOTE:* it is imperative you know how you want to divide your pics up and at what aspect ratio. All this script does is slice up pictures. There are basically only 2 scenarios where this is useful:  
If you want seamless swipe on a landscape photo to POST, that would mean `k` 4x5 images (w x h) to take up as much screen on instagram as possible, so your original landscape photo needs to be 4`k`x5 (no pun intended). This is the most common use case.  
If you want to tap through a panorama on a STORY, that would mean `k` 9x16 images to take up as much screen as possible, so your original landscape photo needs to be 9`k`x16.  

Any questions feel free to file an issue. Enjoy!
