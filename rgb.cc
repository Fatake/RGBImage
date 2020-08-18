#include<opencv2\opencv.hpp>
#include<iostream>
#include <time.h>
#include<stdlib.h>
#define IMAGE_NAME = "img/img_512.jpg"

using namespace std;
using namespace cv;
//Prototipos
void imprimir(Mat m);
 
int main() {
    Mat imagen = imread(IMAGE_NAME, CV_LOAD_IMAGE_GRAYSCALE);
    imshow("Original", imagen);
    imprimir(imagen);
    waitKey(0);
    return 1;
}
 
void imprimir(Mat m) {
    int colores[256];
    for (int i = 0; i < 256; i++) {
        colores[i] = 0;
    }
    for (int j = 0; j < m.rows; j++) {
        for (int i = 0; i < m.cols; i++) {
            int pixel = m.at<uchar>(j, i);
            //cout << pixel << " ";
            colores[pixel]++;
        }
    }
    //Impresión de cantidad de colores
    cout << "Color=Cantidad" << endl;
    for (int i = 0; i < 256; i++) {
        if (colores[i] > 0){
            cout << i << " = " << colores[i] << endl;
        }
    }
}