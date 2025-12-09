# Color Palette Generator

Welcome to the **Color Palette Generator**! This is a simple Python-based project that extracts the **dominant colors** from an image and generates a **color palette**. It helps you visualize the main colors of any image and saves the results for further use.

## 📌 Features

* Load and resize images for faster processing
* Extract top 5 dominant colors using **K-Means clustering**
* Display the input image and its generated color palette
* Save:

  * Palette images (`output/palettes/`)
  * Input image copies (`output/images/`)
  * RGB values (`output/colors.json`)

## 🚀 Technologies Used

* **Python**: Core programming language
* **OpenCV**: Image processing and saving images
* **NumPy**: Array manipulation and calculations
* **Matplotlib**: Displaying images and palettes

## 📂 Project Structure

```
📁 Color-Palette-Generator/
├── 📄 main.py           # Main Python script
├── 📁 image/            # Folder for input images
├── 📁 output/
│    ├── images/         # Copies of input images
│    ├── palettes/       # Generated color palette images
│    └── colors.json     # JSON file storing RGB values
├── 📄 README.md         # Project documentation
```

## 🛠 Setup & Usage

1. Clone this repository:

   ```sh
   git clone https://github.com/logeshwarinaickar/Color-Palette-Generator.git
   ```
2. Install required libraries:

   ```sh
   pip install numpy opencv-python matplotlib
   ```
3. Put your input images in the `image/` folder.
4. Run the script:

   ```sh
   python main.py
   ```
5. The script will display the image and palette and save the output in the `output/` folder.

## 🛠 Functionalities

### 1. Load and Resize Image

* Automatically resizes large images for faster processing.

### 2. Extract Dominant Colors

* Uses K-Means clustering to find the top 5 colors.

### 3. Generate Palette

* Creates a visual palette of dominant colors.

### 4. Save Output

* Saves the palette image, input image copy, and RGB values in JSON format.

---

**Enjoy exploring colors! 🎨**

