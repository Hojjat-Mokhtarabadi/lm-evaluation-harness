def round_score(dataset, type):
    score = dataset['Score']
    quotient = score // 25
    remainder = score % 25

    if remainder >= 13:
        rounded_score = (quotient + 1) * 25
    else:
        rounded_score = quotient * 25

    if type == "sentiment":
        score_labels = {
            0: "افتضاح",
            25: "بد",
            50: "متوسط",
            75: "خوب",
            100: "عالی"
        }
    elif type == "rating":
        score_labels = {
            0: "یک ستاره",
            25: "دو ستاره",
            50: "سه ستاره",
            75: "چهار ستاره",
            100: "پنج ستاره"
        }

    return score_labels.get(rounded_score, "Invalid Score")

def round_score_to_sentiment(dataset):
    return round_score(dataset, "sentiment")

def round_score_to_rating(dataset):
    return round_score(dataset, "rating")