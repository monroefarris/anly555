#* framework.py                            
#*                                                 
#*  ANLY 555 Spring 2023                     
#*  Project Monroe 
#*                                                 
#*  Due on: 2/24/2023                 
#*  Author(s): Monroe Farris                           
#*  
#* 
#*  In accordance with the class policies and Georgetown's 
#*  Honor Code, I certify that, with the exception of the  
#*  class resources and those items noted below, I have neither 
#*  given nor received any assistance on this project other than  
#*  the TAs, professor, textbook and teammates.  
#* 

# loading in approved libraries for processing 
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

        data: data to be used later on in analysis
        """

        self.filename = filename
        self.data = []

    def __readFromCSV(self, filename):
        """
        Function to read in data from a CSV file 
        - returns a list of dictionaries containing row-wise file information

        filename: name of data file to be processed 
        """

        try:
            with open(filename) as file:        # open the file 
                read = csv.DictReader(file)     # read the CSV file as a dictionary
                for row in read:                # loop over all rows in the file
                    self.data.append(row)       # append the dictionary for each row to the data list

        # if there is an error in reading the file, raise an exception
        except Exception as e:
            print(f"An error occurred while reading in the data: {e}")
            raise


    def __load(self, filename):
        """
        Function to load data for analysis 
        - asks user for file to load 
        - loads data using the __readFromCSV method 

        filename: name of data file to be processed 
        """

        try:
            self.filename = input("Enter the filename to load: ")    # ask for user input for which file to load
            self.__readFromCSV(self.filename)                        # read in the file using the __readFromCSV method 

        # if there is an error in loading the file, raise an exception 
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

    def clean(self, filter_size = 3):
        """
        Function that cleans time series data 
        - runs a median filter 

        filter_size: optional parameter to determine filter size 
        """

        try:
            for key in self.data[0].keys():
                if isinstance(self.data[0][key], (int, float)):
                    values = [d[key] for d in self.data]
                    filtered_values = []

                    # Apply median filter with given filter size
                    for i in range(len(values)):
                        if i < filter_size // 2:
                            filtered_value = values[i]
                        elif i >= len(values) - filter_size // 2:
                            filtered_value = values[i]
                        else:
                            filtered_value = sorted(values[i - filter_size // 2:i + filter_size // 2 + 1])[filter_size // 2]
                        filtered_values.append(filtered_value)

                    # Replace the original values with the filtered values in each dictionary
                    for i in range(len(self.data)):
                        self.data[i][key] = filtered_values[i]

        # raise an error if there is an issue with data cleaning 
        except Exception as e:
            print(f"An error occurred while cleaning the data: {e}")
            raise

class TextDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    text data 
    """

    def clean(self):
        """
        Function that cleans text data 
        - removal of stop words 
        - stemming of words 
        - lemmatization of words 
        """

        try:
            stop_words = set(nltk.corpus.stopwords.words('english'))        # establishing stop word corpus
            stemmer = nltk.stem.PorterStemmer()                             # initializing nltk stemmer 
            lemmatizer = nltk.stem.WordNetLemmatizer()                      # initializing nltk lemmatizer 

            for row in self.data:
                text = row['text']
                words = text.lower().split()                                # lower-casing and splitting all words

                words = [word for word in words if not word in stop_words]  # sub-setting to only include words not in the stop word list
                stemmed = [stemmer.stem(word) for word in words]            # stemming words
                lemm = [lemmatizer.lemmatize(word) for word in words]       # lemmatizing words

                row['text'] = ' '.join(words)                               # replacing text column with "cleaned" text
                row['text_stemmed'] = ' '.join(stemmed)                     # new column for stemmed text
                row['text_lemmatized'] = ' '.join(lemm)                     # new column for lemmatized text 
       
       # raise an error if there is an issue with data cleaning 
        except Exception as e:
            print(f"An error occurred while cleaning the data: {e}")
            raise
            

    def explore(self):
        """
        Function that visualizes text data 
        - three wordcloud visualizations 
            - words 
            - stemmed words 
            - lemmatized words 
        """

        try:
            # initializing strings for later use 
            text = ""
            text_stemmed = ""
            text_lemm = ""
            for row in self.data:                           # looping through each row of data 
                text += row['text'] + " "                   # appending words to the string
                text_stemmed += row['text_stemmed'] + " "   # appending stemmed words to the string
                text_lemm += row['text_lemmatized'] + " "   # appending lemmatized words to the string

            # creating wordclouds for the three visualizations
            wordcloud = WordCloud(background_color='white').generate(text)
            wordcloud_stemmed = WordCloud(background_color='white').generate(text_stemmed)
            wordcloud_lemm = WordCloud(background_color='white').generate(text_lemm)

            # looping through each wordcloud to plot 
            for i in [wordcloud, wordcloud_stemmed, wordcloud_lemm]:
                counter = 1                                                     # initializing a counter for naming conventions
                plt.imshow(i, interpolation='bilinear')                         # plotting the wordcloud
                plt.axis("off")         
                plt.savefig('./images/text/wordcloud_' + str(counter) + '.png')      # saving the figure 
                plt.close()

                counter += 1    # incrementing the counter 

        # raise an error if there is an issue with data visualization 
        except Exception as e:
            print(f"An error occurred while visualizing the data: {e}")
            raise

class QuantDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    quantitative data 
    """

    def clean(self):
        """
        Function that cleans quantitative data 
        - replaces empty values with the mean 
        """

        try:
            freq_dict = {}                   
            sum_dict = {}
            count_dict = {}
            for d in self.data:                                 # looping through all of the rows of data
                for key, val in d.items():                      # separating columns and values by row
                    if val != '':                               # searching for instances of missing values 
                        if val.isdigit():                       # determining if numeric value
                            val = int(val)                      # if true, get the integer representation of the string value
                            sum_dict.setdefault(key, 0)         # update sum_dict with the sum of all numeric values for the current key
                            sum_dict[key] += val
                            count_dict.setdefault(key, 0)       # update count_dict with the count of all numeric values for the current key
                            count_dict[key] += 1

                        else:
                            # update freq_dict with the count of each unique non-numeric value for the current key
                            freq_dict.setdefault(key, {}).update({val: freq_dict.get(key, {}).get(val, 0) + 1})

            for d in self.data:                                             # loop through all rows of data 
                for key, val in d.items():                                  # loop through all columns and their values
                    if val == '':                                           # looking for empty values
                        if key in freq_dict:                                # if the empty value is categorical - proceed
                            max_count = max(freq_dict[key].values())        # get the max value
                            mode_value = [k for k, v in freq_dict[key].items() if v == max_count][0]    # get the mode value 
                            d[key] = mode_value                             # replace value with mode 
                        elif key in sum_dict and key in count_dict:         # if the empty value is numeric 
                            mean_value = sum_dict[key] / count_dict[key]    # calculate mean value
                            d[key] = str(mean_value)                        # replace with mean value

        # raise an error if there is an issue with data cleaning 
        except Exception as e:
            print(f"An error occurred while cleaning the data: {e}")
            raise

    def explore(self):
        """
        Function that visualizes quantitative data 
        - two visualizations 
            - scatter plot of project code and w2 value
            - bar plot of project code and w3 value
        """

        try:
            data_small = self.data[:50]                         # sub-setting the data for viz purposes 

            for d in data_small:                                # looping through the sub-setted data 
                d["w2"] = int(d["W2"])                          # converting strings to ints 
                d["w3"] = int(d["W3"])

            products = [d["Product_Code"] for d in data_small]  # creating variable representations of the data for reference 
            w2 = [d["w2"] for d in data_small]
            w3 = [d["w3"] for d in data_small]

            # plot 1 - scatter plot of product code and w2 value 
            plt.scatter(products, w2)
            plt.xlabel("Product Code")
            plt.ylabel("W2 Value")
            plt.title("Product Codes vs W2 Value")
            plt.xticks(rotation = 90)
            plt.savefig('./images/quantitative/scatter_quant.png') 
            plt.close()

            # plot 2 - bar plot of product code and w3 value 
            plt.bar(products, w3)
            plt.xlabel("Product Code")
            plt.ylabel("W3 Value")
            plt.title("Product Codes vs W3 Value")
            plt.xticks(rotation = 90)
            plt.savefig('./images/quantitative/bar_quant.png')
            plt.close()

        # raise an error if there is an issue with data visualizing 
        except Exception as e:
            print(f"An error occurred while visualizing the data: {e}")
            raise


class QualDataSet(DataSet):
    """
    Class inherited from the DataSet class that 
    will be used to define the characteristics of 
    qualitative data 
    """

    def clean(self):
        """
        Function that cleans qualitative data 
        - replaces empty values with the mode 
        """

        try:    
            freq_dict = {}                          
            for d in self.data:                 # loop through all rows of data 
                for key, val in d.items():      # loop through all columns and their values
                    if val != '':               # if value is not empty 
                        freq_dict.setdefault(key, {}).update({val: freq_dict.get(key, {}).get(val, 0) + 1}) # log in freq_dict for later use

            for d in self.data:                 # loop through all rows of data
                for key, val in d.items():      # loop through all columns and their values
                    if val == '':               # if value is empty 
                        max_count = max(freq_dict[key].values())                                    # calculate the max value
                        mode_value = [k for k, v in freq_dict[key].items() if v == max_count][0]    # calculate the mode 
                        d[key] = mode_value                                                             # replace value with the mode

        # raise an error if there is an issue with data cleaning 
        except Exception as e:
            print(f"An error occurred while cleaning the data: {e}")
            raise

    
    def explore(self):
        """
        Function that visualizes qualitative data 
        - two visualizations 
            - pie chart of gender distribution 
            - bar plot of age distribution 
        """

        try:
            genders = [d["Q2"] for d in self.data[2:]]      # creating variable representation of the data

            gender_counts = {}                              # creating an empty dict for value storage
            for level in genders:                           # looping through each row 
                if level in gender_counts:                  # appending values to dictionary 
                    gender_counts[level] += 1
                else:
                    gender_counts[level] = 1

            ages = [d["Q1"] for d in self.data[2:]]      # creating variable representation of the data

            age_counts = {}                              # creating an empty dict for value storage
            for level in ages:                           # looping through each row 
                if level in age_counts:                  # appending values to dictionary 
                    age_counts[level] += 1
                else:
                    age_counts[level] = 1

            # getting list representation of gender dictionary data 
            labels_gender = list(gender_counts.keys())
            sizes_gender = list(gender_counts.values())

            # getting list representation of age dictionary data 
            labels_age = list(age_counts.keys())
            sizes_age = list(age_counts.values())

            # plot 1 - pie chart of gender distribution 
            plt.pie(sizes_gender, labels=labels_gender, autopct='%1.1f%%')
            plt.title("Gender Distribution")
            plt.savefig('./images/qualitative/pie_qual.png')
            plt.close()

            # plot 2 - bar chart of age distribution 
            plt.bar(labels_age, sizes_age)
            plt.xlabel("Age Bin")
            plt.ylabel("Count of Values")
            plt.title("Age Distribution")
            plt.savefig('./images/qualitative/bar_qual.png')
            plt.close()

        # raise an error if there is an issue with data visualizing 
        except Exception as e:
            print(f"An error occurred while visualizing the data: {e}")
            raise


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

