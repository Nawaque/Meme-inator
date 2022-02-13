import cv2
import numpy as np

def resolve(image, mask):

    kernel = np.ones((4,4), np.uint8)
    mask = cv2.dilate(mask, kernel)

    image = cv2.inpaint(image, mask, 2, cv2.INPAINT_NS)

    return image

for a in range(2):
    print(a)
    for i in range(2):

        image = cv2.imread(f'./RESULTS/E_results{a}-{i}.jpg')

        mask = cv2.imread(f'./MASKS/E_results{a}-{i}.png', 0)

        cv2.imwrite(f'./REMOVE/E_results{a}-{i}.jpg', resolve(image, mask))

        cv2.waitKey(0)
        cv2.destroyAllWindows()