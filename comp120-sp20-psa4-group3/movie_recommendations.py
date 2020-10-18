"""
Name: movie_recommendations.py
Date: 3/31/2020
Author: Quinn Bigane & Tom Padova
Description: Based on a Movie ratings data base of various users, this program will recoomend a user a movie
"""
import re
import math
import csv
from scipy.stats import pearsonr

class BadInputError(Exception):
    """Exception for when the program tries to call a meathod or class with a bad input"""
    pass

class Movie_Recommendations:


    # Constructor
    def __init__(self, movie_filename, training_ratings_filename):
        """
        Initializes the Movie_Recommendations object from 
        the files containing movie names and training ratings.  
        The following instance variables should be initialized:
        self.movie_dict - A dictionary that maps a movie id to
               a movie object (objects the class Movie)
        self.user_dict - A dictionary that maps user id's to a 
               a dictionary that maps a movie id to the rating
               that the user gave to the movie.    
        """
        # variable initialization
        # {movieID:MovieObject}
        self.movie_dict = {}
        # {UserID:User_Ratings}
        self.user_dict = {}
        #{movie_id:ratings}
       
        
        #Opens the Movie file fed to Movie_Recommendations as a csv reader
        f = open(movie_filename,encoding='utf-8')
        csv_reader = csv.reader(f, delimiter = ',',quotechar = '"')

        #loops through the Movie file, adds Movie class instance to
        #  dictionary mapped by ID
        for line in csv_reader:
            if re.fullmatch("[0-9]+",line[0]):
                self.movie_dict[int(line[0])] = Movie(int(line[0]),line[1])
        # print(self.movie_dict["1"].title)
        f.close()



        #Opens the User rating file fed to Movie_Recommendations as a csv reader
        f = open(training_ratings_filename,encoding='utf-8')
        csv_reader = csv.reader(f, delimiter = ',',quotechar = '"')

       #loops through the User Ratings file fed to Movie_Recommendations
       #creating a dictionary {userID:{movieID:rating,movieID:rating}}
       
        for line in csv_reader:
            if re.fullmatch("[0-9]+",line[0]):
                if int(line[0]) not in self.user_dict:
                    self.user_dict[int(line[0])] = {}
                self.user_dict[int(line[0])][int(line[1])] = float(line[2])
                self.movie_dict[int(line[1])].users.append(int(line[0]))
        f.close()

                
    

    def predict_rating(self, user_id, movie_id):
        """
        Returns the predicted rating that user_id will give to the
        movie whose id is movie_id. 
        If user_id has already rated movie_id, return
        that rating.
        If either user_id or movie_id is not in the database,
        then BadInputError is raised.
        """
        if user_id not in self.user_dict or movie_id not in self.movie_dict:      # make sure the user and movie exist, if not raise BadInputError
            raise BadInputError

        elif user_id in self.movie_dict[int(movie_id)].users:      # check if user has already rated this movie
            actual_rating = self.user_dict[user_id][movie_id]
            return actual_rating
        
        else:
            d_users_movies_to_ratings = self.user_dict[user_id]
            user_rated_list = d_users_movies_to_ratings.keys()      # movies user_id has rated (sorta like a list)
            total_weighted_scores = 0       # initialize local variables
            sum_of_similarities = 0
            for movie in user_rated_list:
                sim_score = self.movie_dict[movie_id].get_similarity(int(movie), self.movie_dict, self.user_dict) # find sim score using get_similarity
                sum_of_similarities += sim_score    # add each similarity to the total similarites
                actual_rating_of_movie_being_compared = float(self.user_dict[user_id][movie])       # find rating of the movie being compared
                weighted_score = sim_score * actual_rating_of_movie_being_compared      # weight the score of each movie based on the similarity and add this to the total of the weighted scores
                total_weighted_scores += weighted_score
            if sum_of_similarities == 0:    # if no similar movies, return a predicted score of 2.5
                return 2.5
            else:       # find the weighted average of the scores and return this as the predicted rating
                predicted_rating = total_weighted_scores / sum_of_similarities
                return predicted_rating

    def predict_ratings(self, test_ratings_filename):
        """
        Returns a list of tuples, one tuple for each rating in the
        test ratings file.
        The tuple should contain
        (user id, movie title, predicted rating, actual rating)
        """
        
        list_of_tuples = [] # initialize the list to be returned and open the file
        test_ratings_f = open(test_ratings_filename, "r")

        for line in test_ratings_f: # loop through all lines of the file
            if re.fullmatch("[0-9]+",line[0]): # only consider lines that start with a number (skip the title line)
                tokens = line.split(',')       # predict the ratings the user would give to each movie they have rated
                user_id = int(tokens[0])
                movie_id = int(tokens[1])
                movie_title = self.movie_dict[int(movie_id)].title
                predicted_rating = self.predict_rating(int(user_id), int(movie_id)) # use predict_rating to compute the predicted rating of each movie
                actual_rating = float(tokens[2])
                list_of_tuples.append((int(user_id), movie_title, predicted_rating, actual_rating)) # create the tuple with the relevant information


        return list_of_tuples

        
    def correlation(self, predicted_ratings, actual_ratings):
        """
        Returns the correlation between the values in the list predicted_ratings
        and the list actual_ratings.  The lengths of predicted_ratings and
        actual_ratings must be the same.
        """
        return pearsonr(predicted_ratings, actual_ratings)[0]
        
class Movie: 
    """
    Represents a movie from the movie database.
    """
    def __init__(self, movie_id, title):
        """ 
        Constructor.
        Initializes the following instances variables.  You
        must use exactly the same names for your instance 
        variables.  (For testing purposes.)
        id: the id of the movie
        title: the title of the movie
        users: list of the id's of the users who have
            rated this movie.  Initially, this is
            an empty list, but will be filled in
            as the training ratings file is read.
        similarities: a dictionary where the key is the
            id of another movie, and the value is the similarity
            between the "self" movie and the movie with that id.
            This dictionary is initially empty.  It is filled
            in "on demand", as the file containing test ratings
            is read, and ratings predictions are made.
        """
        # variable initialization
        self.id = movie_id              #id of this movie
        self.title = title              #title of this movie
        self.users = []                 #list of users who rated this movie
        self.similarities = {}          #ongoing dictionary mapping other movies to their similarity score to this movie

    def __str__(self):
        """
        Returns string representation of the movie object.
        Handy for debugging.
        """
        
        #The code wants to return a string so test is here as a stand in
        return 'Movie class'

    def __repr__(self):
        """
        Returns string representation of the movie object.
        """

        return "ID:" + str(self.id) + ", Title:" + str(self.title) 

    def get_similarity(self, other_movie_id, movie_dict, user_dict):
        """ 
        Returns the similarity between the movie that 
        called the method (self), and another movie whose
        id is other_movie_id.  (Uses movie_dict and user_dict)
        If the similarity has already been computed, return it.
        If not, compute the similarity (using the compute_similarity
        method), and store it in both
        the "self" movie object, and the other_movie_id movie object.
        Then return that computed similarity.
        If other_movie_id is not valid, raise BadInputError exception.
        """
        #if this function is called with a movie not in our dictionary
        if other_movie_id not in movie_dict.keys():
            raise BadInputError
        #if this function is called and the similarity score has already been recorded
        elif other_movie_id in self.similarities.keys():
            return self.similarities[other_movie_id]
        #if this function is called and the similarity score still needs to be calculated
        else:
            #compute similarity score
            sim_score = self.compute_similarity(other_movie_id, movie_dict, user_dict)
            #store the similarity score in this movies similarities data base
            movie_dict[self.id].similarities[other_movie_id] = sim_score
            #store the similarity score in the other movies similarity data base
            movie_dict[other_movie_id].similarities[self.id] = sim_score
            return sim_score
                

    def compute_similarity(self, other_movie_id, movie_dict, user_dict):
        """ 
        Computes and returns the similarity between the movie that 
        called the method (self), and another movie whose
        id is other_movie_id.  (Uses movie_dict and user_dict)
        """
        #initialize required variables
        sum_of_difference = 0
        similarity_score = 0
        counter = 0
        #for every user who has rated this movie
        for user in self.users:
            #if that movie has also rated the movie being compared
            if user in movie_dict[other_movie_id].users:
                #add the difference of their ratings to a running sum and counter +1 for calculating the average
                sum_of_difference += abs(float(user_dict[user][self.id]) - float(user_dict[user][other_movie_id]))
                counter += 1
        #if their were no users who rated both movies, return a similarity score of 0
        if counter == 0:
            return 0
        #if their were users who rated both movies, return a similarity score = 1 - (average of the differences / 4.5)
        else:
            similarity_score = 1 - (sum_of_difference / counter)/4.5
            return similarity_score
        


        
if __name__ == "__main__":
    # Create movie recommendations object.
    movie_recs = Movie_Recommendations("movies.csv", "training_ratings.csv")

    # Predict ratings for user/movie combinations
    rating_predictions = movie_recs.predict_ratings("test_ratings.csv")
    print("Rating predictions: ")

    
    for prediction in rating_predictions:
        print(prediction)
    predicted = [rating[2] for rating in rating_predictions]
    actual = [rating[3] for rating in rating_predictions]
    print(predicted)
    print(actual)
    correlation = movie_recs.correlation(predicted, actual)
    print(f"Correlation: {correlation}")    