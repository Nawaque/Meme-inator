import cv2
import numpy as np


for a in range(2):
    print(a)
    for i in range(2):

        image = cv2.imread(f'./RESULTS/E_results{a}-{i}.jpg')
        imageG = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        mask = cv2.imread(f'./MASKS/E_results{a}-{i}.png', 0)

        kernel = np.ones((2,2), np.uint8)
        mask = cv2.dilate(mask, kernel)

        image = cv2.inpaint(image, mask, 2, cv2.INPAINT_NS)

        cv2.imwrite(f'./REMOVE/E_results{a}-{i}.jpg', image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()