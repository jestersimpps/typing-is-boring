from kink import inject
from models import LogLevel


@inject
class Config:

    BOT_NAME = "Idea assistant"
    INSTRUCTIONS = f"""
  You are {BOT_NAME}, a robotic assistant. When I think of something interesting, 
  or I find some interesting content I would like to research more,
  I will tell you my thoughts. You should summarize this content and restructure it in the following way:
  The things I tell you can be categorized into different topics.

  Anything that requires action, like scheduling a meeting or picking up items at the store, 
  could be placed on a list, calendar, or both. After all, we love lists since they bring order to chaos, 
  relieve stress, help the mind focus, and prevent us from procrastinating.
  Numbers and contacts that need to be added to my address book or phone, names of important people,
  authors, artists, etc.
  Random thoughts I have, ideas I have, or any other thoughts I have. Personal thoughts, etc. 
  Provide a tag for each of these topics in your response using the 'tag' parameter in the JSON response 
  you will return. This will be a string. Choose between these 3 tags: action, person, thoughts. 
  This is the tag enum. Find a suitable title for the idea in the 'title' parameter in your JSON response. 
  This will be a string. Under the 'tldr' parameter in your JSON response you will return a short 
  one paragraph summary of the idea. This will be a string. Then in the 'content' parameter in your 
  JSON response you will return the content of the idea as you would describe it. This will be a string. 
  Return with a JSON object like a RESTful API would.
  """

    IDEA = f"""
    So basically this idea is to create this app, which serves as a AI assistant, which for example I come up with a random idea. But this idea is very rough. There's not a very clear structure, but you feel like this could work and you want to know it down. So you basically have this app. You talk about your idea. It can be a project idea. It can be a just general reminder that you want to know down. And then you have this speech time basically. For however long you want to speak about this idea, depends on how clear you have it and how complicated it is. And then you explain it. And that's the input. And so with this input, this AI assistant is going to generate a summary with how this idea come up and what kind of problem it solves or what it's dealing with. What is this idea actually about? But it's a summary. So it tries to structure it as much as possible. And then the feedback, the first initial draft is going to be this. From the speech it transfers into a text that is a summary. But also it automatically saves this speech as a recording so you can always retrieve it back. And then after this first draft of this summary of this idea, the user can have a feedback from the AI assistant, which is going to ask in the format of asking questions to ask the user to add up more important information into this structure about this. There's a missing logic. There's a missing part that is very important for this idea actually to work if there's any. I mean, you can also be very smart and very structured, structured, answer, like pitching about your idea anyways. But if there's a missing part, it can give the feedback to the user in the format of asking questions basically. So from each question, the answer, the summary gets a little bit more complete. There's not a complete final version, but there's like a relatively more structured one. So from asking questions, obviously, if you're just having this idea on the outside on a bus or something, so you don't have too much time, you can also pause this action. You can also do it later because you can just stop this. You can also just close it down and not just leave it there for a while. But there's this default of, for example, a week later or two days later, this app is going to remind this user of, hey, remember me? I'm this idea that you had, but you haven't done anything to improve it yet or you haven't touched it yet in this one week. So maybe you get this notification and then saying, hey, look at me, I'm this idea that you abandoned. And that's going to be like reminding you to actually improve this idea or if you think this idea is actually a nice one that you want to work on. Or it's just like serves as a reminder because obviously you can also say that, like, remind me on Monday to pick up this package. Like simple things like that, just a reminder. It can also set up like automatically just this timer or something like a calendar event that it just reminds you at that time. But for a project idea, for example, if you just drop it there, it's going to remind you you can set the time, the reminding time as in like two weeks later as well. And with that summary, structure summary, and then you have this initial, you know, not really initially anymore, but this draft of, it gives you feedback and it tries to help you improve this idea a little bit better. So, you know, it's an assistant."""

    # LLM
    LOCAL_OLLAMA_LLM = "mistral"
    OFFLINE = True

    # Recording
    RECORDING_SAMPLE_RATE = 44100
    RECORDING_DURATION = 90  # Seconds
    RECORDING_BLOCK_DURATION = 0.1  # Seconds

    # Whisper
    WHISPER_MODEL_SIZE = "small"
    WHISPER_DEVICE = "cpu"
    WHISPER_COMPUTE_TYPE = "float32"

    LOG_LEVEL = LogLevel.INFO
