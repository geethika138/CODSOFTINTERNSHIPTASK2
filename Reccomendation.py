data = [
    {'user_id': 1, 'movie_id': 'Inception', 'rating': 5},
    {'user_id': 1, 'movie_id': 'Interstellar', 'rating': 4},
    {'user_id': 1, 'movie_id': 'The Dark Knight', 'rating': 5},
    {'user_id': 2, 'movie_id': 'Inception', 'rating': 4},
    {'user_id': 2, 'movie_id': 'The Matrix', 'rating': 5},
    {'user_id': 3, 'movie_id': 'Interstellar', 'rating': 3},
    {'user_id': 3, 'movie_id': 'The Matrix', 'rating': 4},
    {'user_id': 3, 'movie_id': 'Gladiator', 'rating': 2}
]
def get_movie_ratings():
    movie_ratings = {}
    for entry in data:
        movie_id = entry['movie_id']
        rating = entry['rating']
        if movie_id not in movie_ratings:
            movie_ratings[movie_id] = {'total_rating': 0, 'count': 0}
        movie_ratings[movie_id]['total_rating'] += rating
        movie_ratings[movie_id]['count'] += 1
    for movie_id in movie_ratings:
        movie_ratings[movie_id]['average'] = movie_ratings[movie_id]['total_rating'] / movie_ratings[movie_id]['count']
    return movie_ratings
def get_movie_recommendations(user_id, n_recommendations=5):
    user_ratings = [entry for entry in data if entry['user_id'] == user_id]
    movie_ratings = get_movie_ratings()
    rated_movies = {entry['movie_id'] for entry in user_ratings}
    recommendations = {movie_id: details['average'] for movie_id, details in movie_ratings.items() if movie_id not in rated_movies}    
    top_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]    
    return top_recommendations
def add_rating(user_id, movie_id, rating):
    if 1 <= user_id <= 30 and 1 <= rating <= 5:
        data.append({'user_id': user_id, 'movie_id': movie_id, 'rating': rating})
        print(f"Added rating: User {user_id} rated Movie '{movie_id}' with {rating}")
    else:
        print("Invalid user ID or rating. User ID should be between 1 and 30, rating between 1 and 5.")
def display_all_movies():
    movie_ratings = get_movie_ratings()
    print("All Movies with Average Ratings:")
    for movie_id, details in movie_ratings.items():
        print(f"Movie: '{movie_id}', Average Rating: {details['average']:.2f}")
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Get recommendations")
        print("2. Add a rating")
        print("3. Display all movies with average ratings")
        print("4. Exit")       
        choice = input("Choose an option: ")  
        if choice == '1':
            user_id = int(input("Enter user ID for recommendations (1-30): "))
            if 1 <= user_id <= 30:
                recommendations = get_movie_recommendations(user_id)
                print(f"Top recommendations for user {user_id}:")
                for movie_id, rating in recommendations:
                    print(f"Movie: '{movie_id}', Average Rating: {rating:.2f}")
            else:
                print("Invalid user ID. Please enter a number between 1 and 30.")        
        elif choice == '2':
            user_id = int(input("Enter user ID (1-30): "))
            movie_id = input("Enter movie name: ")
            rating = float(input("Enter rating (1-5): "))
            add_rating(user_id, movie_id, rating)       
        elif choice == '3':
            display_all_movies() 
        elif choice == '4':
            print("Exiting........Thankyou!!!!")
            break
        else:
            print("Invalid option, please try again.")
