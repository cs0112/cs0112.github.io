from dataclasses import dataclass
import csv
import math
import re

# Regular expression to match any character that is not a letter, number, or underscore
bad_characters = re.compile(r"[^\w]")

@dataclass
class Song:
    id: int
    title: str
    year: int
    artist: str
    genre: str
    lyrics: list


def clean_word(word: str) -> str:
    """
    Clean a single word by removing non-word characters and converting to lowercase.
    
    :param word: The word to clean
    :return: The cleaned word
    """
    word = word.strip().lower()
    return bad_characters.sub("", word)


def clean_lyrics(lyrics: str) -> list:
    """
    Clean and tokenize the lyrics of a song.
    
    :param lyrics: The lyrics of a song as a string.
    :return list: A list of cleaned words from the lyrics.
    """
    lyrics = lyrics.replace("\n", " ")
    return [clean_word(word) for word in lyrics.split(" ")]


def create_corpus(filename: str) -> list:
    """
    Create a corpus of songs from a CSV file.
    
    :param filename (str): The name of the CSV file containing song data.
    :return list: A list of Song objects representing the corpus.
    """
    corpus = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None) # Skip header if present
        for i, row in enumerate(reader):
            if row[4] != "Not Available":
                corpus.append(Song(i, # ID
                                   row[1], # Title
                                   int(row[2]), # Year
                                   row[3], # Artist
                                   row[4], # Genre
                                   clean_lyrics(row[5]))) # Lyrics
        return corpus


def compute_idf(corpus: list) -> dict:
    """
    Compute the Inverse Document Frequency (IDF) for each word in the corpus.
    
    :param corpus (list): A list of Song objects.
    :return dict: A dictionary mapping words to their IDF values.
    """
    # TODO: Implement this function
    pass


def compute_tf(song_lyrics: list) -> dict:
    """
    Compute the Term Frequency (TF) for a set of lyrics.
    
    :param song_lyrics (list): A list of words representing the lyrics of a song.
    :return dict: A dictionary mapping words to their term frequencies.
    """
    # TODO: Implement this function
    pass


def compute_tf_idf(song_lyrics: list, corpus_idf: dict) -> dict:
    """
    Compute the TF-IDF weights for a song.
    
    :param song_lyrics (list): A list of words representing the lyrics of a song.
    :param corpus_idf (dict): A dictionary of IDF values for the corpus.
    :return dict: A dictionary mapping words to their TF-IDF weights for the song.
    """
    # TODO: Implement this function
    pass


def compute_corpus_tf_idf(corpus: list, corpus_idf: dict) -> dict:
    """
    Compute TF-IDF weights for all songs in the corpus.
    
    :param corpus (list): A list of Song objects.
    :param corpus_idf (dict): A dictionary of IDF values for the corpus.
    :return dict: A dictionary mapping song IDs to their TF-IDF dictionaries.
    """
    # TODO: Implement this function
    pass


def cosine_similarity(l1: dict, l2: dict) -> float:
    """
    Calculate the cosine similarity between two TF-IDF vectors.
    
    :param l1 (dict): TF-IDF weights for the first song.
    :param l2 (dict): TF-IDF weights for the second song.
    :return float: The cosine similarity between the two songs.
    """
    common_words = set(l1.keys()) & set(l2.keys())
    dot_product = sum(l1[word] * l2[word] for word in common_words)
    magnitude1 = math.sqrt(sum(w * w for w in l1.values()))
    magnitude2 = math.sqrt(sum(w * w for w in l2.values()))
    return dot_product / (magnitude1 * magnitude2) if magnitude1 * magnitude2 else 0


def nearest_neighbor(song_lyrics: str, corpus: list, corpus_tf_idf: dict, corpus_idf: dict) -> Song:
    """
    Find the most similar song in the corpus to the given lyrics.
    
    :param song_lyrics (str): The lyrics of the song to compare.
    :param corpus (list): A list of Song objects.
    :param corpus_tf_idf (dict): TF-IDF weights for all songs in the corpus.
    :param corpus_idf (dict): IDF values for the corpus.
    :return Song: The most similar Song object from the corpus.
    """
    # TODO: Implement this function
    pass


def main(filename: str, lyrics: str):
    """
    Main function to run the song recommendation system.
    
    :param filename (str): The name of the CSV file containing song data.
    :param lyrics (str): The lyrics of the song to find recommendations for.
    """
    corpus = create_corpus(filename)
    corpus_idf = compute_idf(corpus)
    corpus_tf_idf = compute_corpus_tf_idf(corpus, corpus_idf)
    nearest_song = nearest_neighbor(lyrics, corpus, corpus_tf_idf, corpus_idf)
    print(f"Recommended Genre: {nearest_song.genre}")
    print(f"Recommended Song: {nearest_song.title} by {nearest_song.artist}")


if __name__ == "__main__":
    # Example usage
    filename = "small.csv"
    sample_lyrics = "Your sample lyrics here"
    main(filename, sample_lyrics)

