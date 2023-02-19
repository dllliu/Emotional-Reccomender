import cohere
co = cohere.Client('1HkWOHG9s2OKGjyv3CYy6wDfws4WWWuGdenqyGAz')
from cohere.classify import Example

examples=[
Example("I just can't seem to shake this feeling of heaviness", "Sadness"),
Example("Everything feels gray and dull", "Sadness"),
Example("I don't have the energy to do anything anymore", "Sadness"),
Example("It's like a weight on my chest that won't go away", "Sadness"),
Example("I feel like I'm drowning in my own emotions", "Sadness"),
Example("I don't remember the last time I genuinely smiled", "Sadness"),
Example("I just want to crawl into bed and stay there", "Sadness"),
Example("Nothing seems to bring me joy anymore", "Sadness"),
Example("I feel like I'm all alone in a crowded room", "Sadness"),
Example("I keep thinking about what could have been", "Sadness"),
Example("I can't believe they did that to me", "Anger"),
Example("I'm so frustrated that I could scream", "Anger"),
Example("Why do they always have to push my buttons?", "Anger"),
Example("I feel like I'm about to explode", "Anger"),
Example("It's like they're not even listening to me", "Anger"),
Example("I'm tired of being treated like this", "Anger"),
Example("I just want to punch something", "Anger"),
Example("I feel like they're purposely trying to make me mad", "Anger"),
Example("I can't believe I let them get under my skin", "Anger"),
Example("I'm sick of their excuses", "Anger"),
Example("I wish there were someone to talk to" ,"Loneliness"),
Example("I feel like I'm always on the outside looking in" ,"Loneliness"),
Example("I keep trying to make plans with people but no one ever seems to have time for me" ,"Loneliness"),
Example("Even though I know it's not true sometimes it feels like I'm the only person in the world" ,"Loneliness"),
Example("I just want someone to understand me" ,"Loneliness"),
Example("I'm tired of feeling like I'm missing out on life" , "Loneliness"),
Example("I feel like I'm stuck in a bubble watching the world go by without me", "Loneliness"),
Example("I wish I could find someone who truly gets me", "Loneliness"),
Example("I'm tired of pretending like I'm okay" ,"Loneliness"),
Example("It's like I'm invisible to everyone around me" ,"Loneliness"),
Example("I just want to be around people who care about me" ,"Loneliness"),
Example("I don't know how to make friends as an adult", "Loneliness"),
Example("Oh my goodness I can't believe it!", "Surprise"),
Example("I am completely taken aback how did this happen?", "Surprise"),
Example("Well I wasn't expecting that!", "Surprise"),
Example("Oh wow that's amazing news!", "Surprise"),
Example("Holy cow I never saw that coming!", "Surprise"),
Example("Are you serious? That's unbelievable!", "Surprise"),
Example("Well color me shocked!", "Surprise"),
Example("No way I'm in complete disbelief!", "Surprise"),
Example("I am absolutely floored by this revelation!", "Surprise"),
Example("Goodness gracious I'm completely astonished!", "Surprise"),
Example("I'm so happy I can't stop smiling!", "Joy"),
Example("This is the best day ever I'm over the moon!", "Joy"),
Example("I'm feeling so elated life is good!", "Joy"),
Example("I'm feeling on top of the world nothing can bring me down!", "Joy"),
Example("I'm absolutely thrilled this is amazing news!", "Joy"),
Example("I'm beaming with happiness everything is perfect!", "Joy"),
Example("I'm filled with so much joy I could burst!", "Joy"),
Example("I'm in seventh heaven right now nothing can ruin this feeling!", "Joy"),
Example("I'm feeling so grateful and blessed life is beautiful!", "Joy"),
Example("I'm feeling overjoyed my heart is overflowing with happiness!", "Joy"),
Example("I feel like something's not right here", "Fear"),
Example("I'm getting a bad feeling about this", "Fear"),
Example("My heart is pounding in my chest", "Fear"),
Example("I can't shake off this feeling of unease", "Fear"),
Example("I'm too scared to even move", "Fear"),
Example("I don't want to even think about what could go wrong", "Fear"),
Example("I have a sense of impending doom", "Fear"),
Example("I can't handle this fear anymore", "Fear"),
Example("I feel paralyzed with fear", "Fear"),
Example("I'm scared out of my mind", "Fear"),
Example("I'm having a panic attack!", "Fear"),
Example("I can't breathe I'm so scared!", "Fear"),
Example("I can't even stand the thought of it", "Disgust"),
Example("I feel like I need to wash my hands after touching that", "Disgust"),
Example("Ugh just looking at it makes me queasy", "Disgust"),
Example("I can't believe people actually eat that", "Disgust"),
Example("Yikes that smell is making me gag", "Disgust"),
Example("Sorry I just can't stomach it", "Disgust"),
Example("Get that away from me please", "Disgust"),
Example("I'm feeling a bit nauseous just thinking about it", "Disgust"),
Example("I think I'm going to be sick", "Disgust"),
Example("That's just repulsive", "Disgust"),
Example("I'm really sorry I shouldn't have said that", "Remorse"),
Example("I wish I could take back what I did", "Remorse"),
Example("I feel terrible about what happened", "Remorse"),
Example("I didn't mean to hurt you", "Remorse"),
Example("I regret my actions and I'm sorry", "Remorse"),
Example("I feel awful about what I said", "Remorse"),
Example("I should have handled that situation differently", "Remorse"),
Example("I understand now that I was wrong", "Remorse"),
Example("I take full responsibility for my mistake", "Remorse"),
Example("I want to make things right", "Remorse"),
Example("I believe in you and I trust your judgment", "Trust"),
Example("You can count on me to keep your secrets safe", "Trust"),
Example("I have complete faith in your abilities", "Trust"),
Example("I trust that you will make the right decision", "Trust"),
Example("You've earned my trust and I won't betray it", "Trust"),
Example("I know that I can depend on you", "Trust"),
Example("I trust that you have my best interests at heart", "Trust"),
Example("I'm confident that you'll come through for me", "Trust"),
Example("I trust that you will follow through on your promises", "Trust"),
Example("You've shown that you're trustworthy and I appreciate that", "Trust")
]


"""
response = co.classify(
  model='large',
  inputs=inputs,
  examples=examples,
)
"""

val = input("How are you feeling today: ")
arr = []
arr.append(val)
response = co.classify(
  model='large',
  inputs=arr,
  examples=examples,
)
print('The confidence levels of the labels are: {}'.format(
response.classifications))
