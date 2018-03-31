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
import java.util.logging.Level;
import java.util.logging.Logger;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

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
    
    public void imageClicked(MouseEvent event) {
        Object source = event.getSource();
        if (source == image1) {
            System.out.println("image one clicked");
        }
        if (source == image2) {
            System.out.println("image two clicked");
        }
        
        if (source == image3) {
            System.out.println("image three clicked");
        }
        
        if (source == image4) {
            System.out.println("image 4 clicked");
        }
        try {
            switchScene((Stage)(((Node)source).getScene().getWindow()));
        } catch (Exception e) {
            System.out.println("Something Happened");
        }
    }
    
    private void switchScene(Stage stage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("SongClicked.fxml"));
            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.show();
        } catch (IOException ex) {
            Logger.getLogger(FXMLDocumentController.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}
