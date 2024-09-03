import streamlit as st
from datetime import datetime

# Include the Philosopher font from Google Fonts
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Philosopher&display=swap" rel="stylesheet">
    <style>
    * {
        font-family: 'Philosopher', sans-serif;
    }
    .title-text {
        font-size: 50px;
        font-weight: bold;
        color: #F8AE04;
    }
    .header-text {
        font-size: 40px;
        font-weight: bold;
        color: #FFFFFF;
    }
    .subheader-text {
        font-size: 30px;
        font-weight: bold;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
section = st.sidebar.radio(
    "My Mundane Autobiography",
    [
        "Introduction",
        "My Early Life",
        "Education and Learning",
        "Hobbies and Interests",
        "The Future Ahead",
    ],
)

# Title
st.markdown(
    """
    <p class ="title-text">
        My Mundane Autobiography
    </p>
    """,
    unsafe_allow_html=True,
)

# Audio
st.audio("audio/genshinbgm.mp3")

# Subheader
st.markdown(
    """
    <p class="subheader-text">
        The Uneventful Journey of My Life
    </p>
    """,
    unsafe_allow_html=True,
)

# Custom horizontal line using HTML/CSS
st.markdown(
    "<hr style='border: 1px solid #ccc; margin: 25px 0;'>", unsafe_allow_html=True
)

# Introduction
if section == "Introduction":
    st.write(
        """
    My name is Rynze RJ Ferrer Lozano, a 22-year old BSIT 4th year student, and I welcome you to my mundane autobiography.
    """
    )

    st.image(
        "images/profile.jpg",
        caption="Photo taken at the CIT-U library",
        use_column_width=True,
    )

# Section 1
elif section == "My Early Life":
    st.markdown(
        """
        <p class=header-text>
            My Early Life
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
    I was born on February 25, 2002, at a hospital in Cebu City, which is also a holiday for the EDSA Revolution Anniversary. 
    At a young age, I was naughty by nature and a troublemaker at heart. Perhaps, I was the happiest at this stage of my life. 
    I would run around in our little town and play with my friends all day long. Oddly enough, I had gained the most scars so far in my life
    as a child. I consider these as proof that I had been brave enough to even expose myself to adversities and risks in life.
    """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            "images/kid1.jpg",
            caption="Climbing a coconut tree in Negros Oriental",
            use_column_width=True,
        )

    with col2:
        st.image(
            "images/kid2.jpg",
            caption="Posing with a basket ball at home",
            use_column_width=True,
        )

# Section 2
elif section == "Education and Learning":
    st.markdown(
        """
        <p class=header-text>
            Education and Learning
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
    My academic journey was quite a huge influence on my becoming. I was first enrolled in a daycare center, where I weaned off my separation
    anxiety with my parents for school. Then, I had my primary education at a Catholic school called Saint Louis College Cebu, which was called
    Saint Louis School of Mandaue when I first got in. I was only an average student for most of my time here, until the last two years where I
    was able to place fourth overall in my entire grade.
    """
    )

    primary_images = ["images/daycare.jpg", "images/elem.jpg", "images/elemgrad.jpg"]

    primary_captions = [
        "Kasuntingan Daycare Center",
        "White card achiever at SLCC",
        "Elementary Graduation Ceremony",
    ]

    cols = st.columns(len(primary_images))

    for i, col in enumerate(cols):
        col.image(primary_images[i], caption=primary_captions[i], use_column_width=True)

    st.write("")
    st.write(
        """
    My mother saw this potential and made me try applying for a scholarship at Mandaue City Science High School, where I eventually passed into 
    and had my secondary education as a science high school scholar. Here, my brain chemistry seemed to have been altered permanently due to extreme 
    pressure and hardships. Aside from maintaining my scholarship, I was still able to atleast get into the top 10 of my class a handful of times.
    """
    )

    secondary_images = ["images/newhigh.jpg", "images/high.jpg", "images/highgrad.jpg"]

    secondary_captions = [
        "First photo as a ManSci student",
        "Awarading ceremony",
        "Senior Highschool Graduation",
    ]

    cols = st.columns(len(secondary_images))

    for i, col in enumerate(cols):
        col.image(
            secondary_images[i], caption=secondary_captions[i], use_column_width=True
        )

    st.write("")
    st.write(
        """
    After graduating high school during the coronavirus pandemic, I had a period of uncertainty and confusion. I was not sure where I should be 
    headed next, but my parents still had me apply for another scholarship for college. And when I passed for the DOST scholarship, I was still 
    unsure of what to do next until my father advised me to go to his alma mater, Cebu Institute of Technology - University, and take the BSIT course. 
    As a freshman, in the later stages of the pandemic where online classes were the norm, I had a rough time adjusting to the state of affairs. 
    Still, I was able to persevere and even received recognition for my efforts as an achiever. Moving forward, I am now a senior nearing 
    my hopeful graduation.
    """
    )

    college_images = [
        "images/freshman.jpg",
        "images/flexhibit1.jpg",
        "images/flexhibit2.jpg",
    ]

    college_captions = [
        "First selfie in the CIT-U library",
        "Flexhibit awardee",
        "Flexhibit 2.0 awardee",
    ]
    cols = st.columns(len(college_images))

    for i, col in enumerate(cols):
        col.image(college_images[i], caption=college_captions[i], use_column_width=True)

# Section 3
elif section == "Hobbies and Interests":
    st.markdown(
        """
        <p class=header-text>
            Hobbies and Interests
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
    Ever since I was young, the influence brought by my father with anime became the core of my interests and hobbies. My childhood anime is [One Piece](https://en.wikipedia.org/wiki/One_Piece),
    and I cannot count how many times I had rewatched the entirety of it, as well as its manga. Then, I also became addicted to playing online games starting
    with [Adventure Quest Worlds](https://www.aq.com/), even more with [Dragon Nest](https://www.youtube.com/watch?v=Xm1fXkTsIXQ), and then with [Genshin Impact](https://genshin.hoyoverse.com/en/). Now, I have become more tame with casually playing games such as [Mobile Legends](https://www.mobilelegends.com/) and [Roblox](https://www.roblox.com/).
    Instead, I have become a hardcore reader of novels. I have read numerous novels with a variety of genres, with my three most favorite books:
    [Lord of the Mysteries](https://www.webnovel.com/book/lord-of-the-mysteries_11022733006234505), [Omniscient Reader's Viewpoint](https://www.lightnovelworld.co/novel/orv-wn-16091308), and [Solo Leveling](https://www.webnovel.com/book/solo-leveling(only-i-level-up)_12507348206677105).
    """
    )

    hobbies_interests_images = [
        "images/onepiece.jpg",
        "images/genshin.jpg",
        "images/lotm.jpg",
    ]

    hobbies_interests_captions = [
        "One Piece",
        "Genshin Impact",
        "Lord of the Mysteries",
    ]
    cols = st.columns(len(hobbies_interests_images))

    for i, col in enumerate(cols):
        col.image(
            hobbies_interests_images[i],
            caption=hobbies_interests_captions[i],
            use_column_width=True,
        )

# Section 4
elif section == "The Future Ahead":
    st.markdown(
        """
        <p class=header-text>
            The Future Ahead
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
    As much as I plan ahead for the day, I am not really someone who is fixated on what is yet to come. I prefer living in the moment and enjoying
    my life as it goes by. I can say that I like drifting along the currents. But as an adult who should take responsibility for myself, I may be quite
    immature for staying in a bubble of my own making. Still, I should be able to make use of my degree to come and take it one step at a time. As I am
    right now, I have yet to truly decide on a path I should take, but I will make that decision soon enough. Wish me luck.
    """
    )

    st.image(
        "images/forward.jpg",
        caption="Photo taken at SM Seaside Cebu",
        use_column_width=True,
    )

# Footer with Current Date
st.write("Last updated on: ", datetime.now().strftime("%Y-%m-%d"))
