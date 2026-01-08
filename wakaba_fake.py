
import random

#わかばという女の子と会話できる
NAME = "わかば"

EMPATHY = [
    "それはつらかったね。",
    "大変だったんだね。",
    "よく頑張ったと思う。",
    "無理しなくていいんだよ。"
]


QUESTIONS = [
    "もう少し話してもいい？",
    "それって、いつ頃のこと？",
    "今はどんな気持ち？",
    "私でよければ聞くよ。"
]


POSITIVE_WORDS = ["楽しい", "嬉しい", "よかった","最高"]
NEGATIVE_WORDS = ["疲れた", "つらい", "悲しい", "しんどい"]


def judge_mood(text):
    if any(word in text for word in NEGATIVE_WORDS):
        return "negative"
    if any(word in text for word in POSITIVE_WORDS):
        return "positive"
    return "neutral"


print(f"{NAME}:こんにちは。今日はどんな気分？（exitで終了）")


while True:
    user = input("あなた:")
    if user.lower() == "exit":
        print(f"{NAME}:また話そうね。おやすみ。")
        break


    mood = judge_mood(user)


    if mood == "negative":
        reply = random.choice(EMPATHY) + random.choice(QUESTIONS)
    elif mood == "positive":
        reply = "それはよかったね。" + random.choice(QUESTIONS)
    else:
        reply = "うんうん" + random.choice(QUESTIONS)
        
    print(f"{NAME}:{reply}")