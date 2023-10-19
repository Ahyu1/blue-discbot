import json
import os
import requests
from typing import Dict
import discord
from discord.ext import commands
from random import choice
from requests import Response
import time
import asyncio
import random

bot = discord.Client()

header = {"content-type: application/json; charset=utf-8"}
TOKEN = "secret"

@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot))

bot = commands.Bot(command_prefix='.', status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name='Tiebreaker'))
bot.remove_command('help')

@bot.command()
async def info(ctx, id: int):
    rob = requests.get('https://users.roblox.com/v1/users/{}'.format(id))
    rob = rob.json()

    name = rob['name']
    displayname = rob['displayName']
    aydi = rob['id']
    created = rob['created']
    bio = rob['description']
    verified = rob['hasVerifiedBadge']
    banned = rob['isBanned']

    embed = discord.Embed(title='ROBLOX USER INFO',
                          color=0xFFFFFF)

    embed.set_footer(text='API requests from https://users.roblox.com')
    embed.add_field(name='Name:', value=f'{name}', inline=False)
    embed.add_field(name='Display Name:', value=f'{displayname}', inline=False)
    embed.add_field(name='About me:', value=f'{bio}', inline=False)
    embed.add_field(name='Verified?', value=f'{verified}', inline=False)
    embed.add_field(name='Ban Status:', value=f'{banned}', inline=False)
    embed.add_field(name='ID:', value=f'{aydi}', inline=False)
    embed.add_field(name='Created at:', value=f'{created}', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='How to use commands?',
        description='These are the following commands that you can use to call the Bot.\n Please type the command prefix "." before the function.',
        color=discord.Colour.blue()
    )

    embed.add_field(name='function [add]', value='- to get the sum of the two integer\n*format: .add 5 5 (ans=10)*', inline=False)
    embed.add_field(name='function [minus]', value='- to get the difference between the two integer\n*format: .minus 20 10 (ans=10)*', inline=False)
    embed.add_field(name='function [multiply]', value='- to get the product of the two integer\n*format: .multiply 2 5 (ans=10)*', inline=False)
    embed.add_field(name='function [divide]', value='- to get the quotient of the two integer\n*format: .divide 100 10 (ans=10.0)*', inline=False)
    embed.add_field(name='function [sqrt]', value='- to find the square root of a number\n*format: .sqrt 3.162277 3.162277 (ans=10)*', inline=False)
    embed.add_field(name='function [gender]', value='- bot will guess the gender of a person by its name\n*format: .gender alexa*', inline=False)
    embed.add_field(name='function [weather]', value='- to get the current weather condition.\n*format: .weather london*', inline=False)
    embed.add_field(name='function [mycolor]', value='- to know tcolor based on your personality', inline=False)
    embed.add_field(name='function [info]', value='- get your roblox account\'s information', inline=False)
    embed.add_field(name='function [quiz]', value='- Blue will send a random question based from your chosen topic.', inline=False)
    embed.add_field(name='function [loop]', value='- Blue will execute an infinite loop.' , inline=False) #You can call the command *stop* to end the loop.'
    embed.add_field(name='function [hp_meme]', value='- to get a random *Harry Potter* meme', inline=False)
    embed.add_field(name='function [got_meme]', value='- to get a random *Game of Thrones* meme', inline=False)
    embed.add_field(name='function [whois]', value='- get the info of the specific discord user', inline=False)
    embed.add_field(name='function [Blue]', value='- to call the Bot', inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def test(ctx):
    await ctx.send('I\'m working.')

@bot.command()
async def Blue(ctx):
    await ctx.send('I\'m here...')

#bot.command()
#async def hi(ctx):
#    await ctx.send('Hello ' + ctx.message.author.mention + '!')

@bot.command()
async def gm(ctx):
    await ctx.send('Good morning sunshine daisy mellow!')

@bot.command()
async def gn(ctx):
    await ctx.send('Have a good night sleep.')

@bot.command(name='whois')
async def whois (ctx, user:discord.Member=None):
    embed = discord.Embed(color=0xFFFFFF, timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {user}')
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID: ', value=user.id, inline=False)
    embed.add_field(name='Created at', value=user.created_at, inline=False)
    embed.add_field(name='Joined at', value=user.joined_at, inline=False)

    embed.add_field(name='Bot?', value=f'{user.bot}')

    await ctx.send(embed=embed)

@bot.command()
async def im_hungry(ctx):
    feedback = ['I don\'t care',
                'Why tell me?',
                'eat the fuck you want',
                'You must eat right now! don\'t want you to starve.',
                'what do you want to eat? go grab it!',
                'I am also hungry. Pls don\'t interrupt a hungry person.']

    await ctx.send(choice(feedback))

@bot.command()
async def status(ctx, boy: str, girl: str):
    x = random.randint(1, 99)
    status = ['lovers', 'enemies', 'friends']
    s = choice(status)
    men = boy.capitalize()
    wn = girl.capitalize()

    await ctx.send('{} and {} are {}% {}'.format(men, wn, x, s))

@bot.command()
async def im_bored(ctx):
    embed = discord.Embed(
        title='Here you go, watch it. It\'s so good.\n' + 'https://www.netflix.com/ph/title/81205849',
        color=0x000FF
    )

    await ctx.send(embed=embed)

@bot.command()
async def gender(ctx, name: str):
    global embed
    gen = requests.get('https://api.genderize.io?name={}'.format(name))
    gen = gen.json()

    sex = gen['gender']

    if sex == 'male':
        await ctx.send('male ♂🙋‍♂️')

    if sex =='female':
        await ctx.send('female ♀🙋‍♀️')


@bot.command()
async def abcd(ctx):
    should_loop = True

    async def looper():
        while should_loop:
            await ctx.send('looping')

    async def listener():
        nonlocal should_loop
        try:
            await bot.wait_for("message", check=lambda m: m.content == "stop".lower(), timeout=60)
        except asyncio.TimeoutError:
            pass
        else:
            should_loop = False

    await asyncio.gather(looper(), listener())

@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
    sum = f'{a} + {b} = {a + b}'
    embed = discord.Embed(
        title='ADDITION',
        description=f'{sum}',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='--Pascaline Bot--')
    embed.set_author(name='Aladdin\'s Calcu',
                     icon_url='https://cdn.pixabay.com/photo/2018/07/05/19/10/mathematic-3518980_960_720.png')
    embed.set_thumbnail(url='https://www.computerhope.com/jargon/p/plus.png')

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def minus(ctx, a: int, b: int):
    ans = f'{a} - {b} = {a - b}'
    embed = discord.Embed(
        title='SUBTRACTION',
        description=f'{ans}',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='--Pascaline Bot--')
    embed.set_author(name='Aladdin\'s Calcu',
                     icon_url='https://cdn.pixabay.com/photo/2018/07/05/19/10/mathematic-3518980_960_720.png')
    embed.set_thumbnail(url='https://www.emoji.co.uk/files/phantom-open-emojis/symbols-phantom/13105-heavy-minus-sign.png')

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    product = f'{a} x {b} = {a * b}'
    embed = discord.Embed(
        title='MULTIPLICATION',
        description=f'{product}',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='--Pascaline Bot--')
    embed.set_author(name='Aladdin\'s Calcu',
                     icon_url='https://cdn.pixabay.com/photo/2018/07/05/19/10/mathematic-3518980_960_720.png')
    embed.set_thumbnail(url='https://e7.pngegg.com/pngimages/474/777/png-clipart-multiplication-sign-computer-icons-symbol-tache-blue-angle.png')

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def divide(ctx, a: int, b: int):
    quotient = f'{a} / {b} = {a / b}'
    embed = discord.Embed(
        title='DIVISION',
        description=f'{quotient}',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='--Pascaline Bot--')
    embed.set_author(name='Aladdin\'s Calcu',
                     icon_url='https://cdn.pixabay.com/photo/2018/07/05/19/10/mathematic-3518980_960_720.png')
    embed.set_thumbnail(url='https://www.silhouette.pics/images/quotes/english/general/blue-divide-sign-silhouette-image-52650-148835.jpg')

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def sqrt(ctx, a: int, b: int):
    squared = f'{a ** b}'
    embed = discord.Embed(
        title='SQUARE ROOT',
        description=f'{squared}',
        colour=discord.Colour.blue()
    )

    embed.set_footer(text='--Pascaline Bot--')
    embed.set_author(name='Aladdin\'s Calcu',
                     icon_url='https://images.app.goo.gl/pdfr2vVRjbMAUVjf8')
    embed.set_thumbnail(url='https://library.kissclipart.com/20180904/ope/kissclipart-square-root-clipart-square-number-square-root-d574ba6065e4a6b4.jpg')

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def mycolor(ctx):
    colors = [0x0000FF, 0xFF0000, 0xFFFF00, 0xFFA500, 0x00FF00, 0x8F00FF, 0xFFC0CB]
    color_dict = {
        0x000FF: "BLUE\n-Calls to mind feelings of calmness or serenity. It is a sign of stability and reliability",
        0xFF0000: "RED\n-You are a determined person who takes action and are not afraid of taking risks",
        0xFFFF00: "YELLOW\n-You have an illuminating and cheerful essence",
        0xFFA500: "ORANGE\n-Your personality strengths tend to be witty, spontaneous, generous, optimistic, eager and bold",
        0x00FF00: "GREEN\n-Your personality strengths tend to be perfectionistic, analytical, conceptual, cool, and logical",
        0x8F00FF: "VIOLET\n-You are very intuitive and deeply interested in spirituality",
        0xFFC0CB: "PINK\n-You are romantic and approachable. people get easily attracted on you"
    }

    random_color = choice(colors)
    embed = discord.Embed(
        title='What Color Is You?',
        description=f'My source says you are closely to color {color_dict[random_color]}!',
        color=random_color
    )
    embed.set_footer(text='source: google')
    embed.set_author(name='Aladdin\'s Rainbow')
    embed.set_thumbnail(url='https://clipart.world/wp-content/uploads/2020/06/Colorful-Question-Mark-clipart.png')

    await ctx.send(embed=embed)

@bot.command()
async def got_meme(ctx):
    urls = ['https://i.redd.it/eh5prz21pde81.jpg',
            'https://i.redd.it/3cot9k8qg4h81.jpg',
            'https://i.redd.it/55td3jff89g81.jpg',
            'https://i.pinimg.com/564x/54/5a/c2/545ac2301b80074e26fbd5db520feafe.jpg'
            'https://i.pinimg.com/564x/3f/7d/50/3f7d5068eea8648adff7f1762075ae06.jpg',
            'https://i.pinimg.com/564x/9b/5d/c8/9b5dc8771af9012de078590511e3893a.jpg',
            'https://i.pinimg.com/564x/52/e3/40/52e340a5e7d5e4f426d9de2527654d27.jpg',
            'https://i.pinimg.com/564x/05/f9/8a/05f98a3161e37faa93a76752bde9ec94.jpg',
            'https://i.pinimg.com/564x/7d/51/e1/7d51e192bdf1720f7dd1452c67ae7dbc.jpg',
            'https://i.pinimg.com/736x/3f/7d/5c/3f7d5c617508c18783f5b748bc7778dc.jpg',
            'https://i.pinimg.com/564x/93/e3/7f/93e37f650bb4d2a8485c52d0523a634a.jpg',
            'https://i.pinimg.com/564x/24/09/16/2409161cc6f39512517f681f199cc1fe.jpg',
            'https://i.pinimg.com/736x/11/39/e8/1139e8e75887d0fe7819764fd69cd566.jpg',
            'https://i.pinimg.com/564x/40/6a/46/406a4672d7860d12508b75ff162b8d23.jpg',
            'https://i.pinimg.com/564x/de/3b/eb/de3beb5744be40f9e9464f953c3dd8fc.jpg',
            'https://i.pinimg.com/736x/c1/20/e2/c120e2e14cad5dc2c0b4435d9f48c563.jpg',
            'https://i.pinimg.com/736x/9e/24/c0/9e24c08c4d804fd2d7b05b855cb4c9c5.jpg',
            'https://i.pinimg.com/736x/5a/e1/ee/5ae1ee6976267907db9042463ca6af2c.jpg',
            'https://i.pinimg.com/564x/63/23/9b/63239ba9918d06c705babe48e3308533.jpg',
            'https://i.pinimg.com/564x/79/17/76/791776cf8f8cbd405a580e463595f367.jpg']
    embed = discord.Embed(
        colour=0xFFFFFF
    )

    embed.set_image(url=choice(urls))

    await ctx.send(embed=embed)

@bot.command()
async def hp_meme(ctx):
    hp_urls = ['https://i.pinimg.com/564x/99/d6/1d/99d61d5e96960c3c18a29aaec4bca78f.jpg',
               'https://i.pinimg.com/564x/c5/1b/d8/c51bd8d0d039417cbd8bf8fba1a76cd7.jpg',
               'https://i.pinimg.com/564x/9c/39/bd/9c39bd249168919860a6fee5a64ac4fa.jpg'
               'https://i.pinimg.com/564x/90/61/96/906196f11fa5a44bf74b38e13b1ee1ee.jpg'
               'https://i.pinimg.com/564x/2b/2b/bf/2b2bbfb13a758ecdb4f52b526e8a87e9.jpg'
               'https://i.pinimg.com/736x/13/5e/8f/135e8fbf6e6e4b6f1d1a425042d3f3bc.jpg'
               'https://i.pinimg.com/564x/04/1f/c5/041fc57083d2905fafb6d78f69dd9b47.jpg'
               'https://i.pinimg.com/564x/50/41/29/504129b3e39c2beb35a91d77bf0c8079.jpg'
               'https://i.pinimg.com/564x/6b/fd/b4/6bfdb43f24abedd3c046fca85aac2fff.jpg'
               'https://i.pinimg.com/564x/b5/ba/f2/b5baf2d11095c7484c0879c12f241908.jpg']
    embed = discord.Embed(color=0xFFFFFF)

    embed.set_image(url=choice(hp_urls))

    await ctx.send(embed=embed)

@bot.command()
async def quiz(ctx):
    courses = ['Math', 'Science', 'Philosophy', 'Geography', 'History', 'PopCulture']
    embed = discord.Embed(
        title='---Blue\'s Quiz---',
        description='Test your knowledge by answering some basic questions in the following fields below.\nTo select a field: Type ".pick" before your chosen subject',
        colour=discord.Color.dark_blue()
    )

    embed.add_field(name='**Math**', value='-five available questions')
    embed.add_field(name='**Science**', value='-ten available questions')
    embed.add_field(name='**Philosophy**', value='-ten available questions')
    embed.add_field(name='**Geography**', value='-ten available questions')
    embed.add_field(name='**History**', value='-five available questions')
    embed.add_field(name='**Pop Culture**', value='-five available questions')
    embed.set_footer(text='---source of question: google---')

    await ctx.send(embed=embed)

    @bot.command()
    async def pick(ctx, subjects: str):
        global user_answer, answer, questions, q_dicts, img, content, embed
        pick = str(f'{subjects}')
        if pick == 'Geography' in courses:
            questions = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
            q_dicts = {
                'q1': 'What is the largest continent?',
                'q2': 'How many oceans are there in the world?',
                'q3': 'Which city has the highest population?',
                'q4': 'Geographically part of Asia but politically part of Europe.',
                'q5': 'In which country the Leaning Tower of Pisa located?',
                'q6': 'What is the largest Island in the world?',
                'q7': 'The country where you can find Dessert of Death',
                'q8': 'In which city the Tower of Bridge located?',
                'q9': 'What is the largest country in Australia/Oceana?',
                'q10': 'What is the coldest continent?',
            }
            random_question = choice(questions)
            if random_question == 'q1':
                answer = 'Asia'
            if random_question == 'q2':
                answer = 'Five'
            if random_question == 'q3':
                answer = 'Tokyo'
            if random_question == 'q4':
                answer = 'Russia'
            if random_question == 'q5':
                answer = 'Italy'
            if random_question == 'q6':
                answer = 'Greenland'
            if random_question == 'q7':
                answer = 'Afghanistan'
            if random_question == 'q8':
                answer = 'London'
            if random_question == 'q9':
                answer = 'Australia'
            if random_question == 'q10':
                answer = 'Antarctica'

            embed = discord.Embed(
                title='Geo Question:',
                description=f'{q_dicts[random_question]}',
                color=0xFFFFFF
            )

            #embed.set_image(url='https://t3.ftcdn.net/jpg/01/62/59/04/360_F_162590489_5IcesYmlOK0RC4T4r5lydft8aQmpCwI7.jpg')

            await ctx.send(embed=embed)

        if pick == 'Math' in courses:
            math_list = ['q1', 'q2', 'q3', 'q4', 'q5']
            math_dicts = {
                'q1': 'Theorem that refers to the relation between the sides of a triangle.',
                'q2': 'It is a vertical number line in graphing and also called the ordinate.',
                'q3': 'What is the angle of the right triangle?',
                'q4': 'How many sides are there in Hexagon?',
                'q5': 'Who worked for the fundamental groundwork of probability?'
            }
            random_math = choice(math_list)
            if random_math == 'q1':
                answer = 'Pythagorean Theorem'
            if random_math == 'q2':
                answer = 'y-axis'
            if random_math == 'q3':
                answer = '90'
            if random_math == 'q4':
                answer = 'six'
            if random_math == 'q5':
                answer = 'Blaise Pascal'

            embed = discord.Embed(title='Math Question:', description=f'{math_dicts[random_math]}', color=0xFFFFFF)

            #embed.set_image(url='https://thumbs.dreamstime.com/b/education-seamless-pattern-doodle-math-geometry-formulas-problems-green-chalkboard-background-128538488.jpg')

            await ctx.send(embed=embed)

        if pick == 'Science' in courses:
            sci_list = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
            sci_dicts = {
                'q1': 'He discovered the concept of Gravity.',
                'q2': 'What was the name of the first man-made satellite launched by the Soviet Union in 1957?',
                'q3': 'What is the hottest planet in our solar system?',
                'q4': 'Which is the main gas that makes up the Earth\'s atmosphere?',
                'q5': 'What name is given for the number of protons found in the nucleus of an atom?',
                'q6': 'What is the symbol of the chemical element **Tungsten**?',
                'q7': 'Who is the *Father of Microbiology?*',
                'q8': 'True or false? The human skeleton is made up of less than 100 bones.',
                'q9': 'Atomic number of *Oganesson*',
                'q10': 'He is the first person who walked on the moon.'
            }
            random_science = choice(sci_list)
            if random_science == 'q1':
                answer = 'Sir Isaac Newton'
            if random_science == 'q2':
                answer = 'Sputnik 1'
            if random_science == 'q3':
                answer = 'Venus'
            if random_science == 'q4':
                answer = 'Nitrogen'
            if random_science == 'q5':
                answer = 'Atomic Number'
            if random_science == 'q6':
                answer = 'W'
            if random_science == 'q7':
                answer = 'Antonie Van Leeuwenhoek'
            if random_science == 'q8':
                answer = 'False'
            if random_science == 'q9':
                answer = '118'
            if random_science == 'q10':
                answer = 'Neil Armstrong'

            embed = discord.Embed(title='Science Question:', description=f'{sci_dicts[random_science]}', color=0xFFFFFF)

            #embed.set_image(url='https://www.clipartkey.com/mpngs/m/196-1960512_cartoon-atom.png')

            await ctx.send(embed=embed)

        if pick == 'Philosophy' in courses:
            philo_list = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']
            philo_dicts = {
                'q1': 'What is the meaning of the term **Philosophy**?',
                'q2': 'Which aims to determine the nature, basis and extent of knowledge?',
                'q3': 'Which theory maintains that an idea is true if it works or settles the problem it deals with?',
                'q4': 'Which is the philosophy that claims ‘we can never have real knowledge of anything’?',
                'q5': 'Which is the study of principles and methods of reasoning?',
                'q6': 'Which is the study of the nature of right and wrong and the distinction between good and evil?',
                'q7': 'Which is the study of art and beauty?',
                'q8': 'The theory that knowledge can be derived from reason by itself, independent of the senses is:',
                'q9': 'Who is the **Father of Philosophy**?',
                'q10': '*The Republic* was written by which philosopher?'
            }
            random_philo = choice(philo_list)
            if random_philo == 'q1':
                answer = 'Love of Wisdom'
            if random_philo == 'q2':
                answer = 'Epistemology'
            if random_philo == 'q3':
                answer = 'Pragmatic Theory'
            if random_philo == 'q4':
                answer = 'Skepticism'
            if random_philo == 'q5':
                answer = 'Logic'
            if random_philo == 'q6':
                answer = 'Ethics'
            if random_philo == 'q7':
                answer = 'Aesthetics'
            if random_philo == 'q8':
                answer = 'Rationalism'
            if random_philo == 'q9':
                answer = 'Socrates'
            if random_philo == 'q10':
                answer = 'Plato'

            embed = discord.Embed(title='Philosophy Question:', description=f'{philo_dicts[random_philo]}',
                                  color=0xFFFFFF)

            #embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdBIMykhDK26nEbytLt7d_I5oXWzjvDVzxgw&usqp=CAU')

            await ctx.send(embed=embed)

        if pick == 'History' in courses:
            hist_list = ['q1', 'q2', 'q3', 'q4', 'q5']
            hist_dicts = {
                'q1': 'Following the appointment of Adolf Hitler as Chancellor in 1933, this flag was adopted as one of the nation\'s dual national flags.',
                'q2': 'The _________ had its origins in the Russian Revolution of 1917',
                'q3': 'It is a historical nation-state and great power that existed from the Meiji Restoration in 1868',
                'q4': 'What is the longest colonized country?',
                'q5': 'Who is the fucking dictator and ruler of Germany in 1933-1945 and killed 40M people. He started that damn WW2 by invading the poor Poland.',
                'q6': 'It is often referred as the *Long Peace*'
            }
            random_history = choice(hist_list)
            if random_history == 'q1':
                answer = 'Nazi Germany'
            if random_history == 'q2':
                answer = 'Soviet Union'
            if random_history == 'q3':
                answer = 'Japan Empire'
            if random_history == 'q4':
                answer = 'Philippines'
            if random_history == 'q5':
                answer = 'Adolf Hitler'
            if random_history == 'q6':
                answer = 'The Cold War (1945-1991)'


            embed = discord.Embed(title='History Question:', description=f'{hist_dicts[random_history]}',
                                  color=0xFFFFFF)

            #embed.set_image(url='https://www.jchistorytuition.com.sg/wp-content/uploads/2019/03/Sovietisation-Leslie-Illingworth-June-1947.gif')

            await ctx.send(embed=embed)



        if pick == 'PopCulture' in courses:
            pop_list = ['q1', 'q2', 'q3', 'q4', 'q5']
            pop_dicts = {
                'q1': 'Who is the half-blood prince in the Harry Potter',
                'q2': 'Who is the author of the novel *The Lord of the Rings*?',
                'q3': 'The actor who played as *Jon Snow* in Game of Thrones.',
                'q4': 'Most followed person in Instagram.\n *Hint: He is a football player*',
                'q5': 'How many views does *Dynamite* by BTS currently have in YT?'
            }
            random_pop = choice(pop_list)
            if random_pop == 'q1':
                answer = 'Severus Snape'
            if random_pop == 'q2':
                answer = 'J.R.R Tolkien'
            if random_pop == 'q3':
                answer = 'Kit Harrington'
            if random_pop == 'q4':
                answer = 'Christiano Ronaldo'
            if random_pop == 'q5':
                answer = '1.5 Billion views'
            embed = discord.Embed(title='Pop Culture Question:', description=f'{pop_dicts[random_pop]}', color=0xFFFFFF)

            #embed.set_image(url='https://www.rd.com/wp-content/uploads/2018/12/pop-culture-trivia-pop-art-collage.jpg')

            await ctx.send(embed=embed)


        @bot.command()
        async def ans(ctx, a: str):
            ans_embed = discord.Embed(
                title='Answer: ',
                description=f'{a}',
                color=0x000FF
            )
            ans_embed.set_footer(text=f"Correct answer: {answer}")

            await ctx.send(embed=ans_embed)


@bot.command()
async def weather(ctx, city):
    api = '9d111192da290d712efcb8d834add9e3'
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api))
    r = r.json()

    city_name = r['name']
    tz = r['timezone']
    temp = r['main']['temp']
    pres = r['main']['pressure']
    humd = r['main']['humidity']
    ws = r['wind']['speed']

    embed = discord.Embed(
        title='Aladdin\'s Forecaster',
        description=f'**City Name:** {city_name}\n**Timezone:** {tz}\n**Temperature:** {temp}\n**Pressure:** {pres}\n**Humidity:** {humd}\n**Wind Speed:** {ws}',
        color=0x000FF)

    #embed.add_field(name='City Name:', value=f'{city_name}', inline=False)
    #embed.add_field(name='Timezone:', value=f'{tz}', inline=False)
    #embed.add_field(name='Temperature:', value=f'{temp}', inline=False)
    #embed.add_field(name='Pressure:', value=f'{pres}', inline=False)
    #embed.add_field(name='Humidity:', value=f'{humd}', inline=False)
    #embed.add_field(name='Wind Speed:', value=f'{ws}', inline=False)weather-icon-with-col
    embed.set_thumbnail(url='https://static.vecteezy.com/system/resources/previews/003/353/952/non_2x/orful-style-free-vector.jpg')

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def aki(ctx):
    await ctx.send('', file=discord.File('kun.jpg'))

@bot.command()
async def anime(ctx):
    a = requests.get('https://animechan.vercel.app/api/random')
    a = a.json()

    title = a['anime']
    character = a['character']
    quote = a['quote']

    embed = discord.Embed(
        title=f'{title}', description=f'{quote}', color=0x000FF
    )

    embed.set_footer(text=f'-{character}')
    await ctx.send(embed=embed)


@bot.command()
async def hi(ctx):
    await ctx.send("Hello, " + ctx.message.author.mention + '!')

bot.run(TOKEN)
