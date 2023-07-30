# Facebook Marketplace Recommendation Ranking System
## Cleaning the dataset

- There are three datasets, `Images.csv`, `Products.csv`, and the `images` folder which includes all the images from Facebook Marketplace. 

- `clean_tabular_data.py` cleans the `Products.csv` to first remove all null values in the columns, and convert the prices to numeric data values by removing any dollar signs and commas. 

- `sandbox.ipynb` assign a label to each category in `Images.csv`. The root category is extracted from the `category` column in `Products.csv`, each category is then assigned an integer. The assigned labels are savaed as the column `labels` in `Images.csv`. The new dataset containing the labels is saved as `training_data.csv`. 

- `clean_images.py` resize the images in the `images` folder by resizing all the images to 512 and saving them in a new folder `resized_images`. To use: call the function `clean_image_data(path_to_directory_of_images)`. 