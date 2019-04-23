import urllib.request
# print("enter your name")
# dwn_link = 'https://doc-0c-2s-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/8331b83eqn5esho11ipq0mbsr9c65j35/1553004000000/03685162078622018745/*/1rxwKr3ZnPjpcJ02W24uo9Rvup-9OLyLM?e=download'
# file_name = "personname.mp4"


def dwn_video(dwn_link, file_name):
    path = 'videos/'
    name = path + file_name + '.mp4'
    urllib.request.urlretrieve(dwn_link, name)
