#* framework.py                            
#*                                                 
#*  ANLY 555 Spring 2023                     
#*  Project Monroe 
#*                                                 
#*  Due on: 2/22/2023                 
#*  Author(s): Monroe Farris                           
#*  
#* 
#*  In accordance with the class policies and Georgetown's 
#*  Honor Code, I certify that, with the exception of the  
#*  class resources and those items noted below, I have neither 
#*  given nor received any assistance on this project other than  
#*  the TAs, professor, textbook and teammates.  
#* 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import csv
import nltk
nltk.download('stopwords')
nltk.download('wordnet')

class DataSet:
    """
    Class that defines the characteristics of a data set to later 
    be used for analysis. 
    """

    def __init__(self, filename):
        """
        filename: name of data file to be processed 
        """

        self.filename = filename
        self.data = []

    def __readFromCSV(self, filename):
        """
        Function to read in data from a CSV file 

        filename: name of data file to be processed 
        """

        try:
            with open(filename) as file:
                read = csv.DictReader(file)
                for row in read:
                    self.data.append(row)

        except Exception as e:
            print(f"An error occurred while reading in the data: {e}")
            raise


    def __load(self, filename):
        """
        Function to load data for analysis 

        filename: name of data file to be processed 
        """

        self.filename = input("Enter the filename to load: ")

        try:
            self.__readFromCSV(self.filename)
        except Exception as e:
            print(f"An error occurred while loading the data: {e}")
            raise

    def clean(self):
        """
        Function for cleaning the data.
        """
        pass
    

    def explore(self):
        """
        Function for exploring the data.
        """
        pass

class TimeSeriesDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    time series data 
    """

    def clean(self, filter_size=3):
        # run a median filter with optional parameters which determine the filter size
        self.data = self.data.rolling(window=filter_size, min_periods=1).median()

class TextDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    text data 
    """

    def clean(self):
    # remove stop words (and feel free to stem and / or lemmatize)
        stop_words = set(nltk.corpus.stopwords.words('english'))
        stemmer = nltk.stem.PorterStemmer()
        lemmatizer = nltk.stem.WordNetLemmatizer()

        for row in self.data:
            text = row['text']
            words = text.lower().split()

            words = [word for word in words if not word in stop_words]
            stemmed = [stemmer.stem(word) for word in words]
            lemm = [lemmatizer.lemmatize(word) for word in words]

            row['text'] = ' '.join(words)
            row['text_stemmed'] = ' '.join(stemmed)
            row['text_lemmatized'] = ' '.join(lemm)


    def explore(self):
        # Create a text string from the dictionary values
        text = ""
        for row in self.data:
            text += row['text'] + " "

        # Create the wordcloud
        wordcloud = WordCloud(background_color='white').generate(text)

        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

class QuantDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    quantitative data 
    """

    def clean(self):
        filled_data = []
        for row in self.data:
            filled_row = {}
            for key, value in row.items():
                if value is None:
                    # Calculate the mean of non-missing values for the key
                    mean = np.mean([v for k, v in row.items() if k != key and v is not None])
                    filled_row[key] = mean
                else:
                    filled_row[key] = value
            filled_data.append(filled_row)

        self.data = filled_data


class QualDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    qualitative data 
    """


    def clean(self):
        filled_data = []
        for row in self.data:
            filled_row = {}
            for key, value in row.items():
                if value == '':
                    # Calculate the mean of non-missing values for the key
                    mode = np.mode([v for k, v in row.items() if k != key and v is not None])
                    filled_row[key] = mode
                else:
                    filled_row[key] = value
            filled_data.append(filled_row)

        self.data = filled_data

        print(self.data[:10])

class ClassifierAlgorithm:
    """
    Class that defines the characteristics of a 
    classifier algorithm to perform analysis on 
    the data 
    """

    def __init__(self):
        pass

    def train(self):
        """
        Function for training data.
        """

        print("training algorithm")

    def test(self):
        """
        Function for testing data 
        """

        print("testing algorithm")

class simpleKNNClassifier(ClassifierAlgorithm):
    """
    Class inherited from the ClassifierAlgorithm class that 
    will be used to define the characteristics of 
    a simple KNN Classifier 
    """

    pass

class kdTreeKNNClassifier(ClassifierAlgorithm):
    """
    Class inherited from the ClassifierAlgorithm class that 
    will be used to define the characteristics of 
    a simple KD Tree KNN Classifier 
    """

    pass


class Experiment:
    """
    Class that defines the characteristics of an 
    experimentation approach to perform analysis on 
    the data 
    """

    def runCrossVal(self, k):
        """
        Function to perform cross validation 

        k: number of groups the data will be split into
        """

        print("cross validation with k = " + str(k))

    def score(self):
        """
        Function that calculates a score for the data 
        based on evaluation metrics 
        """

        print("score function")

    def __confusionMatrix(self):
        """
        Function that generates a confusion matrix 
        for the analysis 
        """

        print("confusion matrix function")

