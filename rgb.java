import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.awt.Color;

import javax.imageio.ImageIO;

public class rgb {
    private static final String IMAGE_NAME = "img/img_512.jpg";

    public static void main(String args[]){
        BufferedImage image = null;
        try {
            image = ImageIO.read(new File(IMAGE_NAME)); 
        } catch (IOException e) {
            System.out.println( e.getMessage() );
        }

        int w = image.getWidth(); 
        int h = image.getHeight(); 
    
        int[] dataBuffInt = image.getRGB(0, 0, w, h, null, 0, w); 
    
        Color c = new Color( dataBuffInt[100] ); 
    
        System.out.println(c.getRed()); // = (dataBuffInt[100] >> 16) & 0xFF 
        System.out.println(c.getGreen()); // = (dataBuffInt[100] >> 8) & 0xFF 
        System.out.println(c.getBlue()); // = (dataBuffInt[100] >> 0) & 0xFF 
        System.out.println(c.getAlpha()); // = (dataBuffInt[100] >> 24) & 0xFF 
    } 
}