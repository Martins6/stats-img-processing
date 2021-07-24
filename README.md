# Statistical Analysis of Satellite Images

This repository contains specific code to statistically analyze satellite images. The jupyter notebooks are completely reproducible.

This analysis was used to build part of a report in a Multivariate Analysis 2 course in the Statistics bachellor degree in UFPE. I've also attached in this repository the report on "Formal_Report.pdf".

In addition, each notebook generated a PDF for a more comprehensive reading.

# Analysis

### Statistical Decomposition

The main objective was to break down the many channels of the satellite image into something easily understood. We want to reduce the dimensionality, but mantaining as much information as possible. For the K-channels that we have on the image, we wish to reduce to 1-dimension only. So we used to methods:

* PCA
* Factorial Analysis

The main conclusion was that those techniques could highlight some things, such as as light clusters in the middle of a desert! Which is really nice to bring out any kind of outliers in the image.

### Clustering

With clustering we wanted to see if we could statistically make regions or surfaces in the image. I also wanted to use the greysclae (1-d images) from Statistical Decomposition. So we used:

* K-Means

The main conclusion was that with 4 groups we could easily see, in a specific photo, the groups river, the light focus, the field and trees. The method was successful in clustering! Also the Factor Analysis provided great features to the model.

# Data

The data was taken from Landsat-8. It is an American Earth observation satellite that updates frequently their data! You can get new data using the AWS CLI. More information on:

* https://github.com/awslabs/open-data-docs/tree/main/docs/landsat-pds
* https://registry.opendata.aws/landsat-8/

As it is knonw, satellites "sees" with different channels than us. Our digital screens can interpret three channels: red, blue, green. However, satellites have multiple channels with different properties. For more information on the intepretation of each channel, checkout this [link](https://www.esri.com/arcgis-blog/products/product/imagery/band-combinations-for-landsat-8/?rmedium=redirect&rsource=blogs.esri.com/esri/arcgis/2013/07/24/band-combinations-for-landsat-8).

# Future Works

* I'm planning on using Fourier Analysis and Wavelet processing to see what other mysteries could be found!

* I shall try to find the optimal number of clusters using the elbow method.

* I'll try to find ways to implement in a distributed way the K-Medoid or Partition Around Medoids (PAM) algorithm, and the Hierarchical in order to analysis such Big Data (500 GB are needed for just this tiny image) and compare different types of clustering methods.

# References

Please check ref_analysis.md for specifc references to the methods used.

# Reproducing

Assuming that you already have python 3.8 on your machine, please then install pip through this [link](https://pip.pypa.io/en/stable/). Also, install the virtualenv module through this [link](https://virtualenv.pypa.io/en/latest/). Then run the following command in the repository:

```bash
python3 -m virtualenv venv/
source venv/bin/activate
pip install requirements.txt
```

After that you can easily run everything on the notebooks with the following command:

```bash
jupyter notebook
```

Then just acess the notebook that you wish!

To generate the PDF via the notebook you should first install TexLive (Latex) and then use:

```bash
jupyter nbconvert --to latex --no-input example.ipynb
pdflatex example.tex
```
