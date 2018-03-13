/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package axelinterface1;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.image.ImageView;
import javafx.scene.image.Image;
import java.util.List;
import java.util.ArrayList;
import javafx.beans.property.DoubleProperty;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.RowConstraints;

/**
 *
 * @author varun
 */
public class FXMLDocumentController implements Initializable {
    private static final String imageUrl = "src/axelinterface1/images/";
    private static final String fileName = "src/axelinterface1/images.txt";
    
    @FXML
    private ImageView image1;
    @FXML
    private ImageView image2;
    @FXML
    private ImageView image3;
    @FXML
    private ImageView image4;
    @FXML
    private GridPane grid;
    
    private List<Image> images;
    private List<ImageView> views;
    private int index;
    
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        this.readFile();
        this.views = new ArrayList<>();
        views.add(image1);
        views.add(image2);
        views.add(image3);
        views.add(image4);
        initGrid();
        for (int x = 0; x < 4; x++) {
            views.get(x).setImage(images.get((index + x)% images.size()));
        }
    } 
    
    private void initGrid() {
        for (int x = 0; x < views.size(); x++) {
            views.get(x).fitHeightProperty().bind(grid.heightProperty().divide(2));
            views.get(x).fitWidthProperty().bind(grid.widthProperty().divide(2));
            views.get(x).setPreserveRatio(false);
        }
    }
    
    private void readFile() {
        this.images = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                images.add(new Image(new File(
                        imageUrl + line).toURI().toString()));
                
                System.out.println(images.get(0).getWidth());
            }
        } catch (IOException e) {
            System.out.println("error: reading file");
        }
        index = 0;
    }
}
