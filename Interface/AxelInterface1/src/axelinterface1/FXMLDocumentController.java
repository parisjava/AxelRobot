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
import javafx.animation.FadeTransition;
import javafx.event.Event;
import javafx.scene.input.SwipeEvent;
import javafx.scene.input.TouchEvent;
import javafx.scene.layout.GridPane;
import javafx.util.Duration;

/**
 *
 * @author varun
 */
public class FXMLDocumentController implements Initializable {
    private static final String imageUrl = "src/axelinterface1/images/";
    private static final String fileName = "src/axelinterface1/images.txt";
    private static final int DURATION = 1000;
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
    private List<FadeTransition> transitions;
    private int index;
    
    
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        this.readFile();
        this.views = new ArrayList<>();
        this.transitions = new ArrayList<>();
        views.add(image1);
        views.add(image2);
        views.add(image3);
        views.add(image4);
        initGrid();
        for (int x = 0; x < views.size(); x++) {
            views.get(x).setImage(images.get((index + x)% images.size()));
            transitions.add(new FadeTransition(Duration.millis(DURATION), views.get(x)));
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
    
    
    public void imageTouched(Event event) {
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
            SwitchScene.switchScene("SongClicked.fxml", SwitchScene.convertEvent(event));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    
    public void swiped(Event event) {
        System.out.println("SWIPE EVENT");
        index += 4;
        for (int x = 0; x < views.size(); x++) {
            transitions.get(x).playFromStart();
            views.get(x).setImage(images.get((x + index) % images.size()));
        }
        
        
    }
    

}
