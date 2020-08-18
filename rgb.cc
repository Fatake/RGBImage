#include <opencv2\opencv.hpp>
#include <iostream>
#include <stdlib.h>
#define IMAGE_NAME = "img/img_512.jpg"

using namespace std;
using namespace cv;

int main() {
    Mat imagen = imread(IMAGE_NAME, CV_LOAD_IMAGE_GRAYSCALE);
    imshow("Original", imagen);
    cout << "La imagen tiene " << imagen.rows << " pixeles de alto x "
        << imagen.cols << " pixeles de ancho" << endl;

    
    uchar pixel = imagen.at<uchar>(511,511);
    cout << "En la coordenada 511x511 el nivel de gris es " << (int)pixel << endl;
    waitKey(0);
    return 1;
}