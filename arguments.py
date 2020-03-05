import sys
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument("--image", help="Insert image name here", type=str)

args = parser.parse_args()
args = vars(args)
image = cv2.imread(args["image"])

cv2.imshow("loaded iamge", image)

cv2.waitKey(0)

cv2.destroyAllWindows()