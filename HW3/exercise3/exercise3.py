import cv2
import numpy as np
import sys

def Gaussian_Noise(pic, mean, sigma):
    
    noisy_Pic=pic.copy()
    cv2.randn(noisy_Pic,mean,sigma)
    cv2.add(pic, noisy_Pic, noisy_Pic)
    
    return noisy_Pic

def salt_pepper_Noise(pic, pa, pb):
    a1 = int(pic.shape[0] * pic.shape[1] * pa)
    a2 = int(pic.shape[0] * pic.shape[1] * pb)
    
    picCopy=pic.copy()
    
    for i in range(a1):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=0
        
    for i in range(a2):
        picCopy[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=255
        
    return picCopy

def main():
    mean =[0, 5, 10, 20]
    sigma = [ 0, 20, 50, 100]
    pa = [0.01, 0.03, 0.05, 0.4] 
    pb = [0.01, 0.03, 0.05, 0.4]
    kernel = [3]
    

    pic = cv2.imread('Lenna.png',0)
    cv2.imshow("Lenna",pic)
    
    for i in range(len(kernel)):
        for m in range (len(mean)):
            for s in range (len(sigma)):
                gaussImage = Gaussian_Noise(pic,mean[m],sigma[s])
                cv2.imshow("GaussianNoise",gaussImage)
                boxFilterImage = cv2.boxFilter(gaussImage, -1, (kernel[i], kernel[i]))
                cv2.imshow("GaussianBoxfilter",boxFilterImage)
                gaussBlurImage=cv2.GaussianBlur(gaussImage, (kernel[i], kernel[i]), 1.5)
                cv2.imshow("GaussianGaussfilter",gaussBlurImage)
                medianFilterImage=cv2.medianBlur(gaussImage,5)
                cv2.imshow("GaussianMedianfilter",medianFilterImage)
                if (m == 0):
                    if (s == 0):
                        cv2.imwrite('boxFilter.png',boxFilterImage)
                        cv2.imwrite('GaussBlur.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter.png',medianFilterImage)
                    elif (s == 1):
                        cv2.imwrite('boxFilter20sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur20sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter20sigma.png',medianFilterImage)
                    elif (s == 2):
                        cv2.imwrite('boxFilter50sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur50sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter50sigma.png',medianFilterImage)
                    elif (s == 3):
                        cv2.imwrite('boxFilter100sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur100sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter100sigma.png',medianFilterImage)
                elif (m == 1):
                    if (s == 0):
                        cv2.imwrite('boxFilter5.png',boxFilterImage)
                        cv2.imwrite('GaussBlur5.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter5.png',medianFilterImage)
                    elif (s == 1):
                        cv2.imwrite('boxFilter5_20sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur5_20sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter5_20sigma.png',medianFilterImage)
                    elif (s == 2):
                        cv2.imwrite('boxFilter5_50sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur5_50sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter5_50sigma.png',medianFilterImage)
                    elif (s == 3):
                        cv2.imwrite('boxFilter5_100sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur5_100sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter5_100sigma.png',medianFilterImage)
                elif (m == 2):
                    if (s == 0):
                        cv2.imwrite('boxFilter10.png',boxFilterImage)
                        cv2.imwrite('GaussBlur10.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter10.png',medianFilterImage)
                    elif (s == 1):
                        cv2.imwrite('boxFilter10_20sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur10_20sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter10_20sigma.png',medianFilterImage)
                    elif (s == 2):
                        cv2.imwrite('boxFilter10_50sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur10_50sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter10_50sigma.png',medianFilterImage)
                    elif (s == 3):
                        cv2.imwrite('boxFilter10_100sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur10_100sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter10_100sigma.png',medianFilterImage)
                if (m == 3):
                    if (s == 0):
                        cv2.imwrite('boxFilter20sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur20sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter20sigma.png',medianFilterImage)
                    elif (s == 1):
                        cv2.imwrite('boxFilter20_20sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur20_20sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter20_20sigma.png',medianFilterImage)
                    elif (s == 2):
                        cv2.imwrite('boxFilter20_50sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur20_50sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter20_50sigma.png',medianFilterImage)
                    elif (s == 3):
                        cv2.imwrite('boxFilter20_100sigma.png',boxFilterImage)
                        cv2.imwrite('GaussBlur20_100sigma.png',gaussBlurImage)
                        cv2.imwrite('Medianfilter20_100sigma.png',medianFilterImage)
        
        
        
        for a in range (len(pa)):
            for b in range (len(pb)):
                pepperSaltImg=salt_pepper_Noise(pic,pa[a],pb[b])
                cv2.imshow("peppersaltnoise",pepperSaltImg)
                boxFilterImage = cv2.boxFilter(pepperSaltImg, -1, (kernel[i], kernel[i]))
                cv2.imshow("peppersaltBoxfilter",boxFilterImage)
                gaussBlurImage=cv2.GaussianBlur(pepperSaltImg, (kernel[i], kernel[i]), 1.5)
                cv2.imshow("peppersaltGaussfilter",gaussBlurImage)
                medianFilterImage=cv2.medianBlur(pepperSaltImg,5)
                cv2.imshow("peppersaltMedianfilter",medianFilterImage)
                
                if (a==0):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter01_0.01.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur01_0.01.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter01_0.01.png',medianFilterImage)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter01_0.03.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur01_0.03.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter01_0.03.png',medianFilterImage)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter01_0.05.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur01_0.05.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter01_0.05.png',medianFilterImage)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter01_0.4.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur01_0.4.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter01_0.4.png',medianFilterImage)
                if (a==1):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter03_0.01.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur03_0.01.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter03_0.01.png',medianFilterImage)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter03_0.03.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur03_0.03.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter03_0.03.png',medianFilterImage)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter03_0.05.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur03_0.05.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter03_0.05.png',medianFilterImage)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter03_0.4.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur03_0.4.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter03_0.4.png',medianFilterImage)
                if (a==2):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter05_0.01.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur05_0.01.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter05_0.01.png',medianFilterImage)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter05_0.03.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur05_0.03.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter05_0.03.png',medianFilterImage)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter05_0.05.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur05_0.05.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter05_0.05.png',medianFilterImage)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter05_0.4.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur05_0.4.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter05_0.4.png',medianFilterImage)
                if (a==3):
                    if (b == 0):
                        cv2.imwrite('SaltboxFilter4_0.01.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur4_0.01.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter4_0.01.png',medianFilterImage)
                    elif (b ==1):
                        cv2.imwrite('SaltboxFilter4_0.03.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur4_0.03.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter4_0.03.png',medianFilterImage)
                    elif (b == 2):
                        cv2.imwrite('SaltboxFilter4_0.05.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur4_0.05.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter4_0.05.png',medianFilterImage)
                    elif (b == 3):
                        cv2.imwrite('SaltboxFilter4_0.4.png',boxFilterImage)
                        cv2.imwrite('SaltGaussBlur4_0.4.png',gaussBlurImage)
                        cv2.imwrite('SaltMedianfilter4_0.4.png',medianFilterImage)
    cv2.waitkerneley(0)
    
if __name__ == "__main__":
    main()