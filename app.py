import streamlit as st
import random

# List of quotes
quotes=[
    """Relationships are for those who cannot live single""",
    '''You have no other option. You have to do that work although your brain will tell you cantdo..

    you have no other option. you have to do that work thats it - “David Goggins”''',
    
 '''"An idiot with a plan can beat a genius without a Plan"- Warren Buffet''',
 '''DISCIPLINE is bridge between where you are now and the future of your dreams''',
 '''The greatest sin is tothink of yourself as weak  -Swami Vivekananda ''',
 '''NOBODY WATCHES YOU MORE THAN A WOMAN WHO LEFT YOU.SHOW HER THAT SHE MADE MISTAKE''',
 '''Your goals are moreimportant than love rightnow.''',
 '''"Remember, women break rules formen they like and make rules formen they don't."-Andrew Tate''',
 '''Growth comes withalot of goodbyes''',
 '''"Live in the present moment, neither dwellingon the past nor worrying about the future."-Lord Krishna''',
 '''Don't get upset with people orsituation because both arepowerless without your reaction.Don't react..SHREE KRISHNA''',
 '''EXCUSES MAKE TODAY EASIER BUT TOMORROWHARDER.DISCIPLINE MAKES TODAY HARD BUT TOMORROWEASIER.''',
 '''The gap between the life youwant and the life you areliving is called mindset, focus,and consistency''',
 '''"If you set your goals ridiculouslyhigh and it's a failure, you will failabove everyone else's success."-James Cameron''',
 '''Control your lust & you'll understand how boring 90%of women are.''',
 '''Don't take revenge, leave them and becometheir biggest regret for losing you''',
 '''If you want to buy without looking at the prise, you have to work without looking at the clock''',
 '''Get Physically fit-Workouts
    Get mentally fit-By reading books,
    Get socially fit-By Interacting with people'''
]

def main():
    
    random_quote = random.choice(quotes)
    st.write(random_quote)

if __name__ == "__main__":
    main()
